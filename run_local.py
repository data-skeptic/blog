import boto3
from core import renderer

s3 = boto3.resource('s3')

repo = "kylepolich/bot-service-wiki"
branch = "/master"
filepath = "actions/numeric/multiply.md"

renderer.render(s3, repo, branch, filepath)
