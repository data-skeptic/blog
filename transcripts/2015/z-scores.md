**Linh Da:** The Data Skeptic podcast is a weekly show featuring conversations about skepticism critical thinking and data science.

**Kyle:** So welcome to yet another episode of the data skeptic podcast mini-episodes. I'm here as always with my wife and co-host, Linh Da. 

**Linh Da:** Howdy! 

**Kyle:** Thanks for joining me as always Linh Da. So our topic for today is Z scores. Are you at all familiar with this?

**Linh Da:** Well you told me that would be the topic right?

**Kyle:** And I prepped you a little bit and Yoshi laughs. Well, a Z score, for those who are unfamiliar, also called the standard score relates to the bell curve which I prefer to call the Gaussian distribution. Do you know much about the bell curve, Linh Da?

**Linh Da:** Well, I think it's a way people is a common way that describes data I guess.

**Kyle:** Did you experience the bell curve while you were in college maybe?

**Linh Da:** I don't remember. But yeah I think anytime 

**Kyle:**  Grade on a curve?

**Linh Da:** Certain. Oh yeah, I think that was in high school actually. I did have some teachers that graded on a curve.

**Kyle:** So the common shape we call the bell curve. It isn't always actually. There are a couple of different types of bell curves but mostly more or less. And I'll just hand wave it for this episode. That's the shape we call the Gaussian distribution. And there's sort of a special case of the Gaussian distribution which actually isn't that much of a special case. It's just sort of a transformation of all Gaussian distributions. We call the normal distribution which is the case where there's a mean of zero and a standard deviation of one. But that's a little bit maybe too detail. Let's back up and just describe what the bell curve is. It has a mean which is the same as its median which is like the average case of where people are. And then it has a standard deviation which describes like how p kid that bell curve is. So if you think of something like how much sugar do you think is in like a snickers bar?

**Linh Da:** A lot. Probably like 20 g.

**Kyle:** 20 g. Okay now if you got 100 different snickers bars and you somehow had a way of measuring exactly the amount of sugar in each. Do you think they'd all have 20 or would have like 19 And some have 21 and so on and so forth?

**Linh Da:** They should be pretty.

**Kyle:** Close right. Very precise manufacturing process. But now on the other hand let's say you went into all the bakeries in town and you bought one chocolate chip cookie in each. How much sugar do you think would be in each of those chocolate chip cookies?

**Linh Da:** I don't know. 12 g?

**Kyle:** And do you think some would have 11 and some 13?

**Linh Da:** If they didn't stir evenly

**Kyle:** Sure. Well almost for sure because you're gonna go all these different bakeries, there's gonna be a much higher variance. They don't have the machine precise methodology that the mars corporation. Does I think mars makes knickers, right?

**Linh Da:** I don't know you should do your homework.

**Kyle:** I should have maybe. But yeah so when you have something less precise, there's more variance which means a wider standard deviation. So that's sort of the the two primary parameters that define the... Well actually those fully defined a standard normal distribution the mean and the variance. So mean being like where the center is and variants being how wide it is and the degree to which observations differ from the mean. That gets us very close to what a Z score is. The Z score is any given observation, how far it is from the mean of its population. So I thought maybe a good way to talk about this would be human height which actually I don't believe human height is normally distributed. But let's not get into that here let's just assume it is. And let's also assume that this random statistic I got on the internet which told me that the standard deviation is three inches is correct according to Wikipedia. And this part I trust in the US. For all people living in the US Ages, 20 and above males have an average height of 5 ft 9.5 inches females have an average height of 5 ft 4 inches. Does that sound about right to you? 

**Linh Da:** Yeah

**Kyle:** Okay and the standard deviation of 3 inches means that if you go out three inches in either direction from those two means, that accounts for about 68% of all the population. So rounded up just a little bit. Let's say 70% of people are three inches away from each of those means. Does that sound reasonable to you?

**Linh Da:** Yeah I mean what it tells me is that. I'm outside of that I'm 5 ft so I'm very short.

**Kyle:** Well you jump the gun. I was about to talk about the significant disparity in our heights. Seeing how is how this is a radio. Well, it's not radio, it's a podcast but an audio thing. We've never talked about height before so maybe you could share yours and I'll share mine.

