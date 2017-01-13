## Weather Data and The Library Problem

This post is a follow up related to our episode titled [The Library Problem](http://dataskeptic.com/blog/episodes/2016/the-library-problem) in which I have a discussion about a particular interview question I used to ask junior data scientists.

I've had a few listeners coincidentally come up with the same unique idea: could you use weather data in this problem?  I think this is an interesting idea worth a further discussion.  Feel free to share your perspective in the comment section below.

My general answer is yes - weather data could *probably* be useful for this problem.  However, I expect it's a weak predictor and one whose information content might not justify the engineering investment.

Let's first explore what it would take to implement this.

To begin, you'd need to have some source of weather data.  Weather is a fairly complicated system.  As I understand it, the mechanics of how weather changes are really well understood.  Meterologists seem to have theories which adequate describe all weather phenomenon.  In the same way that Newtonian mechanics *almost* perfectly describes the orbits of the planets, qualified people know how weather changes.  I'm not an expert in this area, but this is my lay understanding.  There may still be a few anomolies to explain just like there were in the orbits of Uranus and Mercury before realtivity closed that gap.

The challenges to forecasting the weather are bounded not by an understanding of the mechanics of weather but by the computational power to evolve the models.  It's interesting to note that [IBM bought the Weather Company](http://www.marketwatch.com/story/ibm-finally-reveals-why-it-bought-the-weather-company-2016-06-15).

The idea that a data scientist with no background in weather science could build a useful forecast is pretty hubristic.

Luckily, we don't have to re-invent the wheel.  There are already a variety of services available to programmatically retrieve weather forecasts.  I've had fantastic luck working with the [Dark Sky API](https://darksky.net/dev/) in the past.  First 1k forecasts are free; reasonable pricing thereafter.

Yet some integration is required.  That takes time, and time has a cost which we'll call $C$.  We have to ask about the value of information.  The librarian needs to make a decision.  I didn't specify what that was in the episode.  Maybe the decision is whether or not to execute their discretionary powers to deny the checkout if the risk is too great.  (I doubt this would happen in real life, but let's go with it)

The librarian can make a decision based on a model which does not include the weather forecast as a signal.  We'll call that the uninformed decision $D_u$.  The librarian might also have access to a theoretically superior model which does use the weather data and make a more informed decision $D_i$ based on that prediction.

Let a function $U$ exist which calculates the expected utility (perhaps dollars saved) for each decision $D_x$.  In other words $U : D_x \rightarrow \mathbb{R}$.

I'm going to skip over some important decision theory about those decisions, but it might be worth a follow up post on the subject.

Using the data above, we can now define the value of information for the weather data as:

$V = U(D_i) - U(D_u) - C$

In english, the value of information is the expected utility when acting *with* the information, minus the utility you would have gotten anyway acting *without* the information, minus the cost of aquiring and integrating the information.

The cost is non-trivial.  The person building the model will need to spend at least a few hours working on this, possibly more.

It seems intuitive that some percentage of the library patronage would be adverse to doing errands (like returning library books) during inclement weather.  For patrons who keep their books for the full term of the checkout and find themselves unwilling to leave the comfort of their homes on the due date because of the weather, a forecast would have great predictive power.

There could definitely be circumstances other than the one I described above for which weather correlates with likelihood of return.  Maybe people would rather go to the beach on nice days.  Or more car accidents happen during bad weather, and people on their way to return a book will give up after having an accident.  I'm just trying to convince myself that indeed some circumstances exist for which weather forecasts could plausibly be useful.  The last digit of the person's phone number, on the other hand, has no plausible usefulness.

Now the question is how useful can the weather forecast be?  How much information is contained in this signal which cannot be extracted from some other source?

I don't have the answer to this question for weather.  However, my instincts tell me that the predictive power will be rather low.  As a former Chicagoan, I lived in a large variance of weather conditions.  Yes, during extremely bad snow days, I'd sometimes have to stay home.  But that was exceptional.  I think most people find ways to have routines which are not deeply effected by the weather.  I've lived in Los Angeles for many years now, and I can attest that drivers here don't always have the automotive prowess of my fellow Chicagoans.  There are times when the slightest hint of rain changes plans.  Yet our rain is rare enough that this event isn't all that useful.

Ultimately, this problem, as with any supervised machine learning problem, is trying to provide an algorithm with a useful input dataset and examples of the desired output, so that the algorithm can identify correlations between the input and output data.  These correlations can be exploited for predictive power.

I find myself shuffling through the various scenarios, however contrived, in which the weather much actively switch a patron's behavior from someone who returns on time to someone who doesn't.  While I'm sure it effects some individual return events, I'm not convinced there are enough available for weather to contribute predictive power to the question.

Granted, library behavior *on the whole* is likely to be effected by weather.  If you wanted to predict how many patrons will come to the library on a given day, this blog post would have read very differently.  The problem is predicting if a book, at the time of checkout, will be returned on time.  Since "on time" is a window of time, the affect of weather is a bit more murky.

For the record, I would not have penalized anyone I interviewed for bringing up the weather just because my instinct says it's not the most useful indicator.  First, I could be wrong about my expectation.  Second, I wouldn't assert it has no value; there must be some predictive power there.  Third, a good discussion about the hows and whys of incorporating weather would teach me a lot about a person's problem solving strategies.  We all have to make mistakes and go down dead ends in order to learn.  Success is not about how many dead ends you go down, but rather how quickly you recognize the dead end and turn around.

