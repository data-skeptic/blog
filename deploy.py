import json
import boto3
import os
import fileinput
import pandas as pd
import re
import base64
import hashlib
import mimetypes
import wget
import uuid
import string
import zipfile
import requests
import sys
import bs4
import shutil
import io
import nbformat
import hashlib
import datetime
import bs4 as soup
import logging
from urllib.parse import quote
import six
from summarizer import get_desc, get_title, get_pretty_name
from parsers import parsers

import json

def lambda_handler(event, context):
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }


logname = sys.argv[0]
logger = logging.getLogger(logname)
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
logger.setLevel(logging.DEBUG)

logfile = '/var/tmp/' + logname + '.log'
ldir = os.path.dirname(logfile)
if not(os.path.isdir(ldir)):
    os.makedirs(ldir)
hdlr = logging.FileHandler(logfile)

hdlr.setFormatter(formatter)
logger.addHandler(hdlr) 
stdout = logging.StreamHandler()
stdout.setFormatter(formatter)
logger.addHandler(stdout)



def unzip(source_filename, dest_dir):
    zf = zipfile.ZipFile(source_filename)
    zf.extractall(dest)

def get_filename(repo, branch):
    filename = repo[repo.rfind('/')+1:] + '-' + branch + '.zip'
    return filename

def download(repo, branch, dest, filename):
    src = repo + '/archive/' + branch +'.zip'
    if not(os.path.isdir(dest)):
        os.mkdir(dest)
    fname = wget.download(src)
    os.rename(fname, filename)

def get_src_dict(repo_root, parent):
    d = {}
    suffixes = parsers.keys()
    rootdir = repo_root.rstrip(os.sep)
    start = rootdir.rfind(os.sep) + 1
    for path, dirs, files in os.walk(rootdir):
        for file in files:
            i = file.rfind('.')
            if i != -1:
                ext = file[i:]
                if ext in suffixes:
                    d[path + '/' + file] = True
    return d


def contained_in_tag(s, pos, tag):
    stag = "<" + tag.lower() + ""
    etag = "</" + tag.lower() + ">"
    before = s[0:pos].lower()
    after  = s[pos:].lower()
    i = before.rfind(stag)
    if i == -1:
        return False
    i2 = before.rfind(etag)
    if i2 != -1 and i < i2:
        return False
    j = after.find(etag)
    if j == -1:
        return False
    j2 = after.find(stag)
    if j2 < j:
        return False
    return True


def next_delimiter(s, a, is_closing, delim='$'):
    i = s.find(delim, a)
    if i > 0:
        check_for_preceeding_whitespace = s[i-1:i]
        if not(is_closing) and not(check_for_preceeding_whitespace.isspace()) and not(check_for_preceeding_whitespace==">"):
            return next_delimiter(s, is_closing, i+1)
        if contained_in_tag(s, i, "code"): # For R stuff
            return next_delimiter(s, is_closing, i+1)
        if contained_in_tag(s, i, "pre"):  # For R stuff
            return next_delimiter(s, is_closing, i+1)
    if i == -1:
        return -1
    if i > 0:
        before = s[i-1]
        if before == '\\':
            return next_delimiter(s, is_closing, a+1)
    return i

def render_uri(s3, bucket, absfile, parser):
    buck = s3.Bucket(bucket)
    rendered_map = {}
    contents = parser(absfile)
    title = get_title(absfile, contents)
    desc = get_desc(contents)
    i = 0
    ranges = []
    while i < len(contents):
        i = next_delimiter(contents, i, False)
        if i != -1:
            j = next_delimiter(contents, i+1, True)
            if j != -1:
                ranges.append([i, j+1])
        if i == -1 or j == -1:
            i = len(contents)
        else:
            i = j + 1
    logger.debug("Found " + str(len(ranges)) + " latex statements to render.")
    updated_contents = replace_latex_with_svgs(ranges, contents, buck, rendered_map)
    a = absfile.rfind('/') + 1
    b = absfile.rfind('.')
    fname = absfile[a:b]
    logger.debug('Now update for knitr images')
    updated_contents = knitr_img_handling(s3, title, absfile, updated_contents, bucket, fname)
    return updated_contents


def escape_latex(latex):
    fname = latex.replace("\\", "\\\\") \
    .replace(":", "%3A") \
    .replace(";", "%3B") \
    .replace('"', '\"') \
    .replace("|", "\\|") \
    .replace("<", "%3C") \
    .replace(">", "%3E") \
    .replace("*", "%2A") \
    .replace("=", "%3D") \
    .replace("+", "%2B") \
    .replace("?", "%3F") \
    .replace("/", "%2F")
    if fname.startswith('\\'):
        fname = 'l_' + fname
    return fname


