import json
import boto3
import wget




#   Find changes on github master/dev branch
#   Check that no router paths match blog folders, /blog approx match goes to /blog/ml/2016/blah
#   Get last rendered from Dynamo (file, timestamp, branch)
#   Render md/ipynb/Rhtml
#   Blog.js is a wrapper that puts headerless stuff in the middle (query for only release date in past)
#   Copy to S3 of dataskeptic.com
#   Add recording to Dynamo DB
# X Send alert
#   UI to update dynamo and add tags, release date


# src, first added, release date, ???


import boto3

client = boto3.client('dynamodb')

tblName = 'blog'

try:
    client.update_item(TableName=tblName, Key={'hash_key':{'N':'value'}}, AttributeUpdates={"some_key":{"Action":"PUT","Value":{"N":'value'}}}) 
except Exception, e:
    print (e)





import json
import decimal

dynamodb = boto3.resource('dynamodb', region_name='us-east-1', endpoint_url="http://localhost:8000")

table = dynamodb.Table('Movies')

with open("moviedata.json") as json_file:
    movies = json.load(json_file, parse_float = decimal.Decimal)
    for movie in movies:
        year = int(movie['year'])
        title = movie['title']
        info = movie['info']

        print("Adding movie:", year, title)

        table.put_item(
           Item={
               'year': year,
               'title': title,
               'info': info,
            }
        )













