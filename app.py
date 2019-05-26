import boto3
from botocore.vendored import requests
from chalice import Chalice, Rate
import json
import os
from urllib.parse import unquote

from core import renderer, podcast

app = Chalice(app_name="blog")

@app.route("/blog/deploy", methods=['POST'], content_types=['application/x-www-form-urlencoded'])
def index():
    prefix = 'payload='
    payloadstr = app.current_request.raw_body.decode('utf-8')
    payload = unquote(payloadstr[len(prefix):])
    event = json.loads(payload)
    access = os.getenv('ACCESS_KEY')
    secret = os.getenv('SECRET_KEY')
    s3 = boto3.resource('s3', aws_access_key_id=access, aws_secret_access_key=secret)
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


@app.schedule(Rate(1, unit=Rate.MINUTES))
def scheduled(event):
	print(event.to_dict())
    url = 'http://dataskeptic.libsyn.com/rss'
    print(f'fetching {url}')
    podcast.update_podcast_rss(url)


#@app.on_s3_event(bucket='mybucket-name', events=['s3:ObjectCreated:*'])
#def handle_image_upload(event):
#    TODO: resize uploaded images


def process_commit(s3, repo, branch, commit):
    author = commit['author']['email']
    for filepath in commit['added']:
        renderer.render(s3, repo, branch, filepath, author)
    for filepath in commit['removed']:
        renderer.remove(s3, filepath)
    for filepath in commit['modified']:
        renderer.render(s3, repo, branch, filepath, author)


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
