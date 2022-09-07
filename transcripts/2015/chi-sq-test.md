**Linh Da:** The data skeptic podcast is a weekly show featuring conversations about skepticism critical thinking on data science

**Kyle:** Welcome to another mini episode of the data skeptic podcast I'm joined as always by my wife and co host linda

**Linh Da:** I'm linda Hello

**Kyle:** thanks for joining me linda

**Linh Da:** Thank you

**Kyle:** So today we're going to talk about the chi squared test Are you familiar with this at all

**Linh Da:** How do you spell

**Kyle:** itWell you spell it with a greek letter that looks like an X So that's how you spell But

**Linh Da:** most

**Kyle:** people say C H I That's how like use it in most programming languages and stuff or how you write it in a

**Linh Da:** textbook

**Kyle:** So chi square is a type of distribution Um But we're going to use it for a specific purpose We're going to talk about the chi squared independence test which is a form of hypothesis testingDo you remember in episode 24 when we talked about the T Test

**Linh Da:** a little bit

**Kyle:** and I was talking about human heights and things like that So the T test these are kind of like sisters in a way T test you can use well just go back and listen to that episode to find out how to use it The chi square test is in a different situation It's when you have categorical data like labels of something over a few different sub samplingsMaybe I should mention some more details I'm not going to talk about the arithmetic procedure for how you actually implement the chi square test You can go find plenty of resources online and most of the time Actually software packages do that for you So whether use like R or python you know it's one command it's chi sq dot test or something like that Also not going to talk about things like the Yates continuity correction because the software will usually figure out whether or not you need that I want to talk abouthow and when you should use the chi squared test Okay

**Linh Da:** okay

**Kyle:** You know what categorical data is So there's numerical data that's like how many MPH were you going It's a number it's continuous you can measure it and like one is always faster than the other But something like what is your favorite color is a good example of categorical because there's no real order it's not like red goes before green goes before yellowI mean there's the color spectrum but basically people just have colors there's no relationship to one another or like whether or not your immediate er pesca Terrien or vegetarian those are three categories but there's no order for them They're just labels If you want to say like our men more likely to be vegetarians than women That would be a categorical hypothesis you could test because you put all the men in one group all the women in the other groupand you get the frequency of how many times each person fits in each Now In order for the chi square test to be appropriate You have to first make sure all of your observations are unbiased They're independent and identically distributed You sample them well you have to make sure your sample size is big enough and there's a couple of rules of thumb The one I typically want to follow is that every cell has to have at least five observationsDo you know what I mean by cell So picture a table as the rose men male and female and as the columns vegetarian pesca Terrien and Omnivore And then you write the number of people who said they were in each in those blanks

**Linh Da:** and

**Kyle:** each little blank like an excel is a cell So if you don't Yeah as a rule of thumb some people argue it should be 10 and some people talk about the overall sample size and I guess the moral here that I don't want to get into the statistical debate But if you have a very very tiny sample size you need to be very considerate of whether or not that's going to affect your test and you know not just follow a rule of thumb but consider like one important thing I would suggest isimagine if you had one extra data point if that one single data point can change the results of your test then your test is very fragile So yeah if you have really tiny numbers odds are the chi square test or any test is probably not gonna be a good one for you The rule of thumb is kind of like five for each cellSo I thought it would be fun to do more of a hands on projects So I got some data out of the L A City data portal that has crime statistics

**Linh Da:** So Kyle sent me an email So on the left have the days of the week monday Tuesday Wednesday thursday friday all of them Yeah all of themAnd then the other columns say vehicle then another column has bike where the row and the columns intersect There are numbers under bike vehicle day

**Kyle:** Those are the reported number of thefts of each of those type of vehicles Do you think the day of the week will affect the distribution over which type of thefts occur

**Linh Da:** So let me just backtrack for these numbers Are you saying these days the people reported the theft or these days they think the theft happened

**Kyle:** Great question And actually that's a good data provenance question I would have to follow up Let's work on the assumption that I'm pretty sure it's true that the count ison the day that the report came in which presumably should be the same day as the theft more or less

**Linh Da:** Okay so then you ask me do I think there would be more thefts on a certain day of the week or

**Kyle:** weekday versus weekend kind of situation

**Linh Da:** I guess weekends have more thefts because that's when people go out So there's more targets

**Kyle:** So do you think it's more proportionally more more vehicle and more bike thefts oris it that the bike thieves are consistent but the car thieves have a weekend spree

**Linh Da:** Well I think bikes would also go up because probably more people bike on the weekend

**Kyle:** So you think that even though there might be higher volume on the weekend that the proportion is the same

