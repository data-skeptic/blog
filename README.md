# dataskeptic.com blog

This repository holds the source files and codebase for rendering blog posts from Jupyter notebooks, Rhtml files, and markdown.  It also contains the codebase to upload these into the dataskeptic cms.

## Guest Bloggers Invited

Please check out details in these two posts:

[How to be a guest blogger on dataskeptic.com](http://dataskeptic.com/blog/meta/2016/how-to-be-a-guest-blogger-on-dataskeptic.com)

[Using git as a CMS](http://dataskeptic.com/blog/meta/2017/using-git-as-a-cms)

## Deploying

This repository includes a command line tool for rendering Jupyter notebooks, Markdown files, and Rhtml files.  The rendering process does the following things:

* Run code (Rhtml only)
* Convert to html
* Extract all images (Jupyter notebooks and Rhtml)
* Push images to S3
* Check for static images included in the repository.  For example filename `my-post.md`, put static images in a folder called `src-my-post` in the same directory as `my-post.md`.  Your file should relatively link to images in that folder.  All files in the folder will be copied to S3
* Push the final html file to S3
* Call blog api to insert a new record and link to S3 content

## Creds

If you are going to be updating content on dataskeptic.com, you will need creds (this probably only applies to you if you are an employee of dataskeptic.com).

```
{
    "accessKey"  : "********************",
    "secretKey"  : "****************************************"
}
```

T

## Installing

If you're interested in installing this software under our license, best plan is to reach out for help.

