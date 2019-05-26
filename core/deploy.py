
# DONE

* Render markdown and save to s3
* Call dataskeptic api to insert into database

# TODO:

* elastic search update
* delete
* svg handling
* jupyter image to image file
* Rmd
* Schedule regular check of rss feed

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









    logger.debug('Now update for knitr images')
    updated_contents = knitr_img_handling(s3, title, absfile, updated_contents, bucket, fname)
    return updated_contents






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

def render_blog(base_url, s3, item_metadata, blog_id):
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
    fake_handle = io.BytesIO(contents.encode('utf-8'))
    res = s3.Bucket(bucket).put_object(Key=s3key, Body=fake_handle)
    x = os.path.basename(s3key)
    a = s3key.rfind('/')
    b = s3key.rfind('.')
    dname = 'src-' + s3key[a+1:b]
    keypath = s3key[0:len(s3key)-len(x)] + dname + '/'
    for src in srcfiles:
        s3key2 = keypath + os.path.basename(src)
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

def render_inner(s3, contents, branch):
    bucket    = "dataskeptic.com"
    base_url  = "https://4sevcujref.execute-api.us-east-1.amazonaws.com/" + branch
    render_inner2(contents)

def render_one(base_url, s3, absfile, bucket, env):
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
    render_inner2(c)

def render_inner2(c):
    chash = hashlib.md5(c).hexdigest()
    a = len(bucket)+1
    i = uri.rfind('.')
    s3key = uri[a:i] + '.htm'
    parser = parsers[ext]
    contents = parser(absfile)
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
    blog_id = post_already_exists(base_url, s3key)!
    render_item(base_url, s3, bucket, srcfiles, item_metadata, env, blog_id)


def decode_base64(data):
    """Decode base64, padding being optional.

    :param data: Base64 data as an ASCII byte string
    :returns: The decoded byte string.

    """
    missing_padding = len(data) % 4
    if missing_padding != 0:
        data += b'='* (4 - missing_padding)
    return base64.decodestring(data)
