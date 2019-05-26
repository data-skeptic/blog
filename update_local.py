import boto3
from core import podcast
from core import renderer

s3 = boto3.resource('s3')

fname = "rss.xml"
bucket_name = "dataskeptic.com"
db_s3_key = "posts.db.parquet"

database = podcast.get_database(s3, bucket_name, db_s3_key)

repo = "data-skeptic/blog"
branch = "/master"
filepath = "episodes/2019/simultaneous-translation.md"
author = "kyle@dataskeptic.com"

#renderer.render(s3, repo, branch, filepath, author)


updated = podcast.update_podcast_from_file(s3, database, fname)
print(updated)
if updated:
    print("Podcast updates made")
    podcast.update_database(s3, bucket_name, db_s3_key, database)
