import boto3
from botocore.vendored import requests
from chalice import Chalice, Rate
import json
import os
from urllib.parse import unquote

from core import dao, podcast, renderer

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
    if repo == 'data-skeptic/blog':
        bucket_name = "dataskeptic.com"
    elif repo == 'kylepolich/bot-service-wiki':
        bucket_name = 'dialog'
    ref = event['ref']
    branch = ref[ref.rfind('/'):]
    commits = event['commits']
    resp = { "commits": 0, "login": login, "repo": repo }
    db_s3_key = "posts.db.parquet"
    database = dao.get_database(s3, bucket_name, db_s3_key)
    for filepath in commits:
        process_commit(database, s3, bucket_name, repo, branch, filepath)
        resp['commits'] += 1
    return {
        'statusCode': 200,
        'body': resp
    }


@app.schedule(Rate(1, unit=Rate.MINUTES))
def scheduled(event):
	print(event.to_dict())
    podcast.update_podcast_rss(url)
    s3 = boto3.resource('s3', aws_access_key_id=access, aws_secret_access_key=secret)
    bucket_name = 'dataskeptic.com'
    db_s3_key = 'posts.db.parquet'
    url = 'http://dataskeptic.libsyn.com/rss'
    print(f'fetching {url}')
    database = dao.get_database(s3, bucket_name, db_s3_key)    
    podcast.update_podcast_rss(database, s3, bucket_name, db_s3_key, url)


#@app.on_s3_event(bucket='mybucket-name', events=['s3:ObjectCreated:*'])
#def handle_image_upload(event):
#    TODO: resize uploaded images


def process_commit(database, s3, bucket_name, repo, branch, commit):
    author = commit['author']['email']
    for filepath in commit['added']:
        render.render_one(database, s3, bucket_name, repo, branch, filepath, author)
    for filepath in commit['removed']:
        doc_type = renderer.get_type(filepath)
        renderer.remove(s3, bucket_name, doc_type, filepath)
        # TODO: remove from elasic search
        # TODO: remove from parquet database
    for filepath in commit['modified']:
        renderer.render_one(database, s3, bucket_name, repo, branch, filepath, author)