def replace_latex_with_svgs(ranges, contents, buck, rendered_map):
    logger.debug("replace_latex_with_svgs")
    # Go backwards because this is destructive of the source
    # Backwards makes debugging easier
    i = len(ranges) - 1
    while i >= 0:
        r = ranges[i]
        b = r[0]
        e = r[1]
        latex = contents[b+1:e-1]
        m = len(latex)
        if m > 1000:
            print("Latex string is too long, probably an error if parsing")
            sys.exit(-1)
        if m > 100:
            m = 100
        print('latex raw:', latex[0:m])
        if type(latex) != str:
            latex = latex.decode('utf-8')
        latex = latex.replace('&amp;', '&')
        latex = latex.replace('&lt;', '<')
        latex = latex.replace('&gt;', '>')
        blatex = latex
        fname = escape_latex(latex)
        fname = fname + ".svg"
        s3key = "latex/" + fname
        objs = list(buck.objects.filter(Prefix=s3key))
        if len(objs) > 0:
            rendered_map[s3key] = False
        else:
            rendered_map[s3key] = False
        #
        fnn = quote(fname).replace('%20', '+')
        svguri = "http://s3.amazonaws.com/" + bucket + "/latex/" + fnn
        if rendered_map[s3key]:
            logger.debug("SVG already exists: " + s3key)
        else:
            logger.debug("Going to render " + latex + ' as ' + fname)
            render_and_upload_latex(latex, fname, buck, s3key)
            rendered_map[s3key] = True
        imgTag = "<img className='latex-svg' src='" + svguri + "' alt='" + blatex + "' />"
        if type(contents) != str:
            contents = contents.decode('utf-8')
        contents = contents[0:b] + imgTag + contents[e:len(contents)]
        i -= 1
    #
    return contents


def render_and_upload_latex(latex, fname, buck, s3key):
    logger.debug(latex)
    cmd = '/usr/local/lib/node_modules/mathjax-node/bin/tex2svg '
    cmd += '"' + latex + '"'
    rendered = os.popen(cmd).read()
    f = open(fname, 'w')
    f.write(rendered)
    f.close()
    f = open(fname, 'rb')
    fake_handle = f
    fname = fname.encode('utf-8')
    res = buck.put_object(Key=s3key, Body=fake_handle, ContentType='image/svg+xml', ACL='public-read')
    os.remove(fname)


def render_item(base_url, s3, s3client, bucket, srcfiles, item, env, blog_id):
    logger.debug("render_item")
    ext = item['ext']
    parser = parsers[ext]
    absfile = item['absfile']
    uri = item['uri']
    s3key = item['rendered']
    f = open(absfile, 'rb')
    c = f.read()
    f.close()
    chash = hashlib.md5(c).hexdigest()
    render = True
    isNew = blog_id == -1
    if not(isNew):
        if item['oldHash'] == chash:
            render = False
            logger.warn("Ignoring due to no updates")
        else:
            render = True
    if render:
        logger.warn("Rendering " + absfile)
        contents = render_uri(s3, bucket, absfile, parser)

        title = get_title(absfile, contents)
        item_metadata = {
            "absfile": absfile,
            "srcfiles": srcfiles, 
            "contents": contents, 
            "title": title, 
            "bucket": bucket, 
            "uri": uri, 
            "s3key": s3key, 
            "env": env,
            "hash": chash
        }
        render_blog(base_url, s3, s3client, item_metadata, blog_id)


def post_already_exists(base_url, s3key):
    url = base_url + "/blog/list?src_file=" + s3key
    r = requests.get(url)
    lst = json.loads(r.content.decode('utf-8'))
    if len(lst) > 0:
        logger.debug("exists, update")
        blog_id = lst[0]['blog_id']
        return blog_id
    else:
        logger.debug("not found, adding as new")
        return -1

