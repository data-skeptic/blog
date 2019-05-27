from botocore.vendored import requests
import bs4 as soup
import re
import string

from . import dao
from .formats import markdown, svg

def render(s3, bucket_name, repo, branch, filepath):
    t = "https://raw.githubusercontent.com/{repo}{branch}/{filepath}"
    url = t.format(repo=repo, branch=branch, filepath=filepath)
    r = requests.get(url)
    if r.status_code != 200:
        raise Exception('TODO: handle Non-200 response retrieving content')
    doc_type  = get_type(filepath)
    if doc_type is None:
        return
    s3key = "{filepath}".format(branch=branch[1:], filepath=filepath)
    # TODO: refactor this upstream
    if repo == "kylepolich/bot-service-wiki":
        s3key = "wiki/" + s3key
        renderedContent = save(s3, doc_type, bucket_name, 'wiki/latex', s3key, r.content)
    elif repo == "data-skeptic/blog":
        s3key = "blog/" + s3key
        renderedContent = save(s3, doc_type, bucket_name, 'latex', s3key, r.content)
    else:
        raise Exception("Unknown repo: " + repo)
    is_new = renderedContent != None
    return { "is_new": is_new, "s3key": s3key, "content": renderedContent }


def render_one(database, s3, bucket_name, repo, branch, filepath, author):
    updated = render(s3, bucket_name, repo, branch, filepath)
    if updated['is_new']:
        s3key = updated['s3key']
        content = updated['content']
        record = generate_metadata(s3key, content, author)
        database[record['url']] = record
        db_s3_key = "posts.db.parquet"
        dao.update_database(s3, bucket_name, db_s3_key, database)


def generate_metadata(s3key, content, author):
    title = get_title(s3key, content)
    desc = get_desc(content)
    url = get_pretty_name(s3key, title)
    data = {
        'title': fix_string_for_db(title),
        'author': fix_string_for_db(author),
        'description': fix_string_for_db(desc),
        'url': url,
        's3key': s3key
    }
    return data


def get_rendered_key_name(s3key):
    return s3key[:-3] + '.html'


def save(s3, doc_type, bucket_name, latex_prefix, s3key, content):
    """Returns true if the database should have a new row inserted"""
    if doc_type in ['png', 'jpg', 'jpeg', 'gif']:
        obj = s3.Object(bucket_name, s3key)
        obj.put(Body=content)
    elif doc_type == 'md':
        print('aa')
        content2 = svg.render(content.decode('utf-8'), s3, bucket_name, latex_prefix)
        print('bb')
        html = markdown.render(content2)
        print('cc')
        key = get_rendered_key_name(s3key)
        obj = s3.Object(bucket_name, key)
        exists = False
        bucket = s3.Bucket(bucket_name)
        print(">>>>", bucket_name, s3key)
        objs = list(bucket.objects.filter(Prefix=s3key))
        if len(objs) > 0 and objs[0].key == key:
            exists = True
        obj.put(Body=html)
        if not(exists):
            return content2
        else:
            return None
    else:
        raise Exception("Unknown filetype: " + doc_type)


def remove(s3, bucket_name, doc_type, s3key):
    if doc_type in ['png', 'jpg', 'jpeg', 'gif']:
        obj = s3.Object(bucket_name, s3key)
        obj.delete()
    elif doc_type == 'md':
        obj = s3.Object(bucket_name, s3key[:-3] + '.html')
        obj.delete()
    else:
        raise Exception("Unknown filetype: " + doc_type)


def get_type(filepath):
    i = filepath.rfind('.')
    ext = filepath[i+1:].lower()
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


