**Linda:** The Data Skeptic podcast is a weekly show featuring conversations about skepticism critical thinking and data science.

**Kyle:** Welcome back to another mini-episode of the data skeptic podcast. I'm here as always with my wife and co-host Linda.

**Linda:** Hello. Hello.

**Kyle:** How are you doing, Linda?

**Linda:** I am well.

**Kyle:** Today our topic is the infamous t-test. Are you familiar with this?

**Linda:** Nope

**Kyle:** Well it's one of the first-tests they'll teach you in any good statistics course and it's useful but it's not without its caveats. So let's first talk about what it is and then we'll get into the assumptions one has to make in order to use it. A t-test is useful in a couple of different situations and there's some nuances I won't necessarily get into. But the basic idea is if you have two different sets of data and you'd like to know if they're essentially drawn from the same population, the t-test will help you do that. For example, I noticed you've been reading this rather thick wine book here. Can you talk about that for a minute?

**Linda:** It's a Wine Atlas.

**Kyle:** On atlas I'm sorry. And what is the content of the wine atlas?

**Linda:** It is all about wine. I'm only on page 30 so I'm not sure what the rest of about I don't know.

**Kyle:** Actually you're on page 25 so that's a 16 and two-thirds margin of error. But we'll overlook that if you count the indices pages which I always do. It is precisely 400 pages.

**Linda:** Yep. So I think if you're asking me what it's about you should check back in a month.

**Kyle:** Alright maybe we'll do that. One thing a wine grower might want to know is if a particular strand of grapes is especially sweet or not or maybe especially sour or not compared to some other vine of grapes because naturally there are… well you tell me I would presume the winemakers have different goals.

**Linda:** I haven't gotten to that part I think their goal to make the wine taste good which can change depending on the season and the trends so I'm not sure what their goal is.

**Kyle:** So there's something there probably after I hear the word tannins used a lot something like that right. As they're producing their grapes they'd like it to have not necessarily always high but in like a sweet spot of the right amount of whether it's sour nous or tannin or something naturally every grape will be a little bit different. So if you have let's say two vines of grapes and you'd like to compare them and say are these vines producing essentially the same quality of grape. Or is there a significant difference and that could just be an unknown difference. Like one of the vines is just healthier than the other or it could be the result of an experiment like maybe one vine you're giving a little bit more water to and you're hoping it's going to improve the plant without over watering it. So you'd like to kind of set some watering schedule and then evaluate if it's had a positive negative or no effect on the grapes that are produced. How would you go about trying to test a hypothesis like that?

**Linda:** Well the reason I bought this wine book is because wine has a lot of variables. So I don't know how an actual winery person would but most wine grapes grow in valleys the rate of which the water rushes through the soil is one factor if there's a water table underneath the depth of that is another factor. The altitude as an average daytime nighttime. Some high end vineyards make topological charts that depict this and then it's basically like very scientific. So I mean obviously they would have to account for the altitude the way the water runs all this stuff. I can't even imagine. And also which way the wind blows moisture the sun on that side of the hill. Yeah I mean they would account for all these factors then I guess they would experiment because they would estimate that one hillside needs X amount of water and the other hillside needs a different amount of water. They don't treat all the vines the same or they can but then they get different results. So it just depends what they want.

**Kyle:** And I would imagine wine manufacturers are very smart about the science behind their product and they're doing a lot to control the agricultural variables you just described in giving the right amount of water the right amount of grapes but all for the goal of producing the best possible grapes that fit a very specific profile they're looking for. Certain vines in their vineyard will fit that exactly and others may diverge. So one thing they probably want to do is test that every once in a while and say is vine A producing grapes that are equivalent to vine B. And if not they probably want to correct for it. And the t-test is a very powerful statistical tool that one might apply to answer a question like that. You would say here is my data for Group A and my data for Group B. And you want to test the hypothesis that these two populations of grapes are different from one another in a significant way. Or the null hypothesis would be that the gray populations are equivalent. If you can measure sweetness on some scale, populations of grapes are not going to come out to exactly the same value. It's not gonna be like there are 3.1 on the sweetness scale and the other is exactly 3.1. They're going to be like 3.11 and 3.13. Some small variation or maybe a large variation. If the very students large you almost don't even need to do the test. If it's small you'll definitely want to ask the question is this due to chance or is this a real phenomenon. Now one important factor you have to keep in mind with the t-test is that it's based on the assumption that your data is normally distributed. Meaning it's drawn from the Gaussian distribution which I've mentioned before and will eventually do a mini episode all entitled to the Gaussian distribution alone. But for the time being, let's just call that the bell curve. You know what the bell curve is?

