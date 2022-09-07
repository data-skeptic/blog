**Linh Da:** The data skeptic podcast is a weekly show featuring conversations about skepticism critical thinking and data science So

**Kyle:** welcome to yet another episode of the data skeptic podcast Many episodes I'm here as always with my wife and co host linda howdy Thanks for joining me as always lindaSo our topic for today is Z scores Are you at all familiar with this

**Linh Da:** Uh Well you told me that would be the topic right

**Kyle:** And I prepped you a little bitand Yoshi laughs well a Z score for those who are unfamiliar also called the standard score relates to the bell curve which I prefer to call the Gaussian distribution Do you know much about the bell curve linda

**Linh Da:** Well I think it's um away people is a common way that describes data I guess

**Kyle:** Did you experience the bell curve while you were in college maybe

**Linh Da:** UmI don't remember But yeah I think anytime grade on a curve certain Oh yeah I think that was in high school actually I did have some teachers that graded on a curve So

**Kyle:** the common shape we call the bell curve it isn't always actually there's a couple of different types of bell curves but mostly more or less And I'll just hand wave it for this episode That's the shape we call the Gaussian distributionAnd there's sort of a special case of the Gaussian distribution which actually isn't that much of a special case It's just sort of a a transformation of all Gaussian distributions we call the normal distribution which is the case where there's a mean of zero and a standard deviation of one but that's a little bit maybe to detail let's back up and just describe what the bell curve is It has a mean which is the same as its median which is like the average case of where people areand then it has a standard deviation which describes like how p kid that bell curve is So if you think of something like um how much sugar do you think is in like a snickers

**Linh Da:** bar A lot Probably like20 g

**Kyle:** 20 g Okay now if you got 100 different snickers bars and you somehow had a way of measuring exactly the amount of sugar in each do you think they'd all have 20 or would have like 19 And some have 21 and so on and so forth

**Linh Da:** They should be pretty

**Kyle:** close right very precise manufacturing process But now on the other hand let's sayyou went into all the bakeries in town and you bought one chocolate chip cookie in each How much sugar do you think would be in each of those chocolate chip cookies

**Linh Da:** I don't know 12 g

**Kyle:** And do you think some would have 11 and some 13

**Linh Da:** if they didn't stir evenly

**Kyle:** Sure Well almost for sure because you're gonna go all these different bakeries there's gonna be a much higher variance They don't have the machine precise methodology that the mars corporation does I think mars makes knickers right

**Linh Da:** I don't know you should do your homework

**Kyle:** I should have maybe But yeah so when you have something less precise there's more variance which means a wider standard deviationSo that's sort of the the two primary parameters that define the gut Well actually those fully defined a standard normal distribution the mean and the variance So mean being like where the center is and variants being how wide it is and how much howthe degree to which observations differ from the mean that gets us very close to what a Z score is The Z score is any given observation how far it is from the mean of its population So I thought maybe a good way to talk about this would be human height which actually I don't believe human height is normally distributedUm but let's not get into that here let's just assume it is And let's also assume that this random statistic I got on the internet which told me that the standard deviation is three inches is correct according to Wikipedia And this part I trust in the U S For all people living in the U S Ages 20 and abovemales have an average height of five ft 9.5 inches females have an average height of five ft four inches Does that sound about right to you Okay And the standard deviation of three inches means that if you go out three inches either direction from those two means that accounts for about 68% of all the population sorounded up just a little bit let's say 70 70% of people are three inches away from each of those means that's not reasonable You

**Linh Da:** Yeah I mean what it tells me is that I'm outside of that I'm five ft so I'm very short

**Kyle:** Well you jump the gun I was about to talk about the significant disparity in our heights Seeing how is how this is a radio Well it's not radio it's a podcast but an audio thingWe've never talked about height before four so maybe you could share yours and I'll share mine

**Linh Da:** I am five ft

**Kyle:** and I am 6 7 So it's really

**Linh Da:** no you just

**Kyle:** lie No I'm I'm somewhere between I'm like 5 11.5 I could I could say six but I'll just play it cool I'm 5 11.5 so yeah we're about a foot differenceYou are slightly below the mean and I'm slightly above And thanks to your suggestion I actually set up a nice widget on data skeptic dot com website where anyone who wants to can go in and get their Z score So let's put yours in Female uh standard deviations from 235 ft zero inches you have a Z score of minus one in the third And so your percentile is 9.1% basically SoYou are taller than 9.1% of the female population

**Linh Da:** I think that sounds about right I guess it's very rare I'm taller than anyone So

**Kyle:** you trust the numbers I on the other hand I will put in my five ft 11.5 inches I have a Z score of 50.6 repeating two thirds so I am taller than 74.75% of the male population I don't really have an M B a career opportunity here butI'm vaguely on the taller ish side I'm within I'm still within one standard deviation though so that's where we get back to Z scores Z scores are the number of standard deviations away from the the mean that each of us lie what was yours

**Linh Da:** Again Mine was about nine or 10%

**Kyle:** So you're Z score is minus 1.33 so you're a little bit more than one standard deviation but not quite twoI'm not quite one So we're both sort of you know within the average expectation there's an important thing here We should talk about called the 68 95 99.7 rule and the reason you might want to memorize those numbers is those are the approximate amount of the population that lies within one standard deviation of the means So for one standard deviation which I'm a part of for the male height population68% of people are within that 95% of people are within two standard deviations which includes you and 99.7% of people are within three standard deviations So for example if you want to let's say just walk out on the sidewalk and how likely would it be that you meet a woman who is six ft tall or greater She would be 2.66 repeating standard Z scoreThat many standard deviations away there's a little bit less than a 1% chance that that would happen So as the score it just describes how far away from the mean and observation is and this is really useful for when you are trying to assess the likelihood that a result was due to chanceDo you remember when we talked about particle fever the movie we went and

**Linh Da:** saw what was the movie about

**Kyle:** about the large Hadron collider

**Linh Da:** Oh yes so that was Kyle's movie choice So he remembers

**Kyle:** you remembered too though on another podcast because you were like I remember them being so excited They got five sigmaOh yeah yeah yeah so that that means that their result was So the likelihood that their result was just like due to chance Studio coincidence was six nines and then a bunch of other numbers so very very close to one very unlikely that it was just a random result

**Linh Da:** So wait five sigma was five standard deviations away So why don't they say five standard deviations away Because

**Kyle:** I don't know Z scores sounds cooler I guess but they

**Linh Da:** said sigma they didn't say Z

**Kyle:** score Yeah well it's the same thing It's sosome of this comes from an almost antiquated concept that people probably won't talk about much in 100 years that it used to be These calculations were really tricky to do before we had computers So you'd have these big look up tables and you wouldn't actually compute something directly You would transfer your answer to the standard normal distribution of mean zero standard deviation one You'd look up the value in a look up table and then you transfer it backand that's kind of where Z scores come from is that everyone could agree that there was this one sort of standard model of the Gaussian distribution Um but they're still useful like it's still helpful to say like how many standard deviations away from the means something is and in particular in an upcoming episode next week we will have a guest talking a lot about Z scores and in his context he means how likely the result is due to chance or due tothe alternate hypothesis that someone in this case cheated at somethinggood to know So what did you learn today linda But

**Linh Da:** I am very short

**Kyle:** and I am

**Linh Da:** no you're fine

**Kyle:** you could have pushed up my ego and you didn't

**Linh Da:** You said you were six ft 1st

**Kyle:** Yeah well I'm almost if I wear good shoes I

**Linh Da:** guess Well

**Kyle:** thanks again for joining me linda

**Linh Da:** Thank you