**Linh Da:** Is the proportion the same for bike and vehicle Is that

**Kyle:** that's my question What's your

**Linh Da:** thought My guess is for both of them the proportion goes up on the weekends or goes up when people are out

**Kyle:** But I mean with respect to one another

**Linh Da:** from bike to vehicleAh that is probably different I don't know

**Kyle:** So you would think that they'll both go up on the weekends and maybe vehicles go up even more than bikes or vice versa

**Linh Da:** Yeah I mean I guess vehicles would go up even more just because I don't know why I guess bike these people just suddenly be like monday I'm in the office friday I'm gonna get your bikeI know I mean I just feel like the car theft people are more consistent than the bike people You've

**Kyle:** just insulted our bike thieving listeners I'm going to get complaints of this

**Linh Da:** I just think that there's less money and bikes So the people who are going to steal them and volumes are low

**Kyle:** so they have to work harder They're probably more entrepreneurial

**Linh Da:** I

**Kyle:** don't knowWould you mind giving a quick summary of what's about the average day to day And do you see just eyeballing at any major spikes

**Linh Da:** So for vehicles average looks ranges between 1100 and 1300 So I guess the average would be 1200On any given day That's how many thefts and bikes hover around 100-1 10 So the average is probably 106

**Kyle:** Just to give some clarity That is the total number of thefts by day for the period that my data covers which is a partial coverage of 2014Um And the chi square test is all about counting frequency of events So that's why I did it that way It's not that there are 100 bikes stolen a day It's that over this period there were that many

**Linh Da:** I thought every day on sunday Yeah

**Kyle:** Clarification Sorry about that That would be a lot of

**Linh Da:** Yeah I was like wow that's crazy I gotta move I didn't know there were that many bikers on the road is what I was thinking

**Kyle:** So anyway where I was going why something even though it's kind of consistent day to dayit's important to note the point we're making about the relative frequency because if you were to test something like demographics the population of caucasians is very high in the US followed I think number two by african americans and then like Hispanics and asians pacific Islanders and all that stuff trailing off so often those smaller demographics the overall total is much smallerBut that doesn't mean that the proportions are different So you could look at incidents of some disease or whether or not there you know a smoker whether or not they get in car accidents you have to kind of look at relative frequencies And the high square test sorts a lot of that out for you because it looks row by row relativelySo if I want you to eyeball your hypothesis that the weekend vehicles have a surge in thefts What do you think that the data kind of reports that

**Linh Da:** well for vehicle definitely thursday friday and saturday have the most thefts compared to other days of the week

**Kyle:** Um the numbers do go up but it's also a little deceptive because the bikes are such a smaller number andit's relatively consistent So the question we wanna ask is yeah is that perceived incremental increase a real phenomenon that a statistically significant one or is it is perhaps due to chance that thursday friday and saturday seem to be much greater than the bike data And we can use the chi square test to determine that And let me do that right now the chi square test reports back a p value of 10.55Do you remember our p values episode

**Linh Da:** Not much but what does this mean

**Kyle:** This means that the data does not support the alternate hypothesis So we need to reject the alternate hypothesis and accept the null hypothesis that there is no statistically significant change with respect to day of the week for

**Linh Da:** vehicles and bikes or together

**Kyle:** that the day of the week doesn't affect the number of vehicle and bike thefts not the total volume It can affect that but it doesn't affect their proportion

**Linh Da:** Does it matter if you just run your tests just on vehicles excluding bikes will you get the same answer

**Kyle:** What do you mean Because then it's no longer two groups being compared

**Linh Da:** You have to have two groups

**Kyle:** Well you have to have two categories at least you can have actually more than that But if you don't have two categories there's nothing to

**Linh Da:** compare So what question is are you asking with these two categories

**Kyle:** Does the day of the week affect the proportion of the types of thefts that occur

**Linh Da:** Well types you only mean vehicles and bikes correct So then you're saying you ran the chi test and it said when you're comparing vehicles and bikethat's not

**Kyle:** correct The day of the week does not have a statistically significant impact

**Linh Da:** What would a lower p value b zero

**Kyle:** The sort of almost arbitrary rule of thumb that we follow Is that anything below 0.5 we can reject the null hypothesis So that means there's a one in 20 chance that we're wrong that the difference we detected is due to chance but it seems like okay probably if it's only one in 20It it implies that our data is not due to chance Some people also will take a stricter thing depending on you know what your test is Like if you're gonna invest your life savings you might want a p value of .01% or .0001% or something You want a lot more certainty over things if they're very important decisions But 0.05 is this sort ofarbitrary line in the sand that I think Pearson came up