**Linda:** Yes it's an upside-down U. Like levels off at both ends like a squid.

**Kyle:** That's pretty good. Yeah,  I will say that it's actually kind of inappropriate for me to call it the bell curve because there are other distributions that are also bell-shaped. But everyone kind of knows that idea and if you say bell curve, it generally implied you're talking about the normal distribution. Lots of things fit that shape I happen to know that many properties of grapes are normally distributed. There are other things like people's blood pressure. If you look at the blood pressure of entire population it's normally distributed. Now what does all that mean? If you plotted out it fits that shape of the bell curve. The normal distribution there is a mean value the average and there's a standard deviation which is kind of how wide or tall the bell curve is. And a normal distribution is always symmetrical. You have as much to the left of the mean as to the right of the mean. Now not all distributions have that symmetrical property. For example weight in human beings is definitely not normally distributed. It would be inappropriate to dot-testest on the general population of weight for human beings because it is not normally distributed. And the t-test has that as a requirement. What do you think about height? Do you think it would be normally distributed that per gender would you expect height to be a bell curve?

**Linda:** I don't know but my guess is no.

**Kyle:** you're correct But actually most people guess yes. And in fact lots of textbooks use height as an example of something that's normally distributed which if true would be convenient because everyone kind of gets an intuitive sense of human height and its natural variation. But there's actually a great post I'm going to point people to and I think it's our blogger site that gives some good explanations for why height is not normally distributed. But lots of things are and there are also many tests you can apply to try and estimate whether or not your data is normally distributed. I'm not going to get into those here because that's actually an episode in and of itself. But assuming something is normally distributed is a lot like assuming a politician is honest. On the surface, many politicians do look honest and in fact probably a lot of them are but it would not be fair to say just because they look honest and they seem to be honest that they are In fact honest. That was deserving of a laugh, by the way.

**Kyle:** So there's another property I'll just mention that when you do a t-test. There are a few different varieties of t-tests mainly around whether or not your samples are paired or not. So if we look at our wine case the grapes from two vines don't necessarily match up to one another. So that would be an unfair test. But if let's say I don't know you wanted to test those power brand bracelets. You know what I'm talking about that have the holograms and are supposed to make athletes perform better. I don't think they actually have magnets. They have some sort of weird well supposedly you know quantum blah blah blah nonsense words holograms. They sell them over at the Westfield mall sometimes.

**Kyle:** If you wanted to test those you could have an athlete where a placebo power band bracelet and do whatever their athletic thing is let's say the long jump. And then on another day you could have them wear the actual hologram bracelet and compare the two data sets. In that case, it's paired because the same athlete is performing at both days. So you can compare like with like. And if you did that-test you would find that those bracelets are absolutely bunk. So how would you arrive at that conclusion. You would run some tests. You would make sure your data is normally distributed and then you would run a t-test to test the hypothesis. Do you remember back when we did our P-values episode?

**Linda:** So long ago but a little but yes.

**Kyle:** The output of your t-test would give you the p-value which would help you determine if you want to accept the null hypothesis meaning assume that these bracelets have no efficacy or reject the null hypothesis meaning that perhaps there is some effect there. Did you know t-tests are baked into Excel?

**Linda:** No but now that I know they exist that is so nifty

**Kyle:** And you can apply them can't you?

**Linda:** No, because I don't know how to apply them. But that's awesome.

**Kyle:** I think the command and excel is equals T.test depending on your version. And then the parameters you give to that function are some range of data and then some range of data be and then whether or not it's paired or unpaired and it will kick out the answer for you. The equivalent-tests are also there on R, SPSS, and SASS and pretty much any statistical package and toolset available. So you don't have to know the sort of arithmetic behind it.

