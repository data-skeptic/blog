# Blog Deployer

This repo contains both our blog and the software which deploys it to our backend.

We deploy onto AWS Lambda using the Chalice library and manually create a webhook in Github to trigger the lambda API on any database change.

```
python3 -m venv $(pwd)/venv
pip3 install markdown --target ./venv/
pip3 install bs4 --target ./venv/
pip3 install lxml --target ./venv/
```





# dataskeptic.com blog

This repository holds the source files and codebase for rendering blog posts from Jupyter notebooks, Rhtml files, and markdown.  It also contains the codebase to upload these into the dataskeptic cms.

## Guest Bloggers Invited

Please check out details in these two posts:

[How to be a guest blogger on dataskeptic.com](http://dataskeptic.com/blog/meta/2016/how-to-be-a-guest-blogger-on-dataskeptic.com)

[Using git as a CMS](http://dataskeptic.com/blog/meta/2017/using-git-as-a-cms)

