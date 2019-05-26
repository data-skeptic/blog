import boto3
from botocore.vendored import requests
from chalice import Chalice, Rate
import json
import os
from urllib.parse import unquote

from core import renderer

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
    r = requests.get(url)
    f = open(fname, 'wb')
    f.write(r.text.encode('utf-8'))
    f.close()
    with open(fname) as fd:
        xml = xmltodict.parse(fd.read())
        emap = {}
        episodes = xml['rss']['channel']['item']
        n = len(episodes)
        print(f'Number of episodes: {n}')
        for episode in episodes:
            guid = episode['guid']['#text']
            url = episode['enclosure']['@url']
            emap[guid] = url
            do it with json metadata files
            # TODO: check the rss feed for new episodes
            if found
            if not already attached to episodes
            find episode that matches
            if not found quit
            link episode


#@app.on_s3_event(bucket='mybucket-name', events=['s3:ObjectCreated:*'])
#def handle_image_upload(event):
#    TODO: resize uploaded images


def process_commit(s3, repo, branch, commit):
    for filepath in commit['added']:
        renderer.render(s3, repo, branch, filepath)
    for filepath in commit['removed']:
        renderer.remove(s3, filepath)
    for filepath in commit['modified']:
        renderer.render(s3, repo, branch, filepath)


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
