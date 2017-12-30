import json
import boto3
import os
import fileinput
import re
import base64
import hashlib
import mimetypes
import wget
import uuid
import string
import zipfile
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

def get_content_dict(table):
    response = table.scan()
    items = response['Items']
    d = {}
    for item in items:
        uri = item['uri']
        d[uri] = item
    return d

def new_content_render_plan(repo_root, bucket, src_dict, content_dict, ignore):
    plan = []
    s = len(repo_root)
    srcs = src_dict.keys()
    oldHash = None
    for src in srcs:
        uri = src[s:]
        uri = bucket + uri
        publish = True
        for ig in ignore:
            if uri.find(ig) >= 0:
                publish = False
        if publish:
            isNew = True
            if uri in content_dict:
                isNew = False
                oldHash = content_dict[uri]['c_hash']
            ext = uri[uri.rfind('.'):]
            fname = os.path.basename(src)
            path = src[0:len(src) - len(fname)]
            p = fname.rfind('.')
            d = path + "src-" + fname[0:p]
            srcfiles = []
            if os.path.isdir(d):
                srcfiles = os.listdir(d)
            plan.append({"absfile": src, "srcfiles": srcfiles, "uri": uri, "isNew": isNew, "oldHash": oldHash})
    return plan



def next_delimiter(s, a, delim='$'):
    i = s.find(delim, a)
    if i == -1:
        return -1
    if i > 0:
        before = s[i-1]
        if before == '\\':
            return next_delimiter(s, a+1)
    return i

def render_uri(s3, bucket, absfile, parser):
    logger.debug('render_uri')
    buck = s3.Bucket(bucket)
    rendered_map = {}
    contents = parser(absfile)
    #if type(contents) == bytes:
    #    contents = contents.decode('utf-8')
    title = get_title(absfile, contents)
    desc = get_desc(contents)
    i = 0
    ranges = []
    while i < len(contents):
        i = next_delimiter(contents, i)
        if i != -1:
            j = next_delimiter(contents, i+1)
            if j != -1:
                ranges.append([i, j+1])
        if i == -1 or j == -1:
            i = len(contents)
        else:
            i = j + 1
    updated_contents = replace_latex_with_svgs(ranges, contents, buck, rendered_map)
    a = absfile.rfind('/') + 1
    b = absfile.rfind('.')
    fname = absfile[a:b]
    updated_contents = knitr_img_handling(s3, title, absfile, updated_contents, bucket, fname)
    return updated_contents


def escape_latex(latex):
    return latex.replace("\\", "\\\\") \
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
        if type(latex) != str:
            latex = latex.decode('utf-8')
        #latex = latex.replace('&amp;', '&')
        #fname = fname.replace('\\', '_')
        #fname = fname.replace(' ', '_')
        #fname = fname.replace('=', '_')
        blatex = latex
        latex = escape_latex(latex)
        fname = latex + ".svg"
        s3key = "latex/" + fname
        objs = list(buck.objects.filter(Prefix=s3key))
        if len(objs) > 0:
            rendered_map[s3key] = False
        else:
            rendered_map[s3key] = False
        #
        svguri = "http://s3.amazonaws.com/" + bucket + "/latex/" + quote(fname)
        if rendered_map[s3key]:
            logger.debug("SVG already exists: " + s3key)
        else:
            logger.debug("Going to render " + s3key)
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
    # TODO: use prettier filenames
    #fname = hashlib.sha224(rendered.encode('utf-8')).hexdigest() + ".svg"
    #print(cmd)
    f = open(fname, 'w')
    f.write(rendered)
    f.close()
    # TODO: Check if it already exists since has is unique
    #fake_handle = StringIO(rendered)
    f = open(fname, 'rb')
    fake_handle = f
    #print(svguri)
    fname = fname.encode('utf-8')
    res = buck.put_object(Key=s3key, Body=fake_handle, ContentType='image/svg+xml')
    os.remove(fname)


def execute_plan(plan, s3, s3client, bucket, table, env):
    summary = []
    for item in plan:
        srcfiles = plan['srcfiles']
        s3key = item['rendered']
        isNew = not(post_already_exists(table, item_metadata, s3client, bucket, s3key))
        render_item(s3, s3client, bucket, table, srcfiles, item, env, isNew)
        uri = item['uri']
        summary.append({"uri": uri})
    return summary


