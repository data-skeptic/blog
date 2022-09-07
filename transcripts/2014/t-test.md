**Kyle:** the data skeptic podcast is a weekly show featuring conversations about skepticism critical thinking and data scienceWell

**Linh Da:** welcome back to another mini episode of the data skeptic podcast I'm here as always with my wife and co host linda

**Kyle:** Hello Hello

**Linh Da:** how are you doing linda

**Kyle:** I am well Well

**Linh Da:** today our topic is the infamous T Test Are you familiar with this

**Kyle:** nope

**Linh Da:** Well it's one of the first test They'll teach you in any good statistics course and it's useful but it's not without its caveatsSo let's first talk about what it is and then we'll get into the assumptions one has to make in order to use it A T Test is useful in a couple of different situations and there's some nuances I won't necessarily get into But the basic idea is if you have two different sets of data and you'd like to know if they're essentially drawn from the same population The T Test will help you do thatFor example I noticed you've been reading this rather thick wine book here Can you talk about that for a minute

**Kyle:** It's a wine atlas

**Linh Da:** on atlas I'm sorry and what is the contents of the wine atlas

**Kyle:** It is all about wine I'm only on page 30 so I'm not sure what the rest of about I don't knowcheck the end how well

**Linh Da:** actually you're on page 25 so that's a 16 and two thirds margin of error But we'll overlook that if you count the indices pages which I always do it is precisely 400 pages

**Kyle:** yep So I think if you're asking me what it's about you should check back in a month

**Linh Da:** Alright maybe we'll do thatOne thing a wine grower might want to know is if a particular strand of grapes is especially sweet or not or maybe especially sour or not compared to some other vine of grapes because naturally there are well you tell me I would presume the winemakers have different goals

**Kyle:** I haven't gotten to that part I think their goals to make the wine taste good which can change depending on the season and the trends so I'm notsure what their goal is

**Linh Da:** So there's something there probably after I hear the word tannins used a lot something like that right As they're producing their grapes they'd like it to have not necessarily always high but in like a sweet spot of the right amount of whether it's sour nous or tannin or something naturally every grape will be a little bit different So if you have let's say two vines of grapes and you'd like to compare them and say are these vines producing essentiallythe same quality of grape Or is there a significant difference And that could just be an unknown difference Like one of the vines is just healthier than the other or it could be the result of an experiment like maybe one vine you're giving a little bit more water to and you're hoping it's going to improve the plant without over watering it So you'd like to kind of set some watering schedule and then evaluate if it's had a positive negative or no effecton the grapes that are produced How would you go about trying to test a hypothesis like that

**Kyle:** Well the reason I bought this wine book is because wine has a lot of variables So I don't know how an actual winery person would but most wine grapes grow in valleys the rate of whichthe water rushes through the soil is one factor if there's a water table underneath the depth of that is another factor The altitude as an average daytime nighttime Some high end vineyards make topological charts that depict this and then it's basically like very scientific So I mean obviously they would have to account forthe altitude the way the water runs all this stuff I don't even I can't even imagine And also which way the wind blows moisture the sun on that side of the hill Yeah I mean they would account for all these factors then I guess they would experiment because they would estimate that one hillside needs X amount of water and the other hillside needs a different amount of water They don't treat all the vines the same or they can but then they get different results So it just depends what they want

**Linh Da:** And I would imagine wine manufacturers are very smart about the science behind their product and they're doing a lot to control the agricultural variables you just described in giving the right amount of water the right amount of grapes but all for the goal of producing the best possible grapes that fit a very specific profile They're looking for certain vines in their vineyard will fit that exactly and others may diverge So one thing they probably want to do is test that every once in a while and sayis vine A producing grapes that are equivalent divine beat and if not they probably want to correct for it And the T test is a very powerful statistical tool that one might apply to answer a question like that You would say here is my data for Group A and my data for Group BAnd you want to test the hypothesis that these two populations of grapes are different from one another in a significant way Or the null hypothesis would be that the gray populations are equivalent If you can measure sweetness on some scale populations of grapes are not going to come out to exactly the same value it's not gonna be like there are 3.1 on the sweetness scale and the other is exactly 3.1 they're going to be like 3.11 and 3.13 some small variation or maybe a large variationIf the very students large you almost don't even need to do the test If it's small you'll definitely want to ask the question is this due to chance or is this a real phenomenon Now one important factor you have to keep in mind with the T Test is that it's based on the assumption that your data is normally distributed meaning it's drawn from the Gaussian distribution which I've mentioned before and will eventually do a mini episode all entitled to the Gaussian distribution alone But for the time beinglet's just call that the bell curve you know what the bell curve is

