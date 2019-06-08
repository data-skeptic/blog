import boto3
from botocore.vendored import requests
from chalice import Chalice, Rate
import json
import os
from urllib.parse import unquote

from chalicelib import blog, dao, podcast, renderer

app = Chalice(app_name="blog")

access = os.getenv('ACCESS_KEY')
secret = os.getenv('SECRET_KEY')
s3 = boto3.resource('s3', aws_access_key_id=access, aws_secret_access_key=secret)


@app.route("/blog/posts", methods=['GET'])
def blog_posts():
    params = app.current_request.query_params
    print(params)
    blogs = blog.get_blogs()
    if params is not None and 'id' in params:
        url = params['id']
        print(url)
        # TODO: prefix matching
        return blogs[url]
    else:
        return blogs


@app.route("/blog/deploy", methods=['POST'], content_types=['application/x-www-form-urlencoded'])
def blog_deploy():
    prefix = 'payload='
    payloadstr = app.current_request.raw_body.decode('utf-8')
    payload = unquote(payloadstr[len(prefix):])
    event = json.loads(payload)
    return blog.handle_update(github_webhook_event)


@app.route("/blog/posts/update", methods=['POST'])
def blog_posts_update():
    o = app.current_request.json_body
    url = o['url']
    attribute = o['attribute']
    value = o['value']
    return blog.update_attributes(url, attribute, value)


@app.route("/blog/podcast/update", methods=['POST'])
def update_podcast():
    url = 'http://dataskeptic.libsyn.com/rss'
    bucket_name = 'dataskeptic.com'
    db_s3_key = 'posts.db.parquet'
    database = dao.get_database(s3, bucket_name, db_s3_key)    
    print('fetching {url}'.format(url=url))
    podcast.update_podcast_rss(database, s3, bucket_name, db_s3_key, url)


@app.schedule(Rate(1, unit=Rate.MINUTES))
def scheduled(event):
    url = 'http://dataskeptic.libsyn.com/rss'
    print('fetching {url}'.format(url=url))
    print(event)
    bucket_name = 'dataskeptic.com'
    db_s3_key = 'posts.db.parquet'
    database = dao.get_database(s3, bucket_name, db_s3_key)    
    podcast.update_podcast_rss(database, s3, bucket_name, db_s3_key, url)

"""
@app.on_s3_event(bucket='dataskeptic.com', events=['s3:ObjectCreated:*'])
def handle_image_upload(event):
    print(event)
    raise Exception("Not implemented yet!")


TODO: remember how to use SQS in Chalice
@app.on_sqs_message(queue='myqueue')
def handler(event):
    app.log.info("Event: %s", event.to_dict())
    for record in event:
        app.log.info("Message body: %s", record.body)
"""

