import os
import json
import boto3
from botocore.vendored import requests
import markdown

def lambda_handler(event, context):
    accessKey = os.getenv("accessKey")
    secretKey = os.getenv("secretKey")
    s3 = boto3.resource('s3', aws_access_key_id=accessKey, aws_secret_access_key=secretKey)
    sender = event['sender']
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
        'body': json.dumps(resp)
    }


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
    bucket_name = "dataskeptic.com"
    if doc_type in ['png', 'jpg', 'jpeg', 'gif']:
        obj = s3.Object(bucket_name, s3key)
        obj.put(Body=r.content)
    elif doc_type == 'md':
        contents = r.content.decode('utf-8')
        html = markdown.markdown(contents, extensions=['markdown.extensions.tables'])
      obj = s3.Object(bucket_name, s3key[:-3] + '.html')
      obj.put(Body=html)
    else:
        raise Exception("Unknown filetype: " + doc_type)


def remove(s3, s3key):
    pass