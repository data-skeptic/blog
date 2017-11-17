import os
import json
import pandas as pd
import numpy as np
import math
import requests
import markdown
import httplib, urllib, base64
import time

r = requests.get('http://dataskeptic.com/api/blog?limit=100')

oblogs = json.loads(r.content)

blogs = []
start = pd.to_datetime('2017-01-01')
for blog in oblogs:
    blog['publish_date'] = pd.to_datetime(blog['publish_date'])
    if blog['publish_date'] > start:
        blogs.append(blog)

content = {}

for blog in blogs:
    renderedPath = blog['rendered']
    url = 'https://s3.amazonaws.com/dataskeptic.com/' + renderedPath
    if not(content.has_key(url)):
        content[url] = requests.get(url).content

# This is how I am storing my keys for my Cognitive Services tests, just set your value for `key`
f = open('azure.keys', 'r')
keys = json.loads(f.read())
f.close()

key = keys['text-analytics']
headers = {'Content-Type': 'application/json', 'Ocp-Apim-Subscription-Key': key}

params = urllib.urlencode({})

results = []
conn = httplib.HTTPSConnection('westus.api.cognitive.microsoft.com')
i = 0
for k in content.keys():
    v = content[k]
    m = 10240 # The API imposes a limit
    if len(v) > m: 
        v = v[0:m]
    loop = True
    while loop:
        loop = False
        doc = {"language": "en", "id": str(i), "text": v}
        body = {"documents": [doc]}
        conn.request("POST", "/text/analytics/v2.0/keyPhrases?%s" % params, json.dumps(body), headers)
        response = conn.getresponse()
        data = json.loads(response.read())
        conn.close()
        if len(data['errors']) == 0:
            results.append(data)
        else:
            print 'Error, retrying', i
            print data['errors']
            print len(doc['text'])
            loop = True
        time.sleep(1)
        m = int(.9 * len(doc))
        v = v[0:m]
    i += 1

txt = ''
for blog in blogs:
    title = blog['title']
    uri = blog['uri']
    desc = blog['desc']
    renderedPath = blog['rendered']
    url = 'https://s3.amazonaws.com/dataskeptic.com/' + renderedPath
    phrases = results[0]['documents'][0]['keyPhrases']
    txt += "### " + title + "\n"
    txt += "*Blog post*: [" + uri + "](" + uri + ")\n\n"
    txt += "*Phrases*: " + ', '.join(phrases) + "\n\n"

f = open('azure-text-analytics-results.htm', 'w')
html = markdown.markdown(txt)
f.write(html)
f.close()