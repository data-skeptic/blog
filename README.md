# Blog

This repo contains both our blog and the software which deploys it to our backend.

We deploy onto AWS Lambda using the Chalice library and manually create a webhook in Github to trigger the lambda API on any database change.


## Work in progress

- [ ] chalice with new features added
- [ ] Add bio
- [ ] Lambda API which adds related_content to Parquet
- [ ] Tool for June
- [ ] Migrate related_content
- [ ] SNS publish
		- [ ] Slack message
		- [ ] Auto-tweet
		- [ ] Trigger feature engineering pipeline
		- [ ] Trigger ad extraction
		- [ ] Update Bot's Globals with latest episode info
		- [ ] elastic search update
- [ ] Delete
- [ ] jupyter image to image file (jupyter.py TODO:)
- [ ] Rmd: ./tools-and-techniques/2018/elo-ratings-for-ncaa-basketball.Rmd





# Guests

Send us a pull request to update photo or bio.


# dataskeptic.com blog

This repository holds the source files and codebase for rendering blog posts from Jupyter notebooks, Rhtml files, and markdown.  It also contains the codebase to upload these into the dataskeptic cms.

## Guest Bloggers Invited

Please check out details in these two posts:

[How to be a guest blogger on dataskeptic.com](http://dataskeptic.com/blog/meta/2016/how-to-be-a-guest-blogger-on-dataskeptic.com)

[Using git as a CMS](http://dataskeptic.com/blog/meta/2017/using-git-as-a-cms)

