from deploy import *

absfile = '../methods/2017/the-formal-statement-of-p-not-equal-to-np.md'

s3 = boto3.resource('s3')
bucket = 'dev.dataskeptic.com'
parser = md
contents = render_uri(s3, bucket, absfile, parser)
f = open('out.htm', 'w')
#contents = contents.decode('utf-8')
print(type(contents))
f.write(contents)
f.close()