**Linh Da:** with So we're just comparing vehicles on bikes let's say vehicles we keep the data as it then bikes we faked the data Could it come back and the high test tell us a different story Yeah Or do you have to change both columns

**Kyle:** No Um if you change just one the story could be different You want to try and do that here Let's make a copy Okay so I doubled the number of bike thefts on the weekend or not Sorry not the weekend Just friday and saturdayI re ran the test and now I get a p value of 4.39 times 10 to the -11 Very very very close to zero So we now reject the null hypothesis except the alternate hypothesis which is that the day of the week has a statistically significant impact on which type of thefts are going to occuryep between vehicle and bike

**Linh Da:** But

**Kyle:** I like what you proposed actually I think that is a very worthwhile exercise More people should be doing It's almost not enough to just run your test get your p value and decide whether you accept or reject your hypothesis It's nice to play around and say like all right what would it take for me to get the other value How much would I have to tweak my numbers In my case I just said let's double the bike thefts on the weekend which is a pretty strong scalar right doubling some things a lotWhat if I was like Oh let's make it 10% more Would that have changed things So it's a very worthwhile exercise I would say to do what you suggested and just kind of play around with the data and understand how sensitive your result is Too slight changes Um that's not a formal part of the Chi Square test That's just something I recommend for all hypothesis testing in general

**Linh Da:** Will you post this table online

**Kyle:** Yes the table will be in the show notes So people can go look at the data There's also I don't know if everyone knows thisEvery show notes No some of them are just text but they all have source code that shows any of the work that's been done So if you want to repeat the analysis you can go and follow the exact code I post on get hub and you can run through the same analysis yourself and play around with the data if you want toYeah I squared I didn't walk through kind of the arithmetic parts because you can go learn those anywhere I talk more about how to use it Keep in mind that rule of five arbitrary rule But it's helpful because if you have very sparse cells you can often get spurious results Generally sample sizes of 10 or more are looked for and let's wind up with one final discussion about the data itself and being skeptical of it Now I told you I got this out of the L A City data portal You asked a very good question which wasis the date the report date or the actual incident date and I did not know um What I also don't know is if the nature of police procedure can affect this data So for example maybe the worst cops get relegated to weekend duty and the best cops get to you know have the weekends off to spend with their family and their friendsand the worst cops don't report things as well or don't like to fill out paperwork and it could change the numbers or skew the data and I'm not making accusations about the cops per se Just saying that there could be nuances like that that affected So for example what do you think about report rates of vehicle theft versus bike theft

**Linh Da:** I think vehicles will definitely be reported more because they're worth more Whereas bikes people just shrug Yeah

**Kyle:** You feel like cops aren't gonna do anything

**Linh Da:** Yeah What's the cops gonna do

**Kyle:** with two

**Linh Da:** $100 bike even a $500 bike $800 who cares

**Kyle:** Let's get a team of seven people on this We gotta find this bike

**Linh Da:** Yeah And most bikes they have to be in great with the registration number and most aren't

**Kyle:** Yeah

**Linh Da:** And so if you don't have a registration number they're gonna when they find the quote unquote said bike they're not gonna know it's yours

**Kyle:** So it could be that your initial instinct that the weekend made a difference is true but our data doesn't support that because citizens fail to report bike thefts

**Linh Da:** Maybe

**Kyle:** So even if you think oh there's nothingI can do The cops can't help Even if they wanted to try it's still worthwhile to always report these things So we have accurate statistics Okay let's wind up with a shout out I'm gonna do some shout outs in these many episodes for the next couple of weeks because there is a growing community of excellent data related podcast that I want to tell my listeners about in case you don't know about some of themOne that I'm kind of new to is called the partially derivative podcast I will put a link in the show notes It's kind of like a like digg nation for data science They cover the week's top news stories and headlines and they talk about what beers they're drinking and stuff So it's a fun showand it's great because there's no overlap really with data skeptic podcast there They actually do a lot of stuff I wish I could cover But you know I can't turn around the shows as quickly you know to cover news headlines and guests and stuff Different format but interesting stuff if you're into data science so everyone should go check out partially derivative I

**Linh Da:** have a question You encourage people to report bike theft I have a question Did you report your bike

**Kyle:** No I did not

**Linh Da:** Well thenthat just shows you people do not report bike

**Kyle:** Just to say it Say the word starts with an Hno hypothesis

**Linh Da:** Kyle the hitchhikerI'm

**Kyle:** a hypothesis

**Linh Da:** Well our audience can decide what they thinkThanks for joining me
