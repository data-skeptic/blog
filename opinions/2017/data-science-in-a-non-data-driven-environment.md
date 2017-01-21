## Data Science in a non-Data Driven Environment

I got a message from a listener helping a non-profit leverage machine learning to help optimize their donor outreach.  From what I understand, charities in general experience very long tailed behavior from donors - most make a single donation, and a small population of donors make regular and major contributions.

Empirical evidence shows that if you contact everyone in your database asking for donations, you will definitely see a response.  However, you can only do that so often without burning out your audience.  In a perfect world, you would contact only the most receptive donors at exactly the perfect time.

For some people, the "perfect time" could consist of sending them a message right after they've gotten a bonus of some kind (perhaps a commission bonus, tax refund, or something like that) while also contacting them just as they are checking their email and don't have too many emails left to read.

It's hopeless to think that a charity could model the time at which a person is actively checking and responding to email.  It's also probably hopeless to anticipate when a person might find themself in a generous mood with a surplus of income.  Granted, certain good times are known.  I presume post-tax refund might be good.  Better still, the holidays are a time of above and beyond giving.  One might even use common pay period cycles as a feature, but ultimately, certain things are not directly observable or by proxy.

Its a common situation for people that aren't data scientists to hear about some achievements of data science teams, and to conclude their data must be a veritable gold mine.  Sometimes they're right, but more often than not, that gold mine require a lot more excavation and has fewer veins than anticipated.

Its nearly impossible or a data scientist to set up expecations at the front end of a project.  One simply needs to do some exploratory data analysis and let the data speak for itself.  The likelihood of chasing a hypothesis and arriving at the null hypothesis is very high.

The listener was specifically asking me if I had any tips for having a "data conversation".  I gather that this means he's looking for effective communication techniques to set realistic expectations with the non-profit and get them on the path to success.  A part of that challenge is often going to be managing the expectations of what is possible and frequently to explain how much effort exists in the data cleaning phase to transform their less than ideal records into a usable dataset.

In a situation like this, I often go in with the expectation that the organization has very poorly organized data.  This is not because I'm an elitest, but because I know the most effective non-profits are highly attuned at delivering service to their specific cause.  Rarely do they have the time, energy, and resources to implement proper data governance procedures.

Focusing on the problems with the data can be very disheartening for the organization.  More than a few organizations probably give up after the clean up stage slows down progress on a data initative.  Are things totally hopeless?

I think not.  While I've seen data clean up to be a major issue in these types of organizations, I've also observed that it doesn't always take a lot of wisdom to do something impactful.  The worse the data quality, the more likely something as simple as de-duping a mailing list can be.

As I started out saying, a blanket marketing blitz will almost always yield more donations.  Yet, if using physical mailers, those costly postage and material costs add up.  The return might make it worthwhile, but what if you could cut the cost in half and still achieve 95% of the projected return?  Eliminating one-time donors could do just that.  If the organization is uncomfortable with a step like that, perhaps you could sell them on a procedure that assigns a probability of response to every person on their mailing list.  Those most likely to donate should get the "full regalia" mailer.  Those unlikely to donate might best be downgraded to a nearly costly email.

In the end, all good non-profits have some measurable objective they are trying to serve.  This might be individuals served, number of items given to the needy, or number of bad outcomes prevented.  If the organization doesn't have these KPIs (key performance indicators), the most important thing a data scientist can do is help establish a measurable process.  Only through measurement can improvement be rigorously achieved.

If the organization has good KPIs, the next question is what "levers" they have available.  Sometimes it can be very difficult to pin creative people down in this area.  Yet, at the end of the day, there are always a finite number of actions one can take towards any goal.  Identifying the breath of actions, devising a ways of modeling their effectiveness, and optimizing those actions given the objectives of the organization is a great problem for a data scientist to face.  The challenge typically is working with collaborators who aren't particularly analytical to help frame the problem in a solveable way.

In addition to my thoughts, organizations like [Data Kind](http://www.datakind.org/) and [Bayes Impact](http://www.bayesimpact.org/), which do these sorts of activities more regularly than I do, might have great tips as well.  I interviewed one of the Data Kind volunteers in a previous episode titled [Using Data to Help Those in Crisis](http://dataskeptic.com/blog/episodes/2015/using-data-to-help-those-in-crisis) about the Crisis Text Line.  Some lessons might be learned from that interview as well.

But returning to the listeners core question - how does one effectively manage the "data conversation"?

First things first, everyone needs to be honest about the quality of the available data and the effort to transform it.

Second, everyone needs to be realistic about the potential of the data.  Yes, data science is an umbrella term for some deeply powerful methods.  Yet, no analytical method is going to change a 3% conversion rate into a 30% conversion rate.  If an organization is so inefficient that there's a huge gap like this, then they don't need a data scientist, they need new leadership.  An honest asessment of the realistic/plausible improvement that can be done should be considered.  A consideration of the investment required to achieve that realistic estimate should be done in the context of costs and benefits.

Third, its important to frame all plans in the framework of a KPI.  Every non-profit wants to be effective in helping its constituents.  Its easy to get distracted from this in pursuit of a moonshot machine learning solution.

Fourth and finally, any data science work done for the non-profit should, in my opinion, be able to fail fast.  A minimal impact should be invested and a quantitative approach to measure that impact should be the ultimate arbitor about what happens next.  Be ready to give up, pivot, and start over.  At the end of the day, what technique is employed is nowhere near as important as the people helped by the non-profit.
