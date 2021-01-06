## Why Serverless Data Science?

First, "why Serverless?"

I was fairly skeptical about Serverless computing when AWS Lambda debuted, but I've since come around to being a devout practitioner.

What is Serverless computing?  It's a service (e.g. AWS Lambda, Azure Functions, GCP Cloud Functions) which runs your code for you on demand.  You pay only for what you use.  Scalability is (mostly) their problem.

Many developer's first experience with Serverless Functions was creating some simple task (perhaps image thumbnailing) and writing their code directly in the browser and then running the function for it's single service.  In truth, that's a great example of a basic Serverless use case.  A very basic one.

The Serverless infrastructure doesn't care that your code is "simple" or serves only one function.  Your source code could be a full micro-service or even a monolith.  With tools like [chalice](https://github.com/aws/chalice) it's very simple to spin up a fully serverless, mature API in a matter of minutes.  Existing non-serverless projects can often be ported to Serverless quite easily if the use case is a good match and the code is well structured.

Now, "why Serverless **data science**?"

* Reduce friction with other teams
* Scalability
* The benefits of event driven design
* Deploying models

### Reducing Friction

While organizations in general are becoming more mature about how to empower data science efforts, there are still many efforts by IT and Dev Ops groups to force all shaped pegs into one square hole.  Data science groups have special needs.  They need to iterate more quickly and rollback more often than traditional software development.  That's a feature of their work, not a bug.

Serverless as a platform promotes the user of environments as a first principle.  Regardless of the tools a team selects, there's no excuse for not following some basic best practices that will enable a relatively easy hand off of data science related work in a manner that minimizes back and forth during the release and monitoring processes.

### Scalability

While simply writing something Serverless doesn't intrinsically make it more scalable (your implementation does), some basic best practices and design choices will ensure that any scalability issues you face are going to be your Cloud Provider's problem, not yours.  That can be a scary proposition to some.  However, it's more than likely you are not the biggest fish in their pond.  The providers are treating these as first class services.

If you are thorough in your research, you'll learn about things like the cold start problem and even concurrency challenges that some organizations have faced when scaling up.  For extremely conservative technology groups, this can be a reasonable signal to wait.  But Serverless is no longer an "if", it's a "when" for most groups.  But remember, these are first class services.  Providers are actively working on reducing or eliminating the cold start problem through engineering and product customization.

When in doubt, wait; but not too long.


### Event Driven Design

The tools and training of a data scientist typically lead them towards thinking in batches.  Get **all** the training data and build a model.  Grab big chunks of data and run it step by step through a data pipeline in order.

There's nothing wrong with that approach, per se.  Engineers whose work demands that they build such batch systems eventually start micro-batching them, which is the first step towards something more event driven.

Once a model is built, and you want to make real-time inferences in your production system, suddenly, you're living in an event driven world whether you like it or not.  Many groups stubble at this very stage when they've learned their feature engineering process needs to be re-implemented for this setting.  An event driven design can solve many, if not all, of these problems.

Event driven software has many benefits that you can read about generally.  Specifically for the case of data science projects, I frequently recommend adopting event driven approaches in order to provide just enough guard rails to avoid unexpected technical debt.

If everything in your system is an event, then as every observation is made or record arrives, it can be processed.  Whatever features need to be calculated or 3rd party services need to be referenced, do them immediately.  Package up that bundle of data and ship it along for storage, input to a model, or future training data.  Feature engineering changes can now follow a more typical software lifecycle, making new model development a breeze rather than a time sink.


### Model Deployment

For model training, Serverless is probably not the right use case.  Aside form being resource intensive and unpredictable in run time, it's typically unnecessary.  Rarely do you need your model trained **RIGHT NOW**.

An offline training process should result in some binary asset.  In almost all cases it should be stateless.  Standard machine learning models don't have any internal memory or state (although one could argue this is what transformers are).  Give the model the input, get the output.  Give it the same input, get the same output.

Certainly your features may change.  If a fraud detection model requires `num_failed_logins_last_24_hours`, that number may go up and down but the model itself has nothing to do with the updating or persistence of that information.

A stateless model is an ideal case for Serverless design!  You may face some challenges getting your model shoehorned into a lambda function.  I've got a few battlescars from activities like that which I can share in future posts.  But the pain is well worth it in the end when your model can inference on someone else's hardware without your concern.,


## Recommended for further consideration

* [Serverless NLP Model Training](https://dataskeptic.com/blog/episodes/2019/serverless-nlp-model-training) Alex Reeves from Data Skeptic explains a Serverless model training project.

* [Kubernetes vs Serverless](https://softwareengineeringdaily.com/2020/05/29/kubernetes-vs-serverless-with-matt-ward/) - An episode of Software Engineering Daily covering ground not touched on here.

* [AWS Chalice Quickstart](https://aws.github.io/chalice/quickstart.html) - Live the Serverless dream in under 10 minutes.

