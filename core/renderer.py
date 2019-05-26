from botocore.vendored import requests
import bs4 as soup
import re
import string

from .formats import markdown, svg

def render(s3, repo, branch, filepath, author):
    t = "https://raw.githubusercontent.com/{repo}{branch}/{filepath}"
    url = t.format(repo=repo, branch=branch, filepath=filepath)
    r = requests.get(url)
    print(r.status_code)
    if r.status_code != 200:
        raise Exception('TODO: handle Non-200 response retrieving content')
    doc_type  = get_type(filepath)
    if doc_type is None:
        return
    s3key = "{filepath}".format(branch=branch[1:], filepath=filepath)
    if repo == "kylepolich/bot-service-wiki":
        bucket_name = "dialog-creation-system"
        s3key = "wiki/" + s3key
        save(s3, doc_type, author, bucket_name, 'wiki/latex', s3key, r.content)
    elif repo == "data-skeptic/blog":
        bucket_name = "dataskeptic.com"
        s3key = "blog/" + s3key
        save(s3, doc_type, author, bucket_name, 'latex', s3key, r.content)
    else:
        raise Exception("Unknown repo: " + repo)


def save(s3, doc_type, author, bucket_name, latex_prefix, s3key, content):
    if doc_type in ['png', 'jpg', 'jpeg', 'gif']:
        obj = s3.Object(bucket_name, s3key)
        obj.put(Body=content)
    elif doc_type == 'md':
        content2 = svg.render(content.decode('utf-8'), s3, bucket_name, latex_prefix)
        html = markdown.render(content2)
        key = s3key[:-3] + '.html'
        obj = s3.Object(bucket_name, key)
        exists = False
        bucket = s3.Bucket(bucket_name)
        print(">>>>", bucket_name, s3key)
        objs = list(bucket.objects.filter(Prefix=s3key))
        if len(objs) > 0 and objs[0].key == key:
            exists = True
        obj.put(Body=html)
        if not(exists):
            update_database(s3key, content, author)
    else:
        raise Exception("Unknown filetype: " + doc_type)


def get_type(s3key):
    i = s3key.rfind('.')
    ext = s3key[i+1:].lower()
    if ext in ['md']:
        return ext
    return None


def get_desc(contents):
    """Accepts a string in html format; returns a description"""
    if type(contents) == str:
        lcontents = contents.lower()
    else:
        lcontents = contents.decode('utf-8').lower()
    i = lcontents.find("<p>")
    if i != -1:
        j = lcontents.find('</p>', i)
        desc = contents[i+3:j-4]
        desc = re.sub('<[^<]+?>', '', desc)
    else:
        desc = ''
    if len(desc) > 0:
        if desc[-1] == '<':
            desc = desc[:-1]
    return desc


def get_pretty_name(absfilename, title):
    """Given source file and title, select SEO friendly name"""
    i = absfilename.rfind('/')
    if absfilename[i+1:].lower() == 'readme.htm':
        return '/' + absfilename[0:i+1]
    pn = title.lower().replace(' ', '-')
    valid_chars = "-_.() %s%s" % (string.ascii_letters, string.digits)
    pn2 = ''.join(c for c in pn if c in valid_chars)
    i = absfilename.rfind('/')
    return '/' + absfilename[0:i] + '/' + pn2


def fix_string_for_db(s):
    return s.replace(u"\u2018", "'").replace("’", "'").replace("'", "\\'")


def get_title(absfilename, contents):
    """Accepts a filename AND it's contents; returns a title"""
    lcontents = contents.lower()
    c = 1
    b = soup.BeautifulSoup(contents, "lxml")
    while c < 6:
        tag = b.find('h' + str(c))
        if tag != None:
            return tag.text.replace('&#182;', '')
        c += 1
    i = absfilename.rfind('/')
    j = absfilename.rfind('.')
    fname = absfilename[i+1:j]
    fname = fname.replace('-', ' ').replace('_', ' ')
    fname = fname.title()
    return fname


def generate_metadata(s3key, contents, author):
    title = get_title(s3key, contents)
    desc = get_desc(contents)
    url = get_pretty_name(s3key, title)
    data = {
        'title': fix_string_for_db(title),
        'author': fix_string_for_db(author),
        'description': fix_string_for_db(desc),
        'url': url,
        's3key': s3key
    }
    return data


