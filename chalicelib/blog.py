import boto3
import json
import os

from . import dao, elastic, renderer

access = os.getenv('ACCESS_KEY')
secret = os.getenv('SECRET_KEY')
s3 = boto3.resource('s3', aws_access_key_id=access, aws_secret_access_key=secret)
sns = boto3.client('sns', aws_access_key_id=access, aws_secret_access_key=secret, region_name='us-east-2')
#sns.setRegion(Region.getRegion(Regions.US_WEST_2));

arn = 'arn:aws:sns:us-east-2:085318171245:blog-updates-topic'

db_s3_key = 'posts.db.parquet'

def get_blogs():
    bucket_name = 'dataskeptic.com'
    database = dao.get_database(s3, bucket_name, db_s3_key)    
    return database


def handle_update(github_webhook_event):
    sender = {'login': github_webhook_event['sender']}
    login = sender['login']
    repo = github_webhook_event['repository']['full_name']
    if repo == 'data-skeptic/blog':
        bucket_name = "dataskeptic.com"
    elif repo == 'kylepolich/bot-service-wiki':
        bucket_name = 'dialog'
    ref = github_webhook_event['ref']
    branch = ref[ref.rfind('/'):]
    commits = github_webhook_event['commits']
    resp = { "commits": 0, "login": login, "repo": repo }
    database = dao.get_database(s3, bucket_name, db_s3_key)
    for filepath in commits:
        process_commit(database, s3, bucket_name, repo, branch, filepath)
        resp['commits'] += 1
    return {
        'statusCode': 200,
        'body': resp
    }


def publish():
    message = {"foo": "bar"}
    response = sns.publish(
        TargetArn=arn,
        Subject='huh?',
        Message=json.dumps({'default': json.dumps(message)}),
        MessageStructure='json'
    )
    if response['HTTPStatusCode'] != 200:
        print(response)
        raise Exception('Could not publish to sns')


def process_commit(database, s3, bucket_name, repo, branch, commit):
    author = commit['author']['email']
    for filepath in commit['added']:
        render.render_one(database, s3, bucket_name, repo, branch, filepath, author)
        publish()
    for filepath in commit['removed']:
        doc_type = renderer.get_type(filepath)
        renderer.remove(s3, bucket_name, doc_type, filepath)
        dao.remove(filepath)
    for filepath in commit['modified']:
        renderer.render_one(database, s3, bucket_name, repo, branch, filepath, author)


def update_attributes(url, attribute, value):
    bucket_name = 'dataskeptic.com'
    database = dao.get_database(s3, bucket_name, db_s3_key)
    if url not in database:
        raise Exception("No record of {url}".format(url=url))
    old_record = database[url]
    new_record = json.loads(json.dumps(old_record))
    if value is None and attribute in new_record:
        del new_record[attribute]
    else:
        new_record[attribute] = value
    database[url] = new_record
    dao.update_database(s3, bucket_name, db_s3_key, database)
    # TODO: add to elastic search
    #blog_content = 
    #elastic.add(database, url, blog_content)
    return {"old_record": old_record, "new_record": new_record}


def get_attribute(s3, bucket_name, db_s3_key, url, attribute):
    database = dao.get_database(s3, bucket_name, db_s3_key)
    if url not in database:
        raise Exception("No record of {url}".format(url=url))
    return database[url]


