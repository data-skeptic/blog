import boto3
from core import renderer

s3 = boto3.resource('s3')

repo = "kylepolich/bot-service-wiki"
branch = "/master"
filepath = "actions/numeric/multiply.md"

#renderer.render(s3, repo, branch, filepath)

bucket_name = "dataskeptic.com"
repo = "data-skeptic/blog"
url = "/blog/episodes/2015/tf-idf"
attribute = "foo"
value = "bar"
db_s3_key = "posts.db.parquet"

result = renderer.get_attribute(s3, bucket_name, db_s3_key, url, attribute)
print(result)
result = renderer.update_attributes(s3, bucket_name, db_s3_key, url, attribute, value)
result = renderer.get_attribute(s3, bucket_name, db_s3_key, url, attribute)
print(result)
result = renderer.update_attributes(s3, bucket_name, db_s3_key, url, attribute, None)
result = renderer.get_attribute(s3, bucket_name, db_s3_key, url, attribute)
print(result)

! June

# TODO: trigger ad slicing container in AWS Batch