**Kyle:** Yes it's an upside down Ulike levels off at both ends like a squid

**Linh Da:** That's pretty good Yeah Um I will say that it's actually kind of inappropriate for me to call it the bell curve because there are other distributions that are also bell shaped but everyone kind of knows that idea And if you say bell curve it it's generally implied you're talking about the normal distribution Lots of things fit that shape I happen to know thatmany properties of grapes are normally distributed There are other things like people's blood pressure If you look at the blood pressure of entire population it's normally distributed Now what does all that mean If you plotted out it fits that shape of the bell curve The normal distribution there is a mean value the average and there's a standard deviation which is kind of how wide or tall the bell curve isand a normal distribution is always symmetrical you have as much to the left of the mean as to the right of the mean Now not all distributions have that symmetrical property For example weight in human beings is definitely not normally distributed It would be inappropriate to do a T Test on the general population of weight for human beings because it is not normally distributedAnd the T Test has that as a requirement what do you think about height Do you think it would be normally distributed that per gender would you expect height to be a bell curve

**Kyle:** I don't know but my guess is no

**Linh Da:** you're correct But actually most people guess yes And in fact lots of textbooks use height as an example of something that's normally distributed which if true would be convenient because everyone kind of gets an intuitive sense of human height and its natural variation Butthere's actually a great post I'm going to point people to and I think it's the our blogger site that gives some good explanations for why height is not normally distributed But lots of things are And there are also many tests you can apply to try and estimate whether or not your data is normally distributed I'm not going to get into those here because that's actually an episode in and of itself But assuming something is normally distributed is a lot like assuming a politician is honeston the surface many many politicians do look honest and in fact probably a lot of them are but it would not be fair to say just because they look honest and they seem to be honest that they are In fact honestThat was deserving of a laugh By the way

**Kyle:** Kyle's looking at me expecting me to laugh

**Linh Da:** There you go I'll just I'll just cut straight to that

**Kyle:** during the editYou guys at home don't feel the need to laugh

**Linh Da:** So there's another property I'll just mention that when you do a T Test there are a few different varieties of T Tests mainly around whether or not your samples are paired or not So if we look at our wine case the grapes from two vines don't necessarily match up to one another So that would be an unfair test But if let's say I don't know you wanted to test those power brand bracelets You know what I'm talking about that have the holograms and are supposed tomake athletes perform better I don't think they actually have magnets They have some sort of weird well supposedly you know quantum blah blah blah nonsense words holograms They sell them over at the Westfield mall

**Kyle:** Sometimes

**Linh Da:** if you wanted to test those you could have an athlete where a placebo power band bracelet and do whatever their athletic thing is let's say the long jump and then on another day you could have them wear the actual hologram braceletand compare the two data sets In that case it's paired because the same athlete is performing at both days So you can compare like with like and if you did that test you would find that those bracelets are absolutely bunk So how would you arrive at that conclusion You would run some tests You would make sure your data is normally distributed and then you would run a T Test to test the hypothesisDo you remember back when we did our P values episode

**Kyle:** so long ago but a little bit Yes

**Linh Da:** the output of your T Test would give you the P value which would help you determine if you want to accept the null hypothesis meaning assume thatthese bracelets have no efficacy or reject the null hypothesis meaning that perhaps there is some effect there Did you know T Tests are baked into Excel

**Kyle:** No but now that I know they exist that is so nifty

**Linh Da:** and you can apply them can't you

**Kyle:** know because I don't know how to apply them But that's awesome

**Linh Da:** I think the command and excel is equals T dot test depending on your version and then the parameters you give to that function are some range of data and then some range of data be and then whether or not it's Paratore impaired and it will kick out the answer for you The equivalent tests are also there on R And S P S S And sass and pretty much any statistical package and toolset available so you don't have to know thesort of arithmetic behind it

