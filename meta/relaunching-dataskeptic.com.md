## Relaunching DataSkeptic.com

We've spent the last few weeks tinkering away on a new web design.  As I write this, we're in the final stages of coding the site.

Our old site was hacked together without much of a long term plan.  While it served it's purpose, it also looked notably amateurish.  With this relaunch, we've embraced React.js as our primary framework and built the entire site on top AWS architecture.

The site deploys to AWS S3.  The old site ran off a single serve, so in times of high traffic, it would slow down.  That's no longer a problem, as Amazon S3 functions as a CDN for us.

The dynamic elements leverage a great deal of AWS API Gateway and Lambda architecture.  Essentially, we've embraced "serverless" and I couldn't be happier about it.

I'm excited for the forthcoming relaunch and some of the near and long terms plan we have to expand it as well.
