import os
import json
import boto3
from botocore.vendored import requests
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
        remove(s3, repo, branch, filepath)
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
    save(s3, doc_type, s3key, r.content)


def save(s3, doc_type, s3key, content):
    bucket_name = "dataskeptic.com"
    if doc_type in ['png', 'jpg', 'jpeg', 'gif']:
        obj = s3.Object(bucket_name, s3key)
        obj.put(Body=content)
    elif doc_type == 'md':
        contents = content.decode('utf-8')
        html = markdown.markdown(contents, extensions=['markdown.extensions.tables'])
        key = s3key[:-3] + '.html'
        print(key)
        obj = s3.Object(bucket_name, key)
        obj.put(Body=html)
    else:
        raise Exception("Unknown filetype: " + doc_type)


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
