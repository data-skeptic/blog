import json
import boto3
import os
import wget
import uuid
import zipfile
import markdown
import shutil
from cStringIO import StringIO
import nbformat
from nbconvert import HTMLExporter
import hashlib
import datetime
import rpy2.robjects as robjects

def unzip(source_filename, dest_dir):
	zf = zipfile.ZipFile(source_filename)
	zf.extractall(dest)

def download(repo, branch, dest):
    src = repo + '/archive/' + branch +'.zip'
    if not(os.path.isdir(dest)):
        os.mkdir(dest)
    r1 = wget.download(src)
    unzip(r1, dest)
    os.remove(r1)
    filename = repo[repo.rfind('/')+1:] + '-' + branch 
    return filename

def get_src_dict(repo_root, parent, parsers):
    d = {}
    suffixes = parsers.keys()
    rootdir = repo_root.rstrip(os.sep)
    start = rootdir.rfind(os.sep) + 1
    for path, dirs, files in os.walk(rootdir):
        for file in files:
            i = file.rfind('.')
            if i != -1:
                ext = file[i:]
                if ext in suffixes:
                    d[path + '/' + file] = True
    return d

def get_content_dict(table):
	response = table.scan()
	items = response['Items']
	d = {}
	for item in items:
		uri = item['uri']
		d[uri] = item
	return d

def new_content_render_plan(repo_root, src_dict, content_dict, parsers, ignore):
	plan = []
	s = len(repo_root)
	srcs = src_dict.keys()
	oldHash = None
	for src in srcs:
		uri = src[s:]
		if not(uri in ignore):
			isNew = True
			if content_dict.has_key(uri):
				isNew = False
				oldHash = content_dict[uri]['c_hash']
			ext = uri[uri.rfind('.'):]
			parser = parsers[ext]
			plan.append({"absfile": src, "uri": uri, "parser": parser, "isNew": isNew, "oldHash": oldHash})
	return plan

def execute_plan(plan, s3, bucket, table):
	summary = []
	now = datetime.datetime.now()
	n = now.strftime('%Y-%m-%d')
	for item in plan:
		parser = item['parser']
		absfile = item['absfile']
		uri = item['uri']
		f = open(absfile, 'r')
		c = f.read()
		f.close()
		m = hashlib.md5()
		m.update(c)
		hash = m.hexdigest()
		render = True
		if not(item['isNew']):
			if item['oldHash'] == hash:
				render = False
			else:
				render = True
		if render:
			contents = parser(absfile)
			fake_handle = StringIO(contents.encode('utf-8'))
			i = uri.rfind('.')
			ext = uri[i:]
			s3key = uri[:i] + '.htm'
			if s3key[0]=='/':
				s3key = s3key[1:]
			print('Deploying to: ' + bucket + s3key)
			res = s3.Bucket(bucket).put_object(Key=s3key, Body=fake_handle)
			if item['isNew']:
				response = table.put_item(
					Item={
						'uri': uri,
						'ext': ext,
						'last_rendered': n,
						'c_hash': hash,
						'date_discovered': n
					}
				)
			else:
				response = table.update_item(
					Key={
						'uri': uri
					},
					UpdateExpression="set last_rendered = :n, c_hash=:h",
					ExpressionAttributeValues={
						':n': n,
						':h': hash
					},
					ReturnValues="UPDATED_NEW"
				)
			summary.append({"uri": uri})
	return summary

def send_summary(ses, summary, branch, bucket, recipients, efrom):
    response = ses.send_email(
        Source='kyle@dataskeptic.com',
        Destination={'ToAddresses': recipients},
        Message={
            'Subject': {
                'Data': 'Deploying ' + branch + ' to ' + bucket
            },
            'Body': {
                'Text': {
                    'Data': json.dumps(summary)
                }
            }
        },
        ReplyToAddresses=efrom
    )

def clean_up(dest):
	shutil.rmtree(dest)

def md(absfile):
	f = open(absfile, 'r')
	c = f.read()
	f.close()
	html = markdown.markdown(c)
	return html

def knitr(absfile):
	r = robjects.r("""
		library('knitr')
		knit('{}')
		""".format(absfile))
	fname = r[0]
	f = open(fname, 'r')
	c = f.read()
	f.close()
	os.remove(fname)
	return c

def nbconvert(absfile):
	f = open(absfile, 'r')
	c = f.read()
	f.close()
	nb = nbformat.reads(c, as_version=4)
	html_exporter = HTMLExporter()
	html_exporter.template_file = 'basic'
	(body, resources) = html_exporter.from_notebook_node(nb)
	return body

if __name__ == "__main__":
    repo = 'https://github.com/data-skeptic/blog'
    branch = 'dev'
    tblName = 'blog'
    bucket = 'dev.dataskeptic.com'
    emails = ['kylepolich@gmail.com']
    ignore = ['/README.md']
    #
    parsers = {
        '.md': md,
        '.Rhtml': knitr,
        '.ipynb': nbconvert
    }
    #
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(tblName)
    s3 = boto3.resource('s3')
    ses = boto3.client('ses')
    #
    dest = '/tmp/' + str(uuid.uuid1()) + '/'
    filename = download(repo, branch, dest)
    repo_root = dest + filename
    # TODO: Check that no router paths match blog folders, /blog approx match goes to /blog/ml/2016/blah
    src_dict = get_src_dict(repo_root, filename, parsers)
    content_dict = get_content_dict(table)
    plan = new_content_render_plan(repo_root, src_dict, content_dict, parsers, ignore)
    summary = execute_plan(plan, s3, bucket, table)
    send_summary(ses, summary, branch, bucket, emails, ['kyle@dataskeptic.com'])
    clean_up(dest)