def render_item(s3, s3client, bucket, table, srcfiles, item, env, isNew):
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
        render_blog(s3, s3client, table, item_metadata, isNew)


def post_already_exists(table, item_metadata, client, bucket, s3key):
    response = client.list_objects_v2(
        Bucket=bucket,
        Prefix=s3key,
    )
    for obj in response.get('Contents', []):
        print(obj['Key'], '=', s3key)
        if obj['Key'] == s3key:
            uri = item_metadata['uri']
            response = table.get_item(
                Key={"uri": uri}
            )
            if 'Item' in response:
                return True
    return False

def render_blog(s3, s3client, table, item_metadata, isNew):
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
    print("bucket=" + bucket + " s3key=" + s3key)
    res = s3.Bucket(bucket).put_object(Key=s3key, Body=fake_handle)
    x = os.path.basename(s3key)
    a = s3key.rfind('/')
    b = s3key.rfind('.')
    dname = 'src-' + s3key[a+1:b]
    keypath = s3key[0:len(s3key)-len(x)] + dname + '/'
    for src in srcfiles:
        s3key2 = keypath + src
        logger.info('Deploying source file: ' + s3key2)
        i = absfile.rfind('/')
        abspath = absfile[0:i]
        fp = open(abspath + '/' + dname + '/' + src, 'rb')
        data = fp.read()
        fp.close()
        res = s3.Bucket(bucket).put_object(Key=s3key2, Body=data)
    author = 'Kyle'
    if env == 'prod':
        env = 'master'
    publish_date = datetime.datetime(2099,1,1)
    ritem = {
        'uri': uri,
        'ext': ext,
        'last_rendered': n,
        'c_hash': chash,
        'date_discovered': n,
        'env': env,
        'author': author,
        'desc': desc,
        'prettyname': prettyname,
        'publish_date': str(publish_date.date()),
        'rendered': s3key,
        'title': title,
        'absfile': absfile
    }
    save_item(isNew, table, ritem, uri, n)


def save_item(isNew, table, ritem, uri, n):
    logger.info("Updating database for " + uri)
    if isNew:
        logger.debug("isNew")
        print(ritem)
        response = table.put_item(
            Item=ritem
        )
    else:
        logger.debug("updating")
        response = table.update_item(
            Key={
                'uri': uri
            },
            UpdateExpression="set last_rendered = :n, c_hash=:h",
            ExpressionAttributeValues={
                ':n': n,
                ':h': ritem['c_hash']
            },
            ReturnValues="UPDATED_NEW"
        )


def send_summary(ses, summary, branch, bucket, recipients, efrom):
    response = ses.send_email(
        Source='kyle@dataskeptic.com',
        Destination={'ToAddresses': recipients},
        Message={
            'Subject': {
                'Data': 'Deploying ' + branch + ' to ' + bucket
            },
            'Body': {
                'Text': {
                    'Data': json.dumps(summary)
                }
            }
        },
        ReplyToAddresses=efrom
    )

def clean_up(dest):
    shutil.rmtree(dest)


def replacement(match):
    fn = match.groups()[0]
    if os.path.isfile(fn):
        return 'src="data:%s;base64,%s"' % (mimetypes.guess_type(fn)[0], base64.b64encode(open(fn, 'rb').read()))
    return match.group()


def get_r_images(title, fname, bucketpath, c):
    cx = c
    fname = fname[0:len(fname) - len(".html")]
    soup = bs4.BeautifulSoup(c, "lxml")
    imgtags = soup.find_all('img')
    imgs = []
    j = 0
    for i, tag in enumerate(imgtags):
        tpl = "<img src='{src}' class='r-plot' alt='{alt}' title='{title}' />"
        oclass = tag.get('class')
        if oclass is not None:
            if type(oclass) == list:
                oclass = oclass[0]
            if oclass == 'plot':
                osrc = tag.get('src')
                src = bucketpath + fname + "_" + str(i) + ".png"
                alt = title + " image #" + str(i)
                newtag = tpl.format(src=src, alt=alt, title=alt)
                s = str(tag)
                j = cx.lower().find("<img", j)
                cx = cx[0:j] + newtag + cx[j+len(s)+1:]
                j = j + len(s) + 1
                imgs.append({"src": osrc, "dest": src})
    return cx, imgs