**Linda:** So is the result like a number, percentage, or range? What does it spit out?

**Kyle:** Good question. It spits out a p-value. Often that p-value is then wrapped up for you to tell you if you want to accept or reject the null hypothesis.

**Linda:** What's an example of a p-value?

**Kyle:** Any number between 0 and 1.

**Kyle:** Essentially, I would more call it a probability. It's the probability than any difference in the means of your two populations is due to chance. Let's talk about our grapes. If the sweetness of vine a on some arbitrary scale is 3.01 and the sweetness on Vine B is 3.02. Those are different means. But does it mean that the grapes on vine two are slightly sweeter. It might. An exceptionally small p-value. Something less than your alpha So let's say less than 0.5. Then you would say the likelihood of this result of vine be being a little bit sweeter as a result of chance alone is highly unlikely. If, on the other hand, your p-value is quite large than that saying the probability that this difference was simply due to chance is very likely and you would want to then assume that the null hypothesis is true that that difference you measured is just luck of the draw. So the the t-test outputs the p-value which will help you answer the question, do I trust the difference in these means to be a result of differences in the population or are the populations for all intents and purposes equivalent?

**Linda:** So in your wine example you only gave one example grape A grape B. Is that enough data?

**Kyle:** While I was saying Vine A and B. Because you're right. A single grape is not enough data. You need a population of data points I'm assuming that if you have a vine you're you're picking off let's say 20 grapes or 30 grapes or however many grapes testing each one. And all the grapes on vine A give you a mean value for acidity or sweetness or whatever you're testing. And all the grapes on vine be give you the same thing. And then you're comparing those two means.

**Linda:** So you're comparing two means and that's how you enter the data into excel.

**Kyle:** You enter all the data. So if you tested 20 grapes on a vine and 20 in B, you would have 40 data points in two populations.

**Linda:** So then you enter all of it into Excel and then Excel automatically find the mean. Then does the t-test, then creates the p-value.

**Kyle:** You got it.

**Linda:** You you told me how to do it in Excel. So that makes me 20 times more likely to lean on Excel for this.

**Kyle:** Alright good news. Alright quick fun thing to wrap this up. I've actually been shortening things when I call it the t-test it's technically the student's t-test because it's drawn from the student's t-distribution. It's named that because the original publisher published under a pseudonym. The pseudonym was a.student. And the reason they used a student was because this work was all performed while in the employ of the Guinness Brewing company and the Guinness Brewing company was afraid that publishing this result might reveal too much to their competitors about how they go about doing all the various processes. The statistician who came up with this test convinced his superiors to let him publish it anonymously with no specific references to Guinness or to whatever they were testing presumably how much hops is in the beer or something.

**Linda:** That's interesting because I just read an article that said creating breweries in multiple places and actually creating consistent brews beer in two separate locations is extremely difficult. So no doubt this brewery person probably mastered it.

**Kyle:** Yea. So what he mastered is how to measure and say if you are indeed producing the same beer in two locations or not. And the t-test is great for answering that question.

**Linda:** Yeah small breweries have a huge problem being consistent creating the brews.

**Kyle:** Last but not least. If anyone has any interesting questions that are Data Skeptic related, please reach out on Facebook or Twitter. Share your question and maybe it will be the topic for an episode or maybe we'll just respond directly. But I would love to get some feedback. I started getting a few emails these past couple of weeks with people that interesting questions that I've just been corresponding with and I think those conversations would be better served maybe in the Facebook feed or something like that. So everyone could share in the discussion. My one restriction though, please do not send me your spreadsheet and ask me to fix it for you. Phrase your question in I don't know 500 words or less without any attachments. And we'll take it from there. And also while we're at it, we are including our show notes with an example of how to run a t-test in both R and in excel so anyone who wants to be adventurous can get down and dirty themselves. So thanks again for joining me Linda. Catch you next time.

**Linda:** Thanks for listening to the Data Skeptic podcast. Show notes and more information are available at www.dataskeptic.com. You can follow the show on Twitter @dataskeptic. If you enjoy the program please leave us a review on iTunes or stitcher. A review is the greatest way to show your support.
