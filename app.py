import boto3
from botocore.vendored import requests
from chalice import Chalice, Rate
import json
import os
from urllib.parse import unquote

from chalicelib import blog, dao, podcast, renderer

app = Chalice(app_name="blog")


@app.route("/blog/posts", methods=['GET'], content_types=['application/x-www-form-urlencoded'])
def blog_posts():
    params = app.current_request.query_params
    if 'id' in params:
        url = params['id']
        return blog.get_blogs()[url]
    else:
        return blog.get_blogs()


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


@app.schedule(Rate(1, unit=Rate.MINUTES))
def scheduled(event):
    print(event.to_dict())
    bucket_name = 'dataskeptic.com'
    db_s3_key = 'posts.db.parquet'
    url = 'http://dataskeptic.libsyn.com/rss'
    print('fetching {url}'.format(url=url))
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