def imgs_to_s3(buck, imgs):
    for img in imgs:
        dest = img['dest']
        s3key = dest[len("http://s3.amazonaws.com/dataskeptic.com/"):]
        src = img['src']
        logger.debug("Pushing {src} to {key}".format(src=src, key=s3key))
        res = buck.put_object(Key=s3key, Body=open(src, 'rb'))




def render_latest_for_env(s3client, env, repo, table):    
    ignore = ['/README.md']
    branch = env['branch']
    bucket = env['bucket']
    print("Running for " + branch)
    dest = '/tmp/' + str(uuid.uuid1()) + '/'
    repo_root = dest + 'blog-' + branch
    os.makedirs(dest)
    filename = get_filename(repo, branch)
    if not(os.path.exists(filename)):
        print("Didn't find " + filename)
        download(repo, branch, dest, filename)
    x = unzip(filename, dest)
    if clean:
        os.remove(filename)
    # TODO: Check that no router paths match blog folders, /blog approx match goes to /blog/ml/2016/blah
    src_dict = get_src_dict(repo_root, filename)
    content_dict = get_content_dict(table)
    plan = new_content_render_plan(repo_root, bucket, src_dict, content_dict, ignore)
    summary = execute_plan(plan, s3, s3client, bucket, table, branch)
    if clean:
        if os.path.exists(filename):
            os.remove(filename)
        clean_up(dest)


def knitr_img_handling(s3, title, absfile, contents, bucket, fname):
    i = absfile.rfind('/')
    buck = s3.Bucket(bucket)
    bucketpath = 'http://s3.amazonaws.com/' + bucket + '/' + absfile[0:i+1] + 'src-' + fname + '/'
    c2, imgs = get_r_images(title, fname, bucketpath, contents)
    imgs_to_s3(buck, imgs)
    if os.path.exists(fname + '.html'):
        os.remove(fname + '.html')
    for img in imgs:
        os.remove(img['src'])
    return c2


def render_one(table, s3, s3client, absfile, bucket, env):
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
    ext = uri[uri.rfind('.'):]
    parser = parsers[ext]
    fname = os.path.basename(absfile)
    path = absfile[0:len(absfile) - len(fname)]
    p = fname.rfind('.')
    d = path + "src-" + fname[0:p]
    srcfiles = []
    if os.path.isdir(d):
        srcfiles = os.listdir(d)
    contents = parser(absfile)
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
    isNew = not(post_already_exists(table, item_metadata, s3client, bucket, s3key))
    render_item(s3, s3client, bucket, table, srcfiles, item_metadata, env, isNew)
    return True





if __name__ == "__main__":
    logger.debug("Starting")
    try:
        accessKey = os.environ['accessKey']
        secretKey = os.environ['secretKey']
        logger.debug("keys found in environment")
    except KeyError:
        accessKey = None
        secretKey = None
    if accessKey == None:
        config = json.load(open('config.json', 'r'))
        accessKey = config['accessKey']
        secretKey = config['secretKey']
    region = "us-east-1"
    s3 = boto3.resource('s3', aws_access_key_id=accessKey, aws_secret_access_key=secretKey, region_name=region)
    s3client = boto3.client('s3', aws_access_key_id=accessKey, aws_secret_access_key=secretKey, region_name=region)
    dynamodb = boto3.resource('dynamodb', aws_access_key_id=accessKey, aws_secret_access_key=secretKey, region_name=region)
    tblName = 'blog'
    table = dynamodb.Table(tblName)
    #
    ran_locally = False
    if len(sys.argv) > 1:
        if sys.argv[1] == 'render':
            absfile = sys.argv[2]
            if len(sys.argv) > 3:
                env = sys.argv[3]
            else:
                env = 'dev'
            if env == 'dev':
                bucket = 'dev.dataskeptic.com'
            else:
                bucket = 'dataskeptic.com'
            logger.debug("Rendering locally")
            ran_locally = render_one(table, s3, s3client, absfile, bucket, env)
    #
    if not(ran_locally):
        repo = 'https://github.com/data-skeptic/blog'
        emails = ['kylepolich@gmail.com']
        clean = True
        for item in sys.argv:
            if item == '--noclean':
                clean = False
                print("No cleaning")
        #
        environments = [
            {'branch': 'dev', 'bucket': 'dev.dataskeptic.com'}
            ,{'branch': 'master', 'bucket': 'dataskeptic.com'}
        ]
        for env in environments:
            render_latest_for_env(s3client, env, repo, table)





