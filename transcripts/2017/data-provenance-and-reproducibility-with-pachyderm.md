**Intro:** Data Skeptic is the official podcast of DataSkeptic.com bringing you stories, interviews, and many episodes on topics of data science, machine learning, statistics and artificial intelligence. 

**Host:** [Daniel Whitenack](https://www.linkedin.com/in/danielwhitenack) has a PhD in Computational Physics from Purdue University. He’s worked in a diverse set of industries developing data science applications and is a frequent speaker at conferences. He is the maintainer of the Go kernel for Project Jupyter and is presently a data scientist and lead developer advocate at Pachyderm Inc. 

[Daniel](https://twitter.com/dwhitena) also teaches corporate and public data science and engineering classes with [Arden Labs](https://www.ardanlabs.com). I invited Daniel on the show to discuss data reproducibility, provenance, and pipelines. 

Daniel, welcome to Data Skeptic. 

**Daniel:** Thanks. It’s a lot of fun to be here. 

**Host:** So I find – starting with our first topic of reproducibility –  that word can mean different things to different people. I’m wondering if maybe you’ve had that same experience. And if so, could we start with [what the definition of reproducibility might be to an engineer](http://www.tss.trelleborg.com/wiki/Reproducibility). 

**Daniel:** Yeah, definitely. It definitely means different things to different people. I would say in the case of engineering, it means that machinery or code or systems behave consistently over time. In the case of like software engineering, we expect if we have a function that adds two numbers together, if we put in 1 plus 1 the first time, it should equal 2 and 1 plus 1 the second, it should equal 2. And then other people should be able to run that function and have the same result. 

And in the same way in machinery and engineering in general, when you put your car into drive, you don’t want it to go into reverse. You want it to go into drive every time. So that’s kind of a big portion of what good engineering is. 

**Host:** Now, you’ve got a scientific background as well and I suspect in that community, reproducibility can mean something not entirely different but there are a lot of nuances. Could you maybe share your perspective on the distinctions that a scientist would make over an engineer? 

**Daniel:** That kind of engineering reproducibility that we just talked about is kind of a precursor and part of scientific reproducibility. I mean scientists use machinery. They use code to do a research and to make predictions and to write algorithms and whatever it is. So having that consistent behavior in the engineering tools that they’re using is definitely a part of it. 

But then as we’re talking about science and scientific endeavors, a lot of times those endeavors are pushing the envelope as far as what we know, what we’ve done in the past whether that’s in the context of academia or in a company pushing what a company has done in the past as far as scientific and statistical analyses. 

Part of reproducibility in science is you’re pushing that envelope, you’re trying something new and just that first time when you find a new result, or you’re able to do something new. If you only do that once and you’re not able to ever reproduce it then you can’t really have a lot of confidence that you’ve actually discovered something new or done something new that’s valuable. 

In science, people are always building on a scientific discovery of others. Just like in data science, we’re building on things that people have already developed in certain models and other things. But there’s this collaborative effort, if we’re not able to reproduce what other groups and what other people have done in the same way that they did it then we – that incremental improvement of our methods is hampered. 

**Host:** That sort of confirmatory evidence makes a lot of sense of why we trust the scientific theory. In contrast, why is reproducibility critical in business? 

**Daniel:** That last answer kind of leads into this aspect. And I’d like to think about this in a few different ways. So first off, I think that reproducibility is a precursor to true incremental improvement in your methods within a business. If you’re not able to understand what you did before or what other people have done in the company and be able to reproduce it, it’s much more difficult to be able to improve on what has been done in the past. 

And so, there is that development implication and part of that is also having to do with collaboration. If you’re working with a larger team, you want to be able to share something with other people in the team, be able to reproduce what other people have done so that you can continue that development cycle. 

In other area, I think which is becoming a lot more important over time in a business is that more and more we’re making our decisions within a business based on the algorithms that we have. So we’re choosing whether people get a certain insurance policy or maybe more dramatically we’re driving people’s cars now with computers, right? More and more as we see these kind of user-impacting technologies, we’re going to see governments and other institutions, institute regulations and compliance sort of things around algorithmic decisions. 

So it’s very possible that if you’re not able to reproduce what you did before or have some explanation of that or some understanding of what went into an analysis and how to reproduce that, then there could very well be compliance issues as we’re starting to see in the European Union and other places. 

**Host:** So when I think about software engineering, a lot of the concepts of reproducibility and in being very deterministic make obvious sense to me. As you said, 2 plus 2 must always consistently equal 4 or even when I add something to my cart that should always have the same effect. 

But when it comes to data science and I guess maybe I’m specifically thinking of machine learning, there are a lot of methods that have nondeterministic steps. How can we maintain some semblance of reproducibility when algorithms leveraged some random data to make a choice in formulating a model? 

**Daniel:** That’s a really great question because I think a lot of people immediately jumped to the conclusion that in these scenarios you kind of have to throw reproducibility out in order to use these more sophisticated techniques. And I think that’s definitely an excuse, not to say that I haven’t been tempted and haven’t had those thoughts in the past but when I go back to is in my training back in physics, there are a lot of parallels because in fields such as quantum mechanics let’s say, there’s certain behavior that is very much dependent on let’s say an electron going through two slits in a screen. We might not know every time which hole the electron went through. But we know the patterns that should be visible around that. 

In that case, it takes doing the experiment over and over and over to develop these patterns and to understand what we expect. And just because things are nondeterministic in that way doesn’t mean that there are not reproducible patterns in our work. If that wasn’t the case then the laws of quantum mechanics that we rely on for building computers and other things wouldn’t exist. 

So in the similar way to what we do in machine learning, we rely on a lot of sort of random processes or nondeterministic steps in certain machine learning algorithms. But really, what you want to think about is you should have a reproducible pattern that is produced out of your models and out of your processes. 

Even if that’s not exactly the same over time, you should be able to run it over and over and understand the pattern within which you expect your model to behave otherwise you’re kind of just shooting in the dark because you don’t have proper expectations for how your model should behave. 

**Host:** It’s actually a really interesting point I haven’t thought of that even though let’s say, you and I had the same data set and we both ran your algorithm of choice ran it for us some deep learning, whatever the case maybe, the insides that black box might not be the exact same floating point number calculations but our result should be more or less distributed in the same fashion otherwise why are the models erratically different? 

**Daniel:** Exactly, yeah. And you should be able to come up with some expectations to say, “I expect this model based on what the data that I have trained it on in the past and exposed it to. I expect it to behave within this range of values in these scenarios.” And that way, you do have a sense of when something goes wrong and behaves outside of your expectations, either you can learn from that experience and adjust your expectations or you can really pinpoint something that went wrong with your model. 

**Host:** So there are a number of tools that we leverage to do reproducibility. Everything form source control and containers and of course, Pachyderm, that we’re going to talk about in a bit, the one I want to touch on first was the Jupyter notebook. And I want to ask what you see is its role in reproducibility analysis. 

**Daniel:** [Jupyter notebooks](http://jupyter-notebook-beginner-guide.readthedocs.io/en/latest/what_is_jupyter.html) are amazing. As you mentioned, I’m working – I work on the Go kernel for Jupyter and I love using Jupyter and other things like Interact and other things that are going on. And I think these in some ways bring a lab notebook sort of aspect to what we do as data scientists and industry. And that’s really great because you can not only have your code there, you can have your visualizations and add kind of a story along with it. That’s why they are so great for tutorials is because you’re really explaining what you’re doing in your analysis. 

And I think that one extremely important piece of reproducibility is that aspect of being able to share with the people in your team and save as a record the thoughts that went into your analyses and the results of those in a very notebook or lab notebook sort of style. 

So I think it’s definitely a piece of the puzzle at the same time. I had a friend who expressed to me that even though there is these great things about Jupyter notebooks, they kind of leave out one of the great attributes of a “scientific lab notebook” in that there’s no permanent chronological record of work that is paired with some logical ordering of data and results because these things are kind of snapshots and you don’t really see how they have morphed over time if you don’t combine that with some sort of data versioning or other sort of versioning. 

**Host:** Yeah. It’s interesting. They’re definitely a piece of the puzzle but they don’t tell the whole story. 

*Let’s take a quick break from this episode and talk about our sponsor for this week, which is [Periscope Data](https://www.periscopedata.com). What listeners might not know is that I import all the listeners’ stats from the podcast into a MySQL database. And I frequently put together a little manual dashboard that I cut and paste into an email that I send to Linda. *

*Linda: Yeah. You’ve shown it to me before but I recently noticed that they look way nicer and they’re interactive.*

*Host: Yeah, that’s definitely a piece of what I can do now that we’re using Periscope Data is not just help one making more attractive visualizations, for me, it’s about the speed with which I can do data exploration. Those old reports I used to send you required me to figure out my sequel statement then I’d copy and paste that into a Jupyter notebook. I’d get my data frame. I’d write like 10 to 20 lines of matplotlib code and it was kind of hard to do like just quick questions and look at the data in different ways.* 

*Linda: Right. So I noticed on the new dashboard, I could break down by country.* 

*Host: Yeah, that was totally easy using Periscope Data. I’m able to do all that stuff really rapidly, just work in my queries and go straight into a visualization and then put it all together in a dashboard to show you.* 

*Linda: And then you invited me. I created a login and I could customize the dashboard.* 

*Host: And that’s a first, right? My old report used to be static. Now, you can do some customization with it.*

*Linda: Yes.* 

*Host: So I’m going to personalize your dashboard and that’s going to be really easy using their tool. So I was glad I could share this with you so you could see firsthand now. But Periscope Data isn’t just for like one analyst working in isolation. It’s really great for a data teams and for collaboration.* 

*Linda: Head to PeriscopeData.com/Skeptics to start a totally free trial. If you sign up at [PeriscopeData.com/Skeptics](www.periscopedata.com/skeptics), you will receive one of their famous Periscope Data mugs.* 

*Host: Yes. And in addition to that mug, they will send you a bag of coffee so you can work as fast as they do. I really appreciate Periscope Data support this week. Their tool has helped me out a lot. I think it can help you out too. If you’re part of a data team that does rapid data exploration and you want to go straight from sequel into charts in a nice dashboard and things like that, head on over PeriscopeData.com/Skeptics to learn more.* 

So in several of your talks and blog posts and other things I followed about you online, it seems you’re a big advocate of data scientist thinking about data provenance. And we covered this topic briefly on Data Skeptic but it was some time ago. So I think it would be definitely good share some thoughts about this because I don’t see it always to the forefront in discussions of data science. So maybe could you share your definition of data provenance and why it’s important that a data scientist be considering it? 

**Daniel:** Data provenance in my mind is – well, I mean maybe we should take a step back and say, [what does this word provenance mean](http://siis.cse.psu.edu/provenance.html) because maybe you hear it in like the art world or something. So it’s not exactly like you said, maybe we don’t throw it around in our data science scenes too much. 

Provenance is really like saying something about something’s origin. So I was born in Albuquerque in New Mexico. And so my provenance at least part of it is I came from Albuquerque in New Mexico. In the same way that when you’re talking about provenance in an artwork, you’re saying like who has owned that art over time, how it’s passed through history, through hands, and that sort of thing. 

So now, if we bring that into thinking about data provenance, what we’re really talking about is that you don’t really have a full understanding of your data analyses unless you understand what happened to the data that you’re processing before it got to you and kind of where it came from and what happened to it. 

So in companies, a lot of times there is these very complicated data pipelines and various things might have happened to your data before you see it and you might have various transformations of that data. Maybe you joined two data sets first and then you set an index and then you aggregate some things and then you do various other things like normalization and whatever before you actually do any sort of sophisticated modeling. 

So all of those things that happened to your data before you see it, you should have an understanding of those, and provenance is really that understanding. It’s saying this is the record of what happened to my data so I can have an understanding and a confidence in the way that I’m processing it because I know where it came from, I know what happened to it. 

**Host:** So, I want to pick your brain on what are some of the tools you think, we’ve talked about Jupyter, are there any other things that you find helpful in maintaining good provenance and reproducibility standards on a team? 

**Daniel:** As you mentioned, we talked about Jupyter. I think keeping that sort of lab notebook mentality with Jupyter notebooks and whatever your docs are in an organization is important. So along with your project should come docs that explain the reasoning behind your analyses and that sort thing because people move from company to company and if you don’t have that, it’s also really hard for in the same way that people come in and out of research groups and academia, it’s hard for the incoming people to know what they can build on if that record isn’t there. 

So I think just some good practices around that are important. Also, I would say, this isn’t really tooling but I would say that as far as reproducibility and maintainability in a data science project, I think that we should really be celebrating simple but effective solutions to problems. So just because deep learning model can play a board game doesn’t mean you should be using deep learning because a lot of us aren’t playing board games day to day, right? 

So a lot of times, a very reproducible, very maintainable statistical analysis, maybe you’re just calculating, you’re aggregating something, calculating a max that could provide extremely great value in a company. It’s really easy to maintain and reproduce. 

But then as far as like actual additional tooling around things, as you mentioned, I work in an open-source project called Pachyderm. Pachyderm provides data versioning, which I think is incredibly important, if we don’t know what data was input to our model at certain times we can’t reproduce certain things that happened in the past and we can’t improve on certain scenarios. 

So that’s an important piece along with things like Docker which allows us to package up code and tag it so that we know this was the analysis the model packaged in this way that run at this time on this data that I have a version. And then of course those various evaluation techniques that I think are pretty good practices. 

The Elias Ponvert People Pattern, he has wrote a great database called LeVar which allows you to kind of consistently evaluate models over time and it’s a database that supports the sort of model evaluation and validation workflow. 

Those are some of the things that I found pretty interesting in this space. 

**Host:** So I know Pachyderm is a very popular project but I don’t want to take it for granted that every listener knows about it. You gave basically a high-level description of it but could we all go a step deeper and talk about how someone would get started using Pachyderm? 

**Daniel:** Pachyderm provides two things. It provides data versioning that is very closely tied to data pipelining. We really think that this is super useful because again, you want to make sure that you have a good understanding of how your code is versioned and what analyses you’re running and tie that very closely to what data is input and output of the various stages of your analyses. So this is really the vision behind Pachyderm and what it provides along with some great advantages of distributing that analysis over a cluster. 

To get started, it’s actually just a few commands to deploy Pachyderm locally on your laptop and try a few things. If you go to Pachyderm.io, there’s a link to the docs and there’s a “Getting Started” section there and you can deploy it in a few commands and then run for example a Tensor Flow example, a MapReduce sort of example, a web-scraping example. There are a few different ones in the docks that are pretty fun to play with. 

**Host:** So pretty much every company I’ve ever consulted for has a unique mix of different persistent layer technologies or databases or whatever the case maybe in languages and who knows what else in terms of architecture. What is Pachyderm compatible with? 

**Daniel:** Well, Pachyderm is powered by the container ecosystem, and so its language and framework agnostic. In other words, you can do Python, Java, Scala, Go, R, MATLAB, whatever sort of analyses you want within Pachyderm. But as far as what it’s backed by the technology that it’s backed by, Pachyderm runs on top of Kubernetes, which if people aren’t familiar, that’s an open-source orchestration framework from Google that basically allows you to distribute container-based processing over a cluster. 

Data that’s stored in Pachyderm in this data versioning scheme that I mentioned that’s backed by any object store of your choice so it could S3 or GFS or even an on-premises solution or custom solution. We just implemented a client which is basically supports any S3 compatible object store. 

So there are a lot of options as far as compatibility. But I think one of the main things that I really enjoyed as a data scientist is you can utilize all these languages and frameworks so you don’t have to restrict yourself to only one. 

**Host:** And what is the Pachyderm file system? 

**Daniel:** Yeah. So the Pachyderm File System is where the data versioning piece happens. So when you commit data into PFS or the Pachyderm File System, you can think about that kind of like you’re committing code into Get. When you commit data into Pachyderm, you commit that into “data repository.” So you could have any number of these repositories organized in whatever way makes sense for your project and then you commit that data into one of these repositories. 

And as you commit more and more data over time into the repositories, Pachyderm is aware of what data is new and what data is old. And this is like – this is kind of the really great thing about Pachyderm and PFS that I think I have a lot of fun with is that you can set up an analysis that’s analyzing data from one of these repositories and Pachyderm is smart enough to know when there’s new data available and to keep those analyses in sync with the data that’s coming in. And likewise, to not reprocess old data if you don’t need to. 

Host: Very interesting. I was in a situation, this was quite some time ago but basically, I was working on a system that did some forecast and then made adjustments to ad campaigns based on those forecasts. And of course, at the time when the forecast was good, everything was copacetic. 

But in the case where the forecast was not very predictive of the future, we’d end up in these scenarios where people would say, “What the heck were you thinking yesterday when you made this change to the account?” And we could never get back to what the data looked like at the time because it was all kind of overwritten as things went. 

**Daniel:** Yup. 

**Host:** What sort of a better place would I have been if I had had Pachyderm available to me at the time? 

**Daniel:** Yeah, exactly. So, if your forecasts were running in Pachyderm, every analysis that runs in Pachyderm or every transformation or processing stage, it outputs to another committed repository. So you might have your forecasting model outputting to a forecasting data repository in the future. 

Let’s say, tomorrow things don’t look so good, you can basically go back and see, OK, this is the data that changed in my forecast from the previous day to this day as well as this is the data that was input to my forecast the previous day or this day. And really get a picture of how the data changed and how that affected your result. 

And even in scenarios where let’s say that your data got corrupted and you committed bad data into something that eventually ended up producing bad results, you could see that bad data there or that corrupted data. Then in order to right the ship, basically, you would just need to commit the new good data into the repository and Pachyderm would then update everything and get everything in sync such that you don’t have to go through them manually to figure out the things you need to do just to make things better. 

**Host:** We made some rough comparisons to Pachyderm being like yeah, one of the things I love about Git is if a bug ever introduced into some code, if I can just find the one commit right before the bug, I can go get its ID and I can pull from there and kind of start over. 

**Daniel:** Exactly. 

**Host:** How secure is the workflow in Pachyderm. 

**Daniel:** Yeah. So in Pachyderm, actually the language mirrors that of Git although the actual file structure is slightly different but the language is similar. So you make commits into a repository and then you have a list of those commits over time. 

And combined with this provenance thing, like let’s say in that scenario where a certain forecast created a certain bad result, you can issue a command called “flash commit.” Basically, what that tells you is what the commit was that produced that bad result that you ended up with so you can see that’s part of the provenance sort of thing. 

So then you can go back and say, “Well, it was this commit that happened. What was the commit before that?” And then what you can do is roll back your data to that previous commit and update your analyses so that it’s like you’re going back in time to that previous snapshot. There is a lot of tooling around that currently in place and then we’re continually adding new things in the newest release in 1.4, which will be in March, there’s going to be even more tooling around those sorts of interactions. 

**Host:** Very cool. So when I think about really high velocity applications maybe like credit card transactions or even page views or little counters on sites, it seems to me there are maybe hundreds or situations of hundreds or thousands of like transactions, individual updates per second. And if Pachyderm has something I could commit, that must add a little bit of overhead to generate that snapshot. [Are there any best practices](http://www.mdsiinc.com/news/5-reasons-business-invest-security-certifications/) or maybe can you describe how you would work with Pachyderm in situation where we have really high-velocity data? 

**Daniel:** I forget the exact number off the top of my head but the overhead as far as the metadata that’s required with these commits is actually very minimal and it happens very quickly. So we’ve seen people very successfully implement very quick and streaming applications in Pachyderm. 

One of the things that’s nice there is that it does work kind of both in that streaming context or the batch context because again, we’re seeing new data come in and we’re updating our analyses. So doing a streaming analysis versus doing batch is basically just saying that you’re making high frequency commits rather than let’s say a commit per day or whatever it is. 

Logistically, there are no issues there. Operationally in a lot of the scenarios like you’re talking about like the web scenarios and other things, we have seen people that have a very different philosophy around what they want from Pachyderm. So we’ve seen some people in the web context that they’re really interested in Pachyderm for this pipelining piece and the orchestration and the scaling and they’re doing high velocity things. 

But they really don’t want to keep data around. And that might be because of privacy reasons. It might be because of whatever infrastructure they’re running on or whatever it is. 

But in those cases, a lot of times, people will keep records around for a certain period of time and then kind of purge those if they have privacy concerns. Other cases, we’ve seen people that maybe they have events happening really quickly like you’re saying, but really the processing they’re doing is not stream processing. They’re aggregating those things maybe once a day or once a week to do something. In those cases, we’ve seen people batch those events into daily or weekly or whatever commits in Pachyderm. And so, you have those daily, weekly snapshots that also triggered daily, weekly analyses. 

**Host:** So eventually, some hot and new no sequel technology is going to show up and I’m going to want to try it, and if I trust that their persistence layer isn’t really goofy where it kind of rewrites the entire archive for the slightest change to it, has some sort of partition quality to it if you will, can Pachyderm immediately be compatible with it or do I have to wait for it to become sort of context-aware of that new interesting technology? 

**Daniel:** No. Pachyderm is pretty much agnostic to those things. That being said, we have worked with users on specific types of connectors that we already have in place like people doing things with Postgres or other databases that we’ve worked with before. So those things we might have some existing connectors that would make things a little bit easier. But there’s nothing preventing working with the next no-sequel super fancy database.

The thoughts that would go into it is really what you want to get out of it. We have people doing things all the way from just snapshotting their database in Pachyderm to get that kind of time machine sort of quality all the way to streaming events into Pachyderm and then making atomic updates to tables or whatever it is. 

So question would really be around what you want to get out of it and then figuring out how to organize and orchestrate that interaction. 

**Host:** That time machine quality is really one of the biggest appeals to me personally. So perhaps my questions even undervalued some of the pipelining issues you start to mention, could we talk about some of the generally used cases there? 

**Daniel:** As I mentioned, the data pipelining piece in [Pachyderm is language agnostic](http://www.pachyderm.io). And I think this is a really important piece to emphasize in the context of data science and data engineering. Because a lot of the friction and problems and the data team come about because you’re developing a model and some cool stuff that you like working with on your laptop but then maybe you have to hand off your model to Java engineers or something to implement for your data infrastructure or you got data engineers working over here in Scala and then you got people from scientific backgrounds coming in and working even in MatLab or whatever it is. 

We believe that Pachyderm that when you’re doing – when you’re setting up one of these pipelines, you as a data scientist or data engineer should be able to write reasonably simple analyses in your language of choice and push those up to Pachyderm and pair those with stages that are built by other people and their language of choice or whatever fits so you could have a Java stage that feeds a Python stage and into R  - whatever it is. So you can set up these pipelines with the tooling that makes sense for the specific stages and you can scale those individual stages according to the needs of those stages. 

So I could have a Java stage that’s feeding some Python transformation using Pandas and then I could scale that Pandas stage of my pipeline over 10 workers individually and then have that feed into a specific data repository. 

So there is this setup of a language agnostic data pipeline and then also, there’s the idea that pipelining is very closely tied to the versioning. So as opposed to something like Airflow or Luigi which are definitely useful and I’m not arguing with that, but as opposed to those, distinguished from those is this fact that you have this orchestration and pipelining piece but that pipeline is continually kept in sync and up-to-date with the data that’s coming in. 

And as we’ve talked about before, it can be analyzed in terms of versioning and provenance to debug what went wrong in the past or incrementally improve on things and all of that. 

**Host:** How interesting. So is it correct to say that there’s some sort of pole or hub-sub going on where a pipeline knows what it works on and as soon as it sees that that data has changed, it kicks itself off and it does its steps and outputs the results wherever they need to go? 

**Daniel:** Exactly. So when you – in a simple example, let’s say that we’re doing a join of two data sets. We have a data repository A and a data repository B and then we have a Python script that uses Pandas to do the join. When we set up that pipeline, we would just create a very simple JSON specification that says, “Use this image, this Python image and run this Python script. Run that Python script on input from those two repositories, A and B.” 

So it’s going to listen on those two A and B repositories and when something is updated and one or the other one, that triggers that pipeline to run because something has changed. That’s recomputed and then output to an output repository that’s called a join repository. 

So yeah, it’s this idea that you have “input” to a pipeline or through a pipeline stage. And when that input is updated, that pipeline is updated as well. 

**Host:** And that JSON file you were describing is that a Pachyderm specific like a recipe language? 

**Daniel:** Yeah. It’s just a JSON specification that gives Pachyderm the things that it needs to know in order to set up the pipeline. So the image name that you’re running, what you want to run, what’s input. And then also this is where you specify, I mentioned you can distribute things over a certain number of workers, this is where you also specific parallelism. It’s not a very long JSON spec. It just specifies those things that you want to be run and how to run them. 

**Host:** And is there any under the hood optimization that might see, let’s say that join operation kicks off and before it completes, one or both of the repositories have had several other commits that may be it would be appropriate to cancel the current operation and resume on the most current or is that out of scope for what Pachyderm does? 

**Daniel:** Remember that on each commit, you’re only processing what’s new. So there is some optimization in terms of let’s say, in one of our examples, we do some edge detection on images and we commit image 1, image 2, image 3 and then the output is the corresponding edge detected images. Let’s say we commit image 1 and then it processes and detects the edges. And then we commit five more images, so images 2 through to 6. And then another job spun up to process those new five images. It doesn’t reprocess the first one. It just reprocesses the new five. 

And then if you commit two more images in, while the five are being processed, the previous five, a new job is spun up to process the incoming – the new ones, which are the new two, but it doesn’t reprocess the previous six. So it’s only this updating that’s happening. 

So really, you’re not spinning up jobs over and over and reprocess the same thing. 

**Host:** Got you. What about cases where let’s say I want to compute the mean and the median of those two tables? In the case of the mean, I guess if there was some cleverness going on, we could just maintain the sum and the count and get it really quick. But the median, it’s almost a little bit hopeless to think I can store some interim representation. I feel like I have to go get it again. What happens in situations like that? 

**Daniel:** In the most simple implementation, what you can do is play with a part of the specification that controls what parts of the repository and analysis will see. So when an analysis has spun up, basically, you mount that data that you put into your repository into the container that’s running the analysis. But you can either tell Pachyderm to say, “Only expose the new stuff to my analysis or expose everything in that repository.” 

So in a simple case, you could just say, “OK, regardless I’m going to expose everything to that median analysis to be able to understand the full scope of the data.” And then if you really wanted to distribute that and you had something where you had many different commits and you need to distribute that, Pachyderm is smart enough to distribute, let’s say, you have 10 workers to give a tenth of the data to each worker and then you could just have kind of a MapReduce style, reduce stage that would take the median from all those ten stages and find the overall. 

**Host:** In kind of wrapping up, I want to switch gears a little bit. And I’ll confess, I’m very ignorant to the Go language. It’s something I’ve never taken the time to gain an understanding or appreciation for. But I know you are an advocate for it and a contributor to the Go community, can you give us the pitch about why data scientists should consider Go for their work? 

**Daniel:** Yeah. And I can give you kind of how I came to it because I also didn’t start out – well actually, I started out in physics writing some Python along with Fortran and did Python in industry for a while. And really what I came down to is the fact that for a data science application, this is an application where we want people to make decisions based on the predictions that we make or based on the metrics that we calculate or whatever it is. 

The goal is to help people make decisions or help machines make decisions. When you have a breakdown in integrity in your application, this is like almost like game over for you. And I learned this very quickly because I would produce some prediction and I’d give it to people and then it would start behaving weirdly, right. 

If I go back and I look in my logs and I can’t figure out why it’s behaving weirdly and I don’t really know what’s going on, then those people that I’m hoping that will make decisions based on my application start to lose trust in that application. And I found that even if you fix your problems, you will likely never regain that trust. So you kind of just shot yourself in the foot. 

And for me, using this dynamically typed language of Python and just the convenience around it, that’s an amazing thing about Python is you can do things so conveniently. But at the same time, that kind of shoves some things under the rug. And Python will still run and it won’t necessarily give you a lot of information of about edge cases and like if all of a sudden you have 99% missing values in a column, it will still give you a maximum value for that column. And you will have really no insight into what happen underneath. 

Go, on the other hand, because it’s statistically typed and because it kind of necessitate you dealing with these sorts of integrity issues, it creates a scenario, where for me, I could still be productive as a data scientist because there is great tooling there and the language is very useful, I could still be very productive but I was also creating applications that were easy to deploy, easy to maintain, and maintain their integrity over time. And that’s really what I loved about Go.

In that regard, if anybody is interested in learning some data analysis or data science with Go, I would recommend that you check out the [gopherdatascience.org on GitHub](https://github.com/gopherds). There’s a repo called resources that will show you a bunch of the tooling that’s there in that ecosystem. There’s also Slack channel that’s pretty active. 

Pachyderm as well has [a Slack channel where you can come and ask questions](https://pachyderm-users.slack.com/shared_invite/MTQwMzA4OTU1NzY2LTE0ODY2ODk4NjUtMjNhMGRmM2NmZQ) and get debugging advice and that sort of thing. 

And yeah, I appreciate being here. It has been a great conversation. And I’ll be around at conferences this year so hope to meet some of the listeners and discuss a little bit about reproducibility. 

**Host:** Excellent, Daniel. I hope to bump into you at a conference as well. I’ll have all those links you just mentioned in the show notes. And any of the ones that you’ll give me in my last question here, can you once again remind us where we would go to get started or even just dip our toe into the Pachyderm ecosystem? 

**Daniel:** Yeah. So you can go to the website. That’s [Pachyderm.io](http://www.pachyderm.io/). And on that page, it will give you kind of a description of what Pachyderm is. And of course, Pachyderm is open source so it will link to our GitHub project where you can file issues and all that. It will also link to our documentation where you can go through the simple of getting started and local installation and see the examples. And there’s also a link to that Slack channel that I mentioned for questions. 

**Host:** Excellent. Well, Daniel, I want to thank you once again for coming on and sharing your insights. This has been a really cool episode. I’m actually excited about giving Pachyderm a try myself. 

**Daniel:** Great. Yeah. Hope it goes well and we definitely value feedback from the community. That’s what we’re looking for right now. I’m so excited to see all the things going on with it. 

**Host**: Thanks again to Periscope Data for sponsoring this episode. More about them at [PeriscopeData.com/Skeptics](www.periscopedata.com/skeptics). And that will be on the show notes as well. 

**Outro:** Data Skeptic is a listener-supported program. To support the show, visit [DataSkeptic.com](www.dataskeptic.com) and click on the membership tab.