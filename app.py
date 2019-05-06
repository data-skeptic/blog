import os
import json
import boto3
import string
from botocore.vendored import requests
import bs4 as soup
import markdown
from urllib.parse import unquote

from chalice import Chalice, Rate

app = Chalice(app_name="blog")

@app.route("/blog/deploy", methods=['POST'], content_types=['application/x-www-form-urlencoded'])
def index():
    prefix = 'payload='
    payloadstr = app.current_request.raw_body.decode('utf-8')
    payload = unquote(payloadstr[len(prefix):])
    event = json.loads(payload)
    s3 = boto3.resource('s3')
    sender = {'login': event['sender']}
    login = sender['login']
    repo = event['repository']['full_name']
    ref = event['ref']
    branch = ref[ref.rfind('/'):]
    commits = event['commits']
    resp = { "commits": 0, "login": login, "repo": repo }
    for filepath in commits:
        process_commit(s3, repo, branch, filepath)
        resp['commits'] += 1
    return {
        'statusCode': 200,
        'body': resp
    }


@app.schedule(Rate(1, unit=Rate.HOURS))
def scheduled(event):
	print(event.to_dict())
	pass


#@app.on_s3_event(bucket='mybucket-name',
#                 events=['s3:ObjectCreated:*'])


def process_commit(s3, repo, branch, commit):
    for filepath in commit['added']:
        render(s3, repo, branch, filepath)
    for filepath in commit['removed']:
        remove(s3, filepath)
    for filepath in commit['modified']:
        render(s3, repo, branch, filepath)


def get_type(s3key):
    i = s3key.rfind('.')
    ext = s3key[i+1:].lower()
    if ext in ['md']:
        return ext
    return None


def render(s3, repo, branch, filepath):
    t = "https://raw.githubusercontent.com/{repo}{branch}/{filepath}"
    url = t.format(repo=repo, branch=branch, filepath=filepath)
    r = requests.get(url)
    doc_type  = get_type(filepath)
    if doc_type is None:
        return
    s3key = "{branch}/{filepath}".format(branch=branch[1:], filepath=filepath)
    save(s3, doc_type, s3key, r.content)
    s3key = "{filepath}".format(branch=branch[1:], filepath=filepath)
    save(s3, doc_type, s3key, r.content, True)


def save(s3, doc_type, s3key, content, legacy=False):
    bucket_name = "dataskeptic.com"
    if doc_type in ['png', 'jpg', 'jpeg', 'gif']:
        obj = s3.Object(bucket_name, s3key)
        obj.put(Body=content)
    elif doc_type == 'md':
        contents = content.decode('utf-8')
        html = markdown.markdown(contents, extensions=['markdown.extensions.tables'])
        key = s3key[:-3] + '.html'
        obj = s3.Object(bucket_name, key)
        exists = False
        bucket = s3.Bucket(bucket_name)
        objs = list(bucket.objects.filter(Prefix=s3key))
        if len(objs) > 0 and objs[0].key == key:
            exists = True
        obj.put(Body=html)
        if legacy and not(exists):
            title = get_title(s3key, contents)
            desc = get_desc(contents)
            update_database(title, desc, s3key)
    else:
        raise Exception("Unknown filetype: " + doc_type)


def get_desc(contents):
    """Accepts a string in html format; returns a description"""
    lcontents = contents.lower()
    i = lcontents.find('<p>')
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


def update_database(title, desc, s3key):
    blog_id = -1
    author = 'Kyle'
    prettyname = get_pretty_name(s3key, title)
    data = {
        "blog_id": blog_id,
        "details": {
            'title': fix_string_for_db(title),
            'author': fix_string_for_db(author),
            'desc': fix_string_for_db(desc),
            'prettyname': prettyname,
            's3key': s3key
        }
    }
    base_url = "https://4sevcujref.execute-api.us-east-1.amazonaws.com/prod"
    url = base_url + "/blog/upsert"
    o = json.dumps(data)
    print(o)
    r = requests.post(url, o)
    s = r.content.decode('utf-8')
    o = json.loads(s)
    if o['success'] == 1:
        return o
    else:
        None


def remove(s3, s3key):
    bucket_name = "dataskeptic.com"
    if doc_type in ['png', 'jpg', 'jpeg', 'gif']:
        obj = s3.Object(bucket_name, s3key)
        obj.delete()
    elif doc_type == 'md':
        obj = s3.Object(bucket_name, s3key[:-3] + '.html')
        obj.delete()
    else:
        raise Exception("Unknown filetype: " + doc_type)
