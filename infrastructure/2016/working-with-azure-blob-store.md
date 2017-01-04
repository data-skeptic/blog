## Working with Azure Blob Store

I recently heard that Azure Blob Storage added an Append Blob type which is optimized for append-only blobs.  Depending on what "optimized" actually means, this might be a wonderful solution for a project I'm currently working on, so I needed to check it out.

I found some of the documentation a little lacking, so I thought I'd do a rather in depth step by step walk through on how I got configured.

To get started, you'll need to create a storage account.

![Create Azure Storage Account](https://s3.amazonaws.com/dataskeptic.com/infrastructure/2016/azure-append-blob-0.png)

The wizard is pretty self explanatory.

Once the storage account is created, you'll need to get your credentials and set two environment variables: `AZURE_STORAGE_ACCOUNT` and `AZURE_STORAGE_ACCESS_KEY`.  Of course, you can provide these programatically, but I'm a fan of the [Twelve-Factor App](https://12factor.net/) design, so I'm going with environment variables.

For setting these on my development machine (a mac), I added these two lines to the file `~/.bash_profile`:

	export AZURE_STORAGE_ACCOUNT=myaccountname
	export AZURE_STORAGE_ACCESS_KEY=z7PyPmNXZER2yqGZ3wjW4EzdfahhRa4u72cVk6LR39/pF9NxVDjGm5T_RNTBQjshFyfu25WAYzqB5a/fxdMJdE=

The above values are, of course, fake, but I wanted to provide the access key in a recognizable format to help you find yours.  The screenshots below may help you

![Find Azure Storage access key step 1](https://s3.amazonaws.com/dataskeptic.com/infrastructure/2016/azure-append-blob-1.png)

![Find Azure Storage access key step 2](https://s3.amazonaws.com/dataskeptic.com/infrastructure/2016/azure-append-blob-creds.png)

The screenshots above show me working within the Azure dashboard.  I generally do that for tasks that I perform rarely, such as looking up keys or creating services, even though those functions can also be scripted.  From here forward, let's switch to scripts for doing operations I frequently perform.

The first thing I want to do is create a container if one doesn't already exist.  Containers (note - NOT the same as Docker containers) are akin to Buckets in AWS.  They are general groupings of a mixed bag of whatever you choose to store.

	var azure = require('azure-storage');

	var container = 'my-test-container'

	var blobService = azure.createBlobService();
	blobService.createContainerIfNotExists(container, {
	  publicAccessLevel: 'blob'
	}, function(error, result, response) {
	  if (!error) {
	  	console.log("Created " + container)
	  } else {
	  	console.log("Cound not create container, exiting.")
	  }
	});


Azure Storage has a number of different types of things it can store such as files, queues, and tables.  Blobs, and specifically, append blobs are what is interesting to me today.

Unfortunately, Azure doesn't seem to have a method for writing to Append Blobs which appends or creates if it doesn't exist.  Thus, if you aren't sure if your Append Blob exists, you'll need to use `blobService.getBlobProperties(container, blobname, callback)` to check.  Because these calls are asynchronous, I'm a little uncomfortable with that since it seems that things might occur out of order sometimes.  I'm going to design my application to guarentee I know in advance whether or not I'm creating an Append Blob or Appending to one.

## Creating an Append Blob

The script below will create an Append Blob called `test.txt`.

	var blobname = "test.txt"
	var s = "This is the start of the test file\n"

	blobService.createAppendBlobFromText(container, 
		blobname,
		s,
		function(error, result, response) {
		  if (error) {
		  	console.log(error)
		  }
		}
	);

## Appending to an Append Blob

The script below will append to your append blob.

	var s2 = "This line is appended\n"

	blobService.appendFromText(container, 
		blobname,
		s2, 
		function(error, result, response) {
		  if (error) {
		  	console.log(error)
		  }
		}
	);


