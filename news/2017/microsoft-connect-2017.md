## Microsoft Connect 2017

I attended Microsoft Connect today.  These are my notes about the announcements I found noteworthy.


### Visual Studio Live Share

The first novel announcement that caught my attention was a feature called Visual Studio Live Share.  This tool allows users of Visual Studios to easily do a live codeshare for collaboration purposes.

Codesharing is nothing new, and many free tools are available to make it possible.  For users of Visual Studios or Visual Studios Code, its integration with their IDE of choice makes other options rather obsolete.  There's also no barrier between these IDEs. One user in Visual Studios can collaborate with another in Visual Studios Code.

The feature has all the options you would expect.  You can see your collaborator's cursor.  Their highlights are live on your screen.  All this happens in real time.

What was particularly novel (to me, at least) was the ability to share a debugging session.  A user can run a local debugging sessions which is also shared with the collaborator.  The collaborator can see when a report breakpoint is hit, inspect values, and make code improvements as if they were literally in front of the same machine.

This is a really slick feature that could be greatly beneficial for me when managing remote teams.


### .NET Embedding

I built a few Android apps many years ago.  Not just apps with some boilerplate code or a useless app that's just a webview of an existing website.  I built some "real" apps.  When finishing them, I looked at the options for migrating the app to iOS.  At the time, there were essentially no options whatsoever.

Since then we've seen the emergence of React Native and Xamarin.  I'm sure there are more options here, but these are the two I'm familiar with and of the two, I only have experience with React.

Announced today was a major step forward in portability of .NET code.  Essentially, it looks like you can now export .NET code (and presumably the .NET runtime) and easily get that code to play nice with Swift, Java, etc.  I'm not entirely clear on the relationship between .NET and Xamarin, but its clear that if you're doing mobile development and you want true portability, you should familiarize yourself with these options.


### Visual Studio App Center

Again, despite dabbling a bit, I'm not really a mobile developer.  If I was, I'd be more curious about another announcement: Visual Studio App Center.  This appears to be a one stop shop for managing continuous integration, version distribution, deployment, crash reports, testing, and iteration cycles.


## Azure Container Service (AKS)

I was very interested to learn about Azure Container Service.  Naturally, this is a competitor for AWS's ECS (EC2 Container Service).  However, some features that aren't part of ECS were announced that caught my attention.  New feature announced today allow you to use Azure as a debugging environment.  This means instead of debugging your code locally, you "Debug As" to the cloud.

For anyone who has every suffered through the pains of trying to run and coordinate multiple Docker images or wasted hours mocking out services in a vain attempt to get your local development environment to look something like your production environment, this offering promises to solve your problems.


### SQL Operations Studio

Although not discussed in details, SQL Operations Studio was mentioned.  I would have liked to have learned a bit more.  Despite not being a heavy user anymore, I used SQL Server extensively in the past and never had any complaints.  I'm also impressed with some of the more recent advancements allowing Python and R code to run on the database server.  For many applications, keeping your models extremely close to the data has a huge advantage that isn't really matched in any other model deployment solution.

SQL Server Operations Studio appears to be an enterprise monitoring tool.  I presume developers would still work in SSMS, but I think this could be a useful tool for a DBA or lead.


### CosmosDB

We've covered [CosmosDB](https://dataskeptic.com/blog/episodes/2017/cosmos-db) previously on Data Skeptic.  It's a globally distributed multi-modal data store.  The multi-modal part refers to the fact that it functions as a relational database, graph database, and document store.  Announced today were extensions for Spark and, most notably, Cassandra!  The addition of streaming into the mix makes CosmosDB much more attractive to me.


### Azure Databricks

One of the most surprising announcements for me was Azure Databricks.  I'll be blogging about that separately.


### Cognitive Services

A demo of Cognitive Services image recognition didn't introduce much new.  However, What I did find noteworthy was some of their model export options.  Once you train an image classifier, it can be exported as CoreML for iOS.  They say they'll be adding an option for Android in a few weeks.

What this means, is that the challenges of model deployment might be solved.  Typical implementations take a thin client approach.  Any data (image or otherwise) is packaged up, shipped to the cloud, scored, and returned to the device.  While this works fine in many situations, it introduces latency and does not work if connectivity is a problem.  Exporting the model and running natively is a huge win for people facing either of these two challenges.  The integration from a code perspective looks fairly seamless.


### Visual studio tools for AI

With the installation of a new plugin, A "AI Tools" pull down now appears in Visual Studios.  One focus of this effort appears to be galleries and helper libraries.  That's not of particular interest to me, but someone getting starting in machine learning might find it very valuable.

What was much more interesting to me was some of the model training options that appear to be integrated rather nicely into the IDE.  These new tools allow gives users the option to essentially right click and "Train in Cloud".  Abstracting away some pain points in this area is a nice win.  As long as you have an image set up in Azure, this process appears to be painless.

Also of note is the introduction of `System.Numerics.Tensor<T>` to the .NET framework.  This removes some translation that was previously going on when reaching out to external tools like Tensorflow and CNTK.

Lastly, although I haven't checked it out myself, the presentation concluded with a mention of [aischool.microsoft.com](http://aischool.microsoft.com) which might have some nice tutorials for getting started.