def render_blog(base_url, s3, s3client, item_metadata, blog_id):
    logger.debug("render_blog")
    absfile = item_metadata['absfile']
    srcfiles = item_metadata['srcfiles']
    contents = item_metadata['contents']
    title = item_metadata['title']
    bucket = item_metadata['bucket']
    uri = item_metadata['uri']
    chash = item_metadata['hash']
    s3key = item_metadata['s3key']
    env = item_metadata['env']
    now = datetime.datetime.now()
    n = now.strftime('%Y-%m-%d')
    desc = get_desc(contents)
    if desc == '':
        desc = title
    a = len(bucket)+1
    i = uri.rfind('.')
    ext = uri[i:]
    s3key = uri[a:i] + '.htm'
    if s3key[0]=='/':
        s3key = s3key[1:]
    logger.info('Deploying to: ' + bucket + '/' + s3key)
    prettyname = get_pretty_name(s3key, title)
    save_locally = True
    if save_locally:
        logger.info("Saving copy locally as output.htm")
        f = open('output.htm', 'w')
        f.write(contents)
        f.close()
    fake_handle = io.BytesIO(contents.encode('utf-8'))
    res = s3.Bucket(bucket).put_object(Key=s3key, Body=fake_handle)
    x = os.path.basename(s3key)
    a = s3key.rfind('/')
    b = s3key.rfind('.')
    dname = 'src-' + s3key[a+1:b]
    keypath = s3key[0:len(s3key)-len(x)] + dname + '/'
    for src in srcfiles:
        s3key2 = keypath + os.path.basename(src)
        logger.info('Deploying source file: ' + src + ' to ' + s3key2)
        #i = absfile.rfind('/')
        #abspath = absfile[0:i]
        #fp = open(abspath + '/' + dname + '/' + src, 'rb')
        fp = open(src, 'rb')
        data = fp.read()
        fp.close()
        res = s3.Bucket(bucket).put_object(Key=s3key2, Body=data, ACL='public-read')
    author = 'Kyle'
    ritem = {
        'uri': uri,
        'ext': ext,
        'c_hash': chash,
        'author': fix_string_for_db(author),
        'desc': fix_string_for_db(desc),
        'prettyname': prettyname,
        's3key': s3key,
        'title': fix_string_for_db(title),
        'absfile': absfile
    }
    save_item(base_url, blog_id, ritem)


def fix_string_for_db(s):
    return s.replace(u"\u2018", "'").replace("’", "'").replace("'", "\\'")

def save_item(base_url, blog_id, ritem):
    data = {
        "blog_id": blog_id,
        "details": ritem
    }
    url = base_url + "/blog/upsert"
    r = requests.post(url, json.dumps(data))
    s = r.content.decode('utf-8')
    o = json.loads(s)
    if o['success'] == 1:
        print("Success!")
    else:
        print(s)


def clean_up(dest):
    shutil.rmtree(dest)


def replacement(match):
    fn = match.groups()[0]
    if os.path.isfile(fn):
        return 'src="data:%s;base64,%s"' % (mimetypes.guess_type(fn)[0], base64.b64encode(open(fn, 'rb').read()))
    return match.group()


def get_r_images(title, fname, bucketpath, c):
    logger.debug('get_r_images')
    cx = c
    i = 0
    ec = 0
    fname = fname[0:len(fname) - len(".html")]
    soup = bs4.BeautifulSoup(c, "lxml")
    imgtags = soup.find_all('img')
    imgs = []
    j = 0
    logger.debug(len(imgtags))
    for i, tag in enumerate(imgtags):
        tpl = "<img src='{src}' class='r-plot' alt='{alt}' title='{title}' />"
        oclass = tag.get('class')
        alt = tag.get('alt')
        is_r_plot = False
        #print(oclass, alt, tag)
        if oclass is not None:
            if type(oclass) == list:
                oclass = oclass[0]
            if oclass == 'plot':
                is_r_plot = True
        elif alt is not None:
            if alt.startswith('plot of chunk'):
                is_r_plot = True
                #print("ignoring " + alt)
        if is_r_plot:
            print('IS R PLOT!!!!!!!!!!!!!!!')
            osrc = tag.get('src')
            src = bucketpath + fname + "_" + str(i) + ".png"
            alt = title + " image #" + str(i)
            newtag = tpl.format(src=src, alt=alt, title=alt)
            s = str(tag)
            j = cx.find(s)
            z = 0
            q = len(s) - 2
            while z != -1:
                z = cx.lower().find(s[0:q], z+1)
                z2 = cx.find('>', z+1)
                if z != -1:
                    cx = cx[0:z] + newtag + cx[z2+1:]
            imgs.append({"src": osrc, "dest": src})
    print(imgs)
    return cx, imgs


def imgs_to_s3(buck, imgs):
    for img in imgs:
        dest = img['dest']
        s3key = dest[len("http://s3.amazonaws.com/dataskeptic.com/"):]
        src = img['src']
        logger.debug("Pushing {src} to {key}".format(src=src, key=s3key))
        res = buck.put_object(Key=s3key, Body=open(src, 'rb'))

