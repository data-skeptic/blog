## Ethical AI at MS Build 2018

For a conference that is usually about product and service announcements, Build 2018 got off to a surprising start.  Microsoft CEO Satya Nadella began his keynote with a few high level comments on the transformtive nature of technology and what Microsoft sees as it's role is helping people innovate.  Of course, it wouldn't be a Microsoft keynote without a mention of IoT, edge computing, and cloud.  THe keynote then pivoted to a focus on data privacy, cybersecurity, and ethical AI.

Although mentioned, GDPR was not the focal point of these statement.  Sotya described a vision in which Microsoft is building the tools that strive to guarantee data privacy and safety.

Most surprisingly, Satya name dropped word embeddings and homomorphic encryption.  I did realize word embeddings, like those created by word2vec, were now common parlance.  That's all for the best given the impact these methods have had on natural language processing.  Specifically, he echoed well known concerns about bias in word embeddings.  If we train our models on a real world corpus, and that corpus contains racism, sexism, or bias of any kind, then those biases will be learned by the model.  As for homomorphic encryption, this remains, IMO, an aspirational goal.  A fully homomorphic system (what you really need to be useful) has some theoretical gaps and limits today.

Satya also referenced some unnamed companies in healthcare and pharma being their key early partners in exploring the topic of privacy.

> "We think the cloud act is a good start" - Satya Nadella, Build 2018

The keynote eventually concluded with the announcement of [AI for Accessibility](https://www.microsoft.com/en-us/ai-for-accessibility), an initiative to push for more substantial efforts helping leverage machine learning to build tools that make the world more accessible for disabled people.

The keynote next delved into case studies and an announcement that Azure IoT Edge is going open source.  I'm not deeply framiliar with their IoT Edge platform, outside of knowing the objective is to allow deployment and change management on edge device with ease.

A great use case here is the concept that a developer could train their own facial recognition algorithm and deply it directly to the device.  The typical model for home security and facial recognition involves a camera transmitting images to a server for processing.  This means images of your home are sent elsewhere, raising fears about what happens when that cloud service mismanages your data and intimate photos taken by your own security camera are leaked to the internet.  With an edge based approach, the model can exist and ruin on the device, keeping your data from leaving the premises.  Of course, under some conditions (unknown face observed), you can optionally send data to the cloud for further action.

Microsoft customer Jabil was featured.  They have some sort of industrial scale image recognition service.  Their existing solution involved centrally processed analysis.  Introducing some programable circuits which could run at the point of data generation provided an order of magnitude throughput improvement for their particular application.  In other words, running the model on lightweight hardware that lives right next to the sensor was the key enhancement.

The presentation moved on to one of the more impressive live demos for an event like this.  DJI Rockwell Automation builds high end drones.  Microsoft is building out tools to make it possible to build and deploy AI models.  The demo involved a human pilot navigating a drone to a specific location where it was able to locally run an image detection algorithm to identify a defect in a pipe.  Everything worked in this demo, but it still feels a bit future looking.  However, this technology is certainly getting close.  There's a huge opportunity here in industrial safety and monitoring.  Imaging drones that automatically scan the perimeter looking for visible issues.  Similarly, imaging when a sensor raises an alarm in an industrial setting.  A human inspect would be deployed.  A drone could probably get to the point of issue faster and with no safety risk.  I'm not convinced its commercially viable, but it's getting close!

Satya returned to the stage to focus on AI breakthroughs at Microsoft, the most recent being machine translation at human parity.  Microsoft's goal is to commoditize AI, putting it into the hands of every developer in every organization.  Satya talked about Microsoft's path from basic low level cognitive services to the more specialized solutions that have become part of their offerings over the last few years.

### Project Kinect for Azure

Microsoft is working to expand on their learnings from building the vision systems and sensors for their gaming products, bringing a specialized piece of hardware to market known as Project Kinect.  It's a set of sensors and tools for developers to interate into whatever their application is.  It seems that Microsoft believes user interfaces are going to be radically transformed in the future, depending more significantly on gaze and gesture.

### Azure Conversational AI

> "We're launching 100+ new features for the bot framework."

Satya spoke very ambitiously about the tooling and customization they're introducing for the Microsoft Botframework.  Disappointingly, nothing specific was shared, just high level aspirational ideas.

### Voice Assistants

The keynote included a demo of how Cortana is available via Alexa.  The demo implies that Microsoft's vision for voice assistants involves specialied agents like software.  Users might select Alexa for some purposes, Cortana for others, and the Data Skeptic bot for yet other things.  The demo was nothing innovative, in my opinion.  This was the same "what's on my calendar" types of basic demos that really show the maximum capability of current systems.  Despite my personally pessimistic outlook on voice assistants being truly useful in the near future, I do think the vision of having independent voice agents is the right path.  Agents can be customized easily by tone of voice to make it clear that the user interface is in a different "mode", and we can learn which specialized agents we want to request to talk to, depending on our needs.