**Linh Da:** I am five ft.

**Kyle:** and I am 6 7.

**Linh Da:** Really? No, you just lied!

**Kyle:**  No I'm I'm somewhere between I'm like 5 11 and a half. I could say six but I'll just play it cool. I'm 5 11 and half. So yeah we're about a foot difference. You are slightly below the mean and I'm slightly above. And thanks to your suggestion I actually set up a nice widget on [dataskeptic.com]([url](https://dataskeptic.com/blog/episodes/2015/z-scores)) website where anyone who wants to can go in and get their Z score. So let's put yours in Female. Standard deviations from 3 to 5 ft zero inches. You have a Z score of minus one in the third. And so your percentile is 9.1% basically. So you are taller than 9.1% of the female population.

**Linh Da:** I think that sounds about right I guess. It's very rare I'm taller than anyone.

**Kyle:** So you trust the numbers? ,I on the other hand, I will put in my 5 ft 11.5 inches. I have a Z score of 50.6 repeating two-thirds. So I am taller than 74.75% of the male population I don't really have an NBA career opportunity here but I'm vaguely on the taller-ish side. I'm still within one standard deviation though so that's where we get back to Z scores. Z scores are the number of standard deviations away from the mean that each of us lie. What was yours again?

**Linh Da:**  Mine was about nine or 10%.

**Kyle:** So you're Z score is minus 1.33. So you're a little bit more than one standard deviation but not quite two. I'm not quite one. So we're both sort of you know within the average expectation. There's an important thing here we should talk about called the 68/95/99.7 rule. And the reason you might want to memorize those numbers is those are the approximate amount of the population that lies within one standard deviation of the mean. So for one standard deviation which I'm a part of for the male height population, 68% of people are within that. 95% of people are within two standard deviations which includes you and 99.7% of people are within three standard deviations. So for example if you want to let's say just walk out on the sidewalk and how likely would it be that you meet a woman who is six ft tall or greater. She would be 2.66 repeating standard Z score. That many standard deviations away there's a little bit less than a 1% chance that that would happen. So as the score it just describes how far away from the mean and observation is. And this is really useful for when you are trying to assess the likelihood that a result was due to chance. Do you remember when we talked about particle fever the movie we went and saw?

**Linh Da:** What was the movie about?

**Kyle:** About the large Hadron collider.

**Linh Da:** Oh yes. So that was Kyle's movie choice So he remembers.

**Kyle:** You remembered too though on another podcast because you were like I remember them being so excited. They got five sigma.

**Linh Da:** Oh yeah yeah yeah. 

**Kyle:** So that that means that their result was... So the likelihood that their result was just like due to chance Studio coincidence was six nines and then a bunch of other numbers. So very very close to one very unlikely that it was just a random result.

**Linh Da:** So wait five sigma was five standard deviations away. So why don't they say five standard deviations away.

**Kyle:** Because I don't know Z scores sounds cooler I guess.

**Linh Da:** But they said sigma they didn't say Z score.

**Kyle:** Yeah well it's the same thing. So some of this comes from an almost antiquated concept that people probably won't talk about much in 100 years that it used to be. These calculations were really tricky to do before we had computers. So you'd have these big look up tables and you wouldn't actually compute something directly. You would transfer your answer to the standard normal distribution of mean, 0, standard deviation, 1. You'd look up the value in a look-up table and then you transfer it back. And that's kind of where Z scores come from is that everyone could agree that there was this one sort of standard model of the Gaussian distribution. But they're still useful like it's still helpful to say like how many standard deviations away from the means something is. And in particular in an upcoming episode next week, we will have a guest talking a lot about Z scores and in his context. He means how likely the result is due to chance or due to the alternate hypothesis that someone in this case cheated at something.

**Linh Da:** Good to know. 

**Kyle:** So what did you learn today, Linh Da?

**Linh Da:** That I am very short.

**Kyle:** And I am.

**Linh Da:** No, you're fine.

**Kyle:** You could have pushed up my ego and you didn't.

**Linh Da:** You said you were 6 ft first.

**Kyle:** Yeah well I'm almost if I wear good shoes.

**Linh Da:** I guess.

**Kyle:** Well, thanks again for joining me Linh Da.

**Linh Da:** Thank you.
