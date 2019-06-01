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


"""
TODO: remember how to use SQS in Chalice
@app.on_sqs_message(queue='myqueue')
def handler(event):
    app.log.info("Event: %s", event.to_dict())
    for record in event:
        app.log.info("Message body: %s", record.body)
"""


@app.route("/blog/update", methods=['POST'])
def blog_attribute_add():
    o = app.current_request.json_body
    key = o['url']
    attribute = o['attribute']
    value = o['value']
    s3 = boto3.resource('s3', aws_access_key_id=access, aws_secret_access_key=secret)
    bucket_name = 'dataskeptic.com'
    db_s3_key = 'posts.db.parquet'
    database = dao.get_database(s3, bucket_name, db_s3_key)
    if key not in database:
        raise Exception(f"No record of {key}")
    old_record = database[key]
    new_record = json.loads(json.dumps(old_record))
    new_record[attribute] = value
    dao.update_database(s3, bucket_name, db_s3_key, database)
    return {"old_record": old_record, "new_record": new_record}



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


@app.on_s3_event(bucket='dataskeptic.com', events=['s3:ObjectCreated:*'])
def handle_image_upload(event):
    print(event)
    raise Exception("Not implemented yet!")


def add_metadata(event, methods=['POST']):
    print(event)
    ! June
    # TODO: insert into parquet file
    raise Exception("Not implemented yet!")


def process_commit(database, s3, bucket_name, repo, branch, commit):
    author = commit['author']['email']
    for filepath in commit['added']:
        render.render_one(database, s3, bucket_name, repo, branch, filepath, author)
        # TODO: add to elastic search
        #elastic.add()

    for filepath in commit['removed']:
        doc_type = renderer.get_type(filepath)
        renderer.remove(s3, bucket_name, doc_type, filepath)
        # TODO: remove from elasic search
        # TODO: remove from parquet database
    for filepath in commit['modified']:
        renderer.render_one(database, s3, bucket_name, repo, branch, filepath, author)

