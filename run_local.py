import boto3
import json
import pandas as pd

from chalicelib import blog, dao, podcast, renderer

s3 = boto3.resource('s3')

repo = "kylepolich/bot-service-wiki"
branch = "/master"
filepath = "actions/numeric/multiply.md"
bucket_name = "dataskeptic.com"
db_s3_key = "posts.db.parquet"

database = pd.read_parquet("temp.parquet")

#dao.update_database(s3, bucket_name, db_s3_key, database)


#renderer.render(s3, repo, branch, filepath)

if False:
	repo = "data-skeptic/blog"
	url = "/blog/episodes/2015/tf-idf"
	attribute = "foo"
	value = "bar"
	result = renderer.get_attribute(s3, bucket_name, db_s3_key, url, attribute)
	print(result)
	result = renderer.update_attributes(s3, bucket_name, db_s3_key, url, attribute, value)
	result = renderer.get_attribute(s3, bucket_name, db_s3_key, url, attribute)
	print(result)
	result = renderer.update_attributes(s3, bucket_name, db_s3_key, url, attribute, None)
	result = renderer.get_attribute(s3, bucket_name, db_s3_key, url, attribute)
	print(result)

url = 'http://dataskeptic.libsyn.com/rss'
print('fetching {url}'.format(url=url))
bucket_name = 'dataskeptic.com'
db_s3_key = 'posts.db.parquet'
#database = dao.get_database(s3, bucket_name, db_s3_key)    
podcast.update_podcast_rss(database, s3, bucket_name, db_s3_key, url)

#! June

# TODO: trigger ad slicing container in AWS Batch
