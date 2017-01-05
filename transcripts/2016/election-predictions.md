## Election Prediction

**INTRO VOICE-OVER**: Data Skeptic features interviews with experts on topics related to data science, all through the eye of scientific skepticism.

**HOST**: [Jo Hardin](http://research.pomona.edu/johardin/) has a PhD in statistics from UC Davis and is presently a Professor of Mathematics at Pomona College. Her work contributes to diverse topics such as computational biology and genomics. She recently wrote a blog post about the prediction competition for the US 2016 presidential election, giving some tips for competing, and with the election coming up, I thought it would be a great time to talk about how data scientists can study the election process.

Jo, welcome to Data Skeptic.

**JO**: Thanks! Great to be here.

**HOST**: Before we jump into the details and election discussion, could you tell us what the [ASA](http://www.amstat.org/) is and what your particular association is to it?

**JO**: The ASA is the American Statistical Association and I’m involved – I have a couple of roles. I work closely with the statistics education section and their outreach to students of all different kinds. I also work locally with my chapter in Southern California.

**HOST**: What can you tell me about the [ASA’s Prediction Competition](http://thisisstatistics.org/wp-content/uploads/2016/07/2016_ElectionPredictionContest_DetailedRules_2016-0718.pdf)?

**JO**: I think it’s just a way that the ASA came up with to really get students excited and involved with how you can use statistics to think about what’s going on in the news and really kind of current events. The prediction competition is pretty straightforward. It’s simply to predict both the winning presidential candidate as well as the final percentages of the popular vote for each major candidate and I think they want it also – if you can also do it per state and then broken down by demographic groups and what not.

They want a thoughtful answer. They’ve asked for a 200 to 300-word description of the methods and what you did that was original. They’re not really looking for you to just report what Nate Silver has predicted.

But it’s kind of a fun thing and you can work in groups and there’s a $200 cash prize and an opportunity to write it up as a blog, whatever it is that you come up with.

**HOST**: Oh, very cool. When I first read this headline, I started out slightly cynical, thinking, well, realistically in the United States, one of the two major parties wins. You know, no offense to third party candidates. Best of luck to everyone. But it’s sort of a binary outcome in our country. So if it’s a coin toss, I’ve got a 50-50 shot of making a correct random guess. But how do those added features they’re looking for make it a much more interesting and difficult challenge?

**JO**: Well, I think the challenge is sort of twofold. Obviously, we’re going to be looking for more than just a binary response. But in terms of predictions, the two pieces that are so important are what *data do you use* and *what methods do you use*. So there are lots of ways to contribute on those two different fronts and ways to talk about your choices. As most of your listeners will know, there are lots of polling organizations out there and every time they come out with a new poll, it’s slightly different from their neighbor polling organization. Kind of thinking about which polls you’re going to use and how you’re going to combine those results and I think there’s a lot of interesting ideas, creative ways to look at the problem.

**HOST**: Absolutely. I really like your distinction that there’s data and there’s methods. They’re two separate and important things. Maybe we should start with the data. Can you tell me about some of [the sources you identified in your blog post](https://www.r-bloggers.com/presidential-election-predictions-2016-an-asa-competition/) and what differs across them?

**JO**: I give a couple of different places that you can find data, that – poll aggregators. So they’ve taken polls from lots of different sources. I actually use the [data from FiveThirtyEight](http://projects.fivethirtyeight.com/2016-election-forecast/). To be honest, the main reason I use that particular data is because I could scrape the data in a reproducible way. I wrote some code that would allow me to run the code over and over, so that every time there’s a new poll posted, I get a new set of data.

I think that the majority of the base data that goes into these poll aggregators – so Huffington Post or RealClearPolitics or Gallup – they’re using a lot of the same polls. But what differs is how they weigh the polls. Some of them will make choices on – not to use a particular poll if it comes from a really liberal polling organization or a conservative polling organization.

Just today, I was looking and [Daily Kos](http://www.dailykos.com/) says – I don’t know if I’ve said that right. Daily Kos, says that Hillary Clinton has a 72 percent chance of winning and Nate Silver of FiveThirtyEight says Hillary Clinton has a 67.6 percent chance of winning. So you’re definitely going to get some differences across these different poll aggregators.

**HOST**: So you zoned in on FiveThirtyEight as a data source. Now that data isn’t just delivered to you in a nice package on your doorstep, there are some steps to get it. Could you talk about the code you wrote for the scraping and analysis and some of the challenges in putting that together?

**JO**: So one of the big challenges that I had is that when you go on to the FiveThirtyEight site, there’s an XML page that just pops up at you and that was actually pretty straightforward for me just using the XML package and R. I should say that, that I did all of my work using RStudio. But the problem was that I only got the top 10 posts, or the top 10 polls rather. I wanted more information than that. I thought, OK, if I’m going to be predicting this, I want to go out, go back farther into the poll history and kind of see what the trends have been. I was interested in doing some visualizations and what not. 

If you are on the website, you simply click a button and you get, I don’t know how many, 40 or 50 different polls that will show up. So that caused me to really kind of delve into Stack Exchange and reaching out to friends I have who are more expert in this. I ended up using both RCurl and ReadR, which are additional packages, R packages to read HTTP files, HTML files.

But then the key was that the data I ended up downloading into R was JSON and if any of you have worked with JSON files, they’re like lists of lists. So they’re just these nested pieces of information. So there was a reasonable amount of data manipulating to work through that. I’ve documented all that in the code that I posted on GitHub.

**HOST**: Oh, that’s great. I will put a link to your [GitHub repository](https://github.com/hardin47/prediction2016/blob/master/predblog.Rmd) in the show notes for anyone that wants to check that out. What would it take for someone to use your code to kick start their own analysis, leveraging FiveThirtyEight data?

**JO**: So if they want to use the FiveThirtyEight feed that gets updated daily, they can just re-run my code really straightforward. Literally, I’ve written an R Markdown file and the R Markdown file is posted on GitHub. So I’ve written – the first half of the R Markdown file is scraping the data and getting it into tidy format. If they just kind of start halfway through, the data are in tidy format, which means they’ve got variables as the columns and then the polls are the rows. They can just go from there.

**HOST**: Well, that’s great. That would be a big time saver for some of the participants in this competition. So if I were to grab that, perhaps it’s time to get some of the methods. You did some initial analysis independent of your own political perspective, which you’re free to share or not, however you choose. But what did the data tell you when you did the initial run-through of it?

**JO**: One of the things I was surprised by – and maybe it’s because I haven’t been following along as closely as some people – but I was surprised that Trump has virtually never had a lead over Clinton. When you’re aggregating these polls and kind of thinking about weighted averages and trends and telling things as they go along, I was surprised at how consistent they’ve been over time.

From my statistical perspective, as a statistician, the thing I think about every day is variability. So for me, believing that there’s this baseline of Clinton having possibly a four-point lead, then I would exactly expect that some polls should show them tied and other polls should show Clinton ahead by eight points. That’s just the nature of variability and so, that to me says consistency whereas to other people, a swing from zero to eight might seem like extra variability.

**HOST**: So from a purely statistical sampling and inferencing approach, it seems like when we look at polls, they’re trying to answer the question, “Who is America’s current favorite candidate?” Yet this is not necessarily the same question as, “Who will win the upcoming election?” Why not?

**JO**: I mean when you ask who America likes, you have to think about who America is. Who’s going to win the upcoming election depends on the individuals who go to vote on Election Day. Polling organizations try very hard to figure out who those people are. It has to do of course with people who are allowed to vote. There are lots of ways that individuals are sort of disenfranchised in terms of their voting. We know about some. Like, if you’re under 18 or if you’re a felon, those are people you know about.

But other things that people may not know about are that voter rolls sometimes get purged. So kind of cleaned up and reasons might be because you’ve moved. So they go in and they look and see who has moved recently and those people are required to reregister to vote. Sometimes they get purged and I’m not exactly sure about all the legalities of all this. But sometimes they get purged simply because people haven’t voted in a number of elections.

So if you haven’t voted in some number of years – and I feel like I was reading some articles that that just happened recently in Ohio, that people who haven’t voted in the last, I don’t know, three or four elections, are possibly – are being purged from those voter rolls.

So really we want to know not just when I randomly digit dial someone who they like as a candidate. But I also really need to know who is going to vote. Are you going to show up on Election Day?

**HOST**: So in your analysis, you chose to do a weighted average. I think the idea of weighting a set of independent sources is pretty uncontroversial. But perhaps the one matter of difference of opinion could be the way in which you choose to weight them. What did you use and why did you choose that method?

**JO**: I was just kind of playing around with what I sort of think about when I’m looking at these polls. I think how long ago was that poll. How many individuals did they survey? What does FiveThirtyEight think? Because the data that I scraped from FiveThirtyEight actually reports the weight associated with the poll. I’m not sure that my weights in particular are particularly scientific. But it is important to know that some of these polling organizations have particular leanings. The way that those leanings get manifested in the outcomes of the polls have to do with how the question is worded or what the order of the question is.

You know, if you ask about particular political events and then you ask which candidate they’re going to vote for, for president, that can really impact that response. So I think these poll aggregators know a lot more about those particular nuances. But I also think they take into account those standard things. For example, how long ago was it? Has political opinion changed over time? How many individuals are being sampled?

**HOST**: So doing any sort of polling opens up an opportunity for us to have a statistical discussion about how it was sampled. In a perfect world, obviously we’re doing the equivalent of pulling colored balls out of urns in an independent and identically-distributed fashion. But we don’t necessarily have that pure access for a lot of reasons. You’ve given a bunch of them already like people who are able to vote and will show up at the polls on the right day.

I think it’s difficult to take a measurement. What do you think the chances are we’re able to actually measure something close to ground truth value?

**JO**: I think another thing that I haven’t talked about yet which really has to do with this measuring question you’re talking about is how we’re getting in touch with people. Thirty years ago, everybody had a landline and there were pretty standard ways of doing random digit dialing where you were really getting a good representative sample of the US population. Then you could easily ask things like, “Did you vote in the last election?” or “Did you vote in the last presidential election?” and that was a way to gauge whether that person was likely to vote in the upcoming election.

But now, I want to say like 20 percent to 25 percent of people don’t even have a landline. I have a landline, but I almost never answer it, right? So the number of individuals who can be contacted or really the type of individual who can be contacted via a landline is really changing how we’re measuring things.

So there are all sorts of different ways of measuring. There are also internet panels, so people who sign up to be asked questions on a regular basis. Those are a cross-section of the United States and we’re trying to get a representative view, but making sure that – as I was saying with cell phones, obviously the majority of people who have cell-phone-only homes are going to be young people and obviously, young people have different political interests than baby boomers.

**HOST**: True, yeah. So there’s a strong correlation there that we’re going to get a sampling bias from – if we’re only counting opinions of the people who answer landline calls. But can we correct for that? Is there perhaps a small population of young people with landlines and we can oversample or something like that? Is it hopeless or is there something we can do methodologically?

**JO**: I do think we understand some of those demographic categories. A lot of these polling organizations weight based on exactly race, age, education. You can oversample from particular geographic areas to get those internet polls/internet panels. Sometimes those are arrived at through randomly sampling addresses, right? Literal home addresses. Home addresses are something that we definitely understand demographics of, right? We understand towns and what their racial breakdowns are and their education breakdown.

**HOST**: So there are a lot of ways we can go at this. I’m really intrigued by that one of picking addresses because you can really, well, control and hopefully go knock on doors enough times that you get a response. That compared to internet panels where there are very different methods for coming up with the data. Is there any statistical reason why we should say there’s a preferred data collection process or is it all pros and cons?

**JO**: I think you have to use all of them, right? If you think about your nephew and your grandmother, there’s no possible way for you to get information from both of those demographic groups using one method. So I really think that any polling organization that’s going to have accurate information is going to be combining results from lots of different methods. I think they all have pros and cons and I guess I would boil it down to the pros to all of them is that they reach a particular demographic and the cons to all of them are they don’t reach a particular demographic.

**HOST**: You had also mentioned online polling, which is something I happen to know a little bit about. A technique that is used sometimes in the online polling space is to set some nice strata for yourself on I guess some sociological analysis and things like that and say that we need people of these particular criteria and these quantities. As those buckets fill up, you’re getting them. But one bucket gets full. You start turning people away essentially saying, “We’re not interested in your opinion because we already have enough people that look, talk, walk and act like you.” What’s the statistician’s perspective on turning people away like that versus trying to balance later?

**JO**: My instinct is to say that you have to really think about which one is going to bias your answers more strongly. So if you’re really aggressively trying to get people, that to me says that there’s something sort of different about the people that you’re getting than that you’re not getting.

But again, I’m sure there’s so much that goes into it. It’s not just the demographics but it’s also the psychology of an individual who wants to answer a poll versus the psychology of an individual who doesn’t want to answer a poll. 

So really that’s I think where the analyst needs to be careful. It’s just thinking carefully about how am I going to bias my answer – my polling. And I want to do that as minimal as possible.

**HOST**: So I see a lot of polls. The good ones at least in my opinion will report a margin of error around them. Yet as far as I know, that margin of error is arrived out of some set of methodological assumptions that aren’t often stated. Maybe they just take some simple confidence intervals. We don’t know that they check the underlying assumptions. These sorts of concerns can come up. How do you as a statistician interpret the margin of error in a public forum, like on a news broadcast?

**JO**: First of all, before I answer that question directly, I think again 30 years ago, when the majority of polling information came straight from random digit dialing, I think the margin of error was almost purely based on the sample size. That really makes sense from a statistical point of view. If you’re randomly sampling, then the only thing that matters is how big a sample.

You don’t need a huge sample. A thousand people will get you a margin of error of three percent. Nowadays, because we’re combining methods and it’s just a lot more complicated with weights and what not, those margin of errors have more sophisticated formulas going into them.

But I think that there has been a lot of thought and I don’t really question the margin of error in terms of how it has been calculated. Now in terms of what it *means*, what I think when I see one individual poll with a margin of error of let’s say three percent, I’m thinking to myself, “OK. Well, if I look at 100 different polls, 95 percent of those polls are going to capture the ground truth and 5 percent of the polls are not going to capture the ground truth.”

If I’m only looking at one poll, I’m an optimistic person I tend to think. OK. Well, the ground truth, whatever that means for today, is within that margin of error. So if it’s 52 percent, plus or minus 3 percent, then OK, well 49 is in that margin of error. So it could go to the other candidate. 

It also helps me understand when I see an extreme poll that we’re looking at so many polls every day in this election season, that it makes sense that we would see some extreme polls here and there.

**HOST**: That ties it actually to one of the later stage questions I wanted to ask you about. As I was doing some background research for this episode, I noticed you’ve done a lot of work in areas that are very familiar to the Data Skeptic audience, things like [clustering and outlier detection](https://en.wikipedia.org/wiki/Anomaly_detection).

In particular, I noticed you’re doing some work on false discovery rates, which in my opinion is an undervalued aspect of statistics. Could you talk a bit about how we might think of false discovery rates in the context of the election predictions?

**JO**: They’re related but different. So when we’re trying to do inference, we’re interested in what’s going on with the population. I often, when I’m teaching courses and what not, talk about two different pieces of inference. One is hypothesis testing, where I have a very specific question that I’m trying to ask and one is interval estimation, so confidence intervals and prediction intervals. 

False discovery rates come about through hypothesis testing where I’m making a decision. I’m deciding to reject a particular null hypothesis or to not reject that particular hypothesis.

So a false discovery rate is [how often I get a data set that I think is a positive](https://en.wikipedia.org/wiki/False_discovery_rate), but is really only noise. With estimation, you don’t have quite that same idea because I’m not really making a decision about, “Is candidate X going to get 50 percent of the election?” Instead what I’m saying is, “What is the percentage?”

So that estimation is slightly different because I don’t have a yes/no vote. So it’s not quite the same context.

**HOST**: Makes sense. So winding up, when we were talking earlier about better methodology or better data being the right step, what do you think is more important in coming up with a really accurate election prediction?

**JO**: I think that being simple, creative and thoughtful are really the keys to a competition like this. It’s hard for me to believe that a really fancy theoretical model is going to predict much better than a thoughtful nuanced model. So I sort of believe that the person who’s going to win this competition is going to be someone who understands the nuances of the political system and the different polls and has thought carefully about how to combine them in creative ways.

**HOST**: I think that’s some good advice. There’s a lot more [good advice in your blog posts](https://www.r-bloggers.com/presidential-election-predictions-2016-an-asa-competition/) and I will remind everyone that that will be linked to in the show notes as well as [your GitHub repo](https://github.com/hardin47/prediction2016/blob/master/predblog.Rmd) where they can check out your code and perhaps leverage some of that in the competition. Any final words of wisdom for people that want to take on this challenge?

**JO**: I would implore everyone to go vote. If you don’t know if you’re registered to vote, just go to Google and type “How can I vote?” and Google will actually tell you whether or not you are already registered to vote.

**HOST**: Oh, that’s super cool. I didn’t know that. I hope everyone does that. Jo, this has been really interesting. Thank you so much for coming on and sharing your thoughts with us.

**JO**: Great. Thanks so much for having me Kyle.

**HOST**: Take care.

**JO**: Uh-huh. Bye.

**HOST**: So one quick final detail before we sign off. If anyone listening is actually going to participate in the ASA competition, I would like to hear your story. Share it on [the show’s Facebook page](https://www.facebook.com/dataskeptic/). I think that’s the best spot because you can kind of post a longer thing there. You can also tweet at me. Maybe you blogged about it, something like that. I’m really interested in following what goes on with this. If there’s a good number of listeners participating, perhaps we will do a follow-up show about it. So if you’re at all interested in this, I think it’s a cool opportunity to work on a real world problem. Maybe get some feedback on your work. So let me know if you’re going to join and until next time, I want to remind everyone to keep thinking skeptically of and with data.

**EXIT VOICE-OVER**: For more on this episode, visit [www.DataSkeptic.com](www.DataSkeptic.com). If you enjoyed the show, please give us a review on [iTunes](https://itunes.apple.com/us/podcast/data-skeptic/id890348705?mt=2) or [Stitcher](http://www.stitcher.com/podcast/data-skeptic-podcast/the-data-skeptic-podcast).