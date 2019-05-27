    updated_contents = knitr_img_handling(s3, title, absfile, updated_contents, bucket, fname)

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