def knitr_img_handling(s3, title, absfile, contents, bucket, fname):
    i = absfile.rfind('/')
    buck = s3.Bucket(bucket)
    bucketpath = 'http://s3.amazonaws.com/' + bucket + '/' + absfile[0:i+1] + 'src-' + fname + '/'
    i = 0
    ec = 0
    while i != -1:
        i = contents.find('After reading', i+1)
        if i != -1:
            ec += 1
    if ec > 1:
        for j in range(20):
            print('________ERROR@c0@______', ec)
    c2, imgs = get_r_images(title, fname, bucketpath, contents)
    i = 0
    ec = 0
    while i != -1:
        i = c2.find('After reading', i+1)
        if i != -1:
            ec += 1
    if ec > 1:
        for j in range(20):
            print('________ERROR@c2@______', ec)
    imgs_to_s3(buck, imgs)
    if os.path.exists(fname + '.html'):
        os.remove(fname + '.html')
    for img in imgs:
        pass
        #os.remove(img['src'])
    return c2


def render_one(base_url, s3, s3client, absfile, bucket, env):
    logger.debug("render_one")
    cwd = os.getcwd()
    key = '/blog'
    i = cwd.find(key)
    if i == -1:
        print("I can't determine the path to put this on the blog")
        sys.exit(1)
    if cwd[-1] != '/':
        cwd = cwd + '/'
    uri = cwd[i+len(key):] + absfile
    uri = bucket + uri
    ext = absfile[absfile.rfind('.'):]
    parser = parsers[ext]
    fname = os.path.basename(absfile)
    path = absfile[0:len(absfile) - len(fname)]
    p = fname.rfind('.')
    d = path + "src-" + fname[0:p]
    srcfiles = []
    if os.path.isdir(d):
        sf = os.listdir(d)
        for src in sf:
            if src != '.DS_Store':
                sc = d + '/' + src
                srcfiles.append(sc)
    contents = parser(absfile)
    r_dir = path + fname[0:p] + '_img'
    if os.path.isdir(r_dir):
        srcfiles2 = os.listdir(r_dir)
        for isrc in srcfiles2:
            if isrc != '.DS_Store':
                isrc = r_dir + '/' + isrc
                srcfiles.append(isrc)
    f = open(absfile, 'rb')
    c = f.read()
    f.close()
    chash = hashlib.md5(c).hexdigest()
    a = len(bucket)+1
    i = uri.rfind('.')
    s3key = uri[a:i] + '.htm'
    title = get_title(absfile, contents)
    i = s3key.rfind('/')
    if i == -1:
        i = 0
    else:
        i += 1
    fname = s3key[i:]
    item_metadata = {
        "absfile": absfile,
        "srcfiles": srcfiles, 
        "contents": contents, 
        "title": title, 
        "bucket": bucket, 
        "uri": uri, 
        "s3key": s3key, 
        "env": env,
        "hash": chash,
        "ext": ext,
        "rendered": s3key,
        "oldHash": "" # always re-render in manual mode
    }
    logger.debug("Going to render " + bucket + '/' + s3key)
    blog_id = post_already_exists(base_url, s3key)
    render_item(base_url, s3, s3client, bucket, srcfiles, item_metadata, env, blog_id)


def decode_base64(data):
    """Decode base64, padding being optional.

    :param data: Base64 data as an ASCII byte string
    :returns: The decoded byte string.

    """
    missing_padding = len(data) % 4
    if missing_padding != 0:
        data += b'='* (4 - missing_padding)
    return base64.decodestring(data)


if __name__ == "__main__":
    logger.debug("Starting")
    #
    if len(sys.argv) != 3:
        print("ERROR: incorrect parameters")
        print("USAGE: python3 deploy.py meta/2018/post-name.md dev.json")
        sys.exit(-1)

    post_absfilename = sys.argv[1]
    config_filename = sys.argv[2]
    config = json.load(open(config_filename, 'r'))
    accessKey = config['accessKey']
    secretKey = config['secretKey']
    bucket    = config['bucket']
    env = config_filename.replace('.json', '')
    base_url = config['api'] + env
    region = "us-east-1"
    s3 = boto3.resource('s3', aws_access_key_id=accessKey, aws_secret_access_key=secretKey, region_name=region)
    s3client = boto3.client('s3', aws_access_key_id=accessKey, aws_secret_access_key=secretKey, region_name=region)
    render_one(base_url, s3, s3client, post_absfilename, bucket, env)



