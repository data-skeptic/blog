# Blog

- [ ] some object that answers webhook and writes to s3 as .github.webhook
- [ ] spider responds to .github.webhook, generates crawl requests
- [ ] github2html
    - [ ] render (add/update)
    - [ ] handles images
    - [ ] delete ...?





## Install

```
chalice deploy --connection-timeout 600
```

Then, log into AWS console and set the `arn:aws:lambda:us-east-1:668099181075:layer:AWSLambda-Python37-SciPy1x:2` as a Lambda Layer.

## Deploy

```
chalice deploy --connection-timeout 600

aws lambda update-function-configuration --function-name blog-dev --layers arn:aws:lambda:us-east-1:085318171245:layer:pandas-layer:4
```

## Calling

curl https://p34qlugnt6.execute-api.us-east-1.amazonaws.com/dev/blog/posts

curl https://p34qlugnt6.execute-api.us-east-1.amazonaws.com/dev/blog/posts?id=/blog/tools-and-techniques/2016/los-angeles-library-trends


## Work in progress

- [ ] dataskeptic.com dependency
		- [ ] Fix WTF links in libsyn
				- [ ] find existing
				- [ ] make google sheet of redirects
				- [ ] fix libsyn
				- [ ] re-run update
				- [ ] give redirects to cory
- [ ] Add bio
- [ ] Tool for June - new admin by Cory
		- [ ] curl to add bio
		- [ ] curl to add content
- [ ] Migrate related_content
- [ ] SNS publish
		- [ ] elastic search update
		- [ ] Update Bot's Globals with latest episode info
		- [ ] Trigger ad extraction
		- [ ] Slack message
		- [ ] Auto-tweet
		- [ ] Trigger feature engineering pipeline
- [ ] Delete
- [ ] Rmd: ./tools-and-techniques/2018/elo-ratings-for-ncaa-basketball.Rmd
- [ ] scienceblogs.com
		- [ ] easy link to github private