**Kyle:** So is the result like a number or percentage range What does it spit out

**Linh Da:** Good question It spits out a P value Often that p value is then wrapped up for you to tell you if you want to accept or reject the null hypothesis

**Kyle:** What's an example of a P value

**Linh Da:** Any number between zero and 1

**Kyle:** So

**Linh Da:** yeahEssentially I would more call it a probability It's the probability than any difference in the means of your two populations is due to chance Let's talk about our grapes if the sweetness of vine a on some arbitrary scale is 3.01And the sweetness on Vine B is 3.02 Those are different meansBut does it mean that the grapes on vine two are slightly sweeter It might an exceptionally small P value something less than your alpha So let's say less than 0.5 Then you would say the likelihood of this result of vine be being a little bit sweeter as a result of chance alone is highly unlikely If on the other hand your P value is quite largethan that saying the probability that this difference was simply due to chance is very likely and you would want to then assume that the null hypothesis is true that that difference you measured is just luck of the draw So the the T Test outputs the p value which will help you answer the question Do I trust the difference in these means to be a result of differences in the populationor are the populations for all intents and purposes equivalent

**Kyle:** So in your wine example you only gave one example grape A grape B Is that enough data

**Linh Da:** While I was saying Vine A&B Because you're right a single grape is not enough data you need a population of data points I'm assuming that if you have a vine you're you're picking off let's say 20 grapes or 30 grapes or however many grapes testing each oneand all the grapes on vine A Give you a mean value for acidity or sweetness or whatever you're testing and all the grapes on vine be give you the same

**Kyle:** thingand

**Linh Da:** then you're comparing those two means

**Kyle:** You're comparing two means and that's how you enter the data into excel

**Linh Da:** You enter all the data So if you tested 20 grapes on a vine and 29 b You would have 40 data points in two populations

**Kyle:** So then you enter all of it into Excel and then Excel automatically find the meanThen does the T Test then creates the p value

**Linh Da:** You got it

**Kyle:** You you told me how to do it in Excel So that makes me 20 times more likely to Lean on Excel for this

**Linh Da:** Alright good news Alright quick funding to wrapthis up I've actually been shortening things when I call it the T Test it's technically the student's T test because it's drawn from the student's T distribution It's named that because the original publisher published under a pseudonym the pseudonym was a period student a studentAnd the reason they used a student was because this work was all performed while in the employ of the Guinness Brewing company and the Guinness Brewing company was afraid that publishing this result might reveal too much to their competitors about how they go about doing all the various processes The statistician who came up with this test convinced his superiors to let him publish it anonymouslywith no specific references to Guinness or to whatever they were testing presumably how much hops is in the beer or something

**Kyle:** That's interesting because I just read an article that said creating breweries in multiple places and actually creating consistent brewsbeer in two separate locations is extremely difficult So no doubt this brewery person probably mastered it

**Linh Da:** Ha So what he mastered is how to measure and say if you are indeed producing the same beer in two locations or notand the T test is great for answering that question

**Kyle:** Yeah small breweries have a huge problem being consistent creating the bruise

**Linh Da:** Last but not least if anyone has any interesting questions that our data skeptic related please reach out on facebook or twitter share your question and maybe it will be the topic for an episode ormaybe we'll just respond directly But I would love to get some feedback I started getting a few emails these past couple of weeks with people That interesting questions that I've just been corresponding with and I think those conversations would be better served maybe in the facebook feed or something like that so everyone could share in the discussion My one restriction though Please do not send me your spreadsheet and ask me to fix it for youfraser question in I don't know 500 words or less without any attachments And we'll take it from there And also while we're at it including the show notes an example of how to run a T Test in both our and in excel So anyone who wants to be adventurous can get down and dirty themselves So thanks again for joining me linda Catch you next time

**Kyle:** Thanks for listening to the data skeptic podcast Show notes and more information are available at www dot data skeptic dot com You can follow the show on twitter at data skeptic If you enjoy the program please leave us a review on itunes or stitcher A review is the greatest way to show your support
