# Data Skeptic Blog

The software which runs the Data Skeptic website is linked to this github repository.  When a PR is merged into the `master` branch, **Portal** will be notified of the commit.  **Portal** will mirror the updates to the `feaas-prod` S3 bucket, and a File Trigger in **Portal** will render the contents of the file to HTML.  Lastly, that rendered HTML file is published to a special bucket used by our website, and various metadata elements are updated in DynamoDB.

