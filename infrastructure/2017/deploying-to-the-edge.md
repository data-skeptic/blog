## Deploying to the Edge

A major theme of the Microsoft Build 2017 keynote was Microsoft's investment in cloud, AI, and edge.  In this context, MS uses the term AI to describe object recognition, integration across a network of devices, and a layer of intelligence to generate notifications.

They provided one hands on use case and one theoretical.

Their hands on use case was a manufacturing company named Sandvik Coromant.  This company is using machine learning on the telemetry from their industrial devices to detect the need for maintenance.  As you can imagine, when a major machine in a factory breaks down there can be significant safety risks as well as a cascading downtime and loss of efficiency.  Monitoring and predicting possible system failure can dramatically reduce system downtime.  I first discovered this use case in a conversation with a delivery company that monitored their fleet in a similar way.  Any large organization with physical devices in their workflow that *isn't* doing this is falling behind.

In the case of Sandvik Coromant, they had optimized the problem to the point that latency was their next bottleneck.  Data left their factory, went through the network to Azure, was processed by Azure Functions and other tools, then responded back to the factory.  The latency was a little over 2000ms.

Satya said something particularly observant: "Data has gravity; computational power will move toward it".  This is exactly what happened with Sandvik.

Using Microsoft's new Azure IoT Edge runtime, they were able to deploy the same code running in the cloud to run directly on their devies in the factory, reducing latency to around 100ms.

So what is this Azure IoT Edge runtime?  As best I could tell from the demo, the core unit is a Docker container.  I like this approach.  I've had some bad experiences with technologies like PMML in the past which try to provide similar functionality.  With Docker as the base unit, I have a lot more confidence that I'll have the support and longevity I need from a solution.

I imagine there can be challenges getting industrial equipment to run a Docker container.  Specialized industrial machinery like what Sandvik presumably has tends (in my experience) to run about a decade behind in terms of standards and best technology practices.  It also tends to bias towards proprietary systems.  Yet that's an issue for another discussion.

So long as the machine's controller can be managed by a machine that can run a Docker container, this is a pretty elegant solution.  As I understand it, the Azure IoT Edge runtime facilitates deployment and change management, which is a huge plus in removing DevOps headaches.

The second demo included in the keynote related to edge computing was a hypothetical workplace safety scenario.  Microsoft is preparing for world in which commodity cameras have fully coverage of workplaces.  That's a pretty attainable vision, so what next?

The hypothetical demo involved the identification of various tools and people through image recognition.  It's unclear to me how many of those object recognition models are available by default in Cognitive Services vs. those that need to be trained, but that's a great integration problem for a competent data science team to tackle.

With good camera coverage, and a powerful cloud to process the streaming data, running multiple object recognition models, one can achieve a real time description of all the players and tools in an environment.

Great, now what do we do with that?  The demo proposes several novel applications.  Location of tools, identification of unsafe conditions, and detecting when unauthorized/untrained actors attempt to use tools they aren't supposed to, a factor manager could ensure his or her team is safe, compliant, and able to find the tools they need.

A significant amount of computational power will be required to deliver on these visions.  Edge computing is certainly going to need to play a key role in realizing it.  With the ability to programatically create and destroy hundreds of powerful virtual machines in one click, it's easy to take for granted what can be accomplished... in the cloud.

But the Edge use case is perhaps the most critical one.  The speed of light is the upper limit on network communication.  Thus, when the sheer volume of data becomes the limiting factor (rather than the models that process the data), engineers will need to worry about where computations take place.  In my experience, this has always been a painful, deliberate, manual choice.  It's clear that future success, particularly in industrial spaces, are going to require a better framework for agile computation.