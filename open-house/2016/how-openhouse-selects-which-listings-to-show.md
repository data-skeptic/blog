## How OpenHouse Selects Which Listings to Show

In many geographic areas, we have so many listings, that we must return a limited sample.  When visiting [http://gallery.openhouseproject.co/](http://gallery.openhouseproject.co/), we cannot expect users to wait extended periods of time for tens of thousands of listings to be downloaded.  The same is true for API users, although they should already specify the `limit` field to meet their needs.

While we are in the beta development of the OpenHouse project, our focus is on getting the largest collection of data we can find.  As a result, we've cut some corners in terms of sampling bias and how representative the results are when using our API.

At present, our results return chronologically by upload date.  This is not ideal and we have plans to improve upon this design, but for the time being, this is how our system works.

As a result, our recommendation for using our data is to use the following steps:

### Recommendations for using our data

1. Learn how to use or API to download the data you are interested in programatically.  If you aren't comfortable doing that, we're here to help!  Reach out via email or on the Data Skeptic Slack group.
1. Make sure you understand the `limit` and `offset` parameters of the API which paginate the results.  Iterate through calls until you've downloaded *all* the records in our system for the area and criteria of your own interest.
1. Do some data cleansing including deduping.
1. Use your cleaned dataset for analysis.

### Future planned improvements

We plan to add additional filtering to the API including:

* Query by boundbox (currently only radius available)
* Query by arbitrary polygon
* Query by date range

Additionally, we want to provide some choices about the ordering in which the results come back.  As mentioned, our results presently return in the not particularly helpful order they were uploaded.

Naturally we plan to provide the option to order the returned results randomly.  This should enable people only interested in doing analysis on a random sample to make quick single calls to the API for their purposes and expect to get back a representative sample.

Further, we intend to investigate the option of returning a random and stratified result.  If you wanted to conduct a poll about a democratic election, you'd want a sample that is composed of respondents whose age, ethnicity, gender, and other demographic details roughly align with that of the voting public.  We're not yet sure exactly what it means to stratify property sales data.  If you have any ideas, we'd love to hear them!

The randomization could also be problematic.  If two people make identical calls to the API, they should have some reasonable expectation of getting the same results.  This wouldn't happen with a truly randomized sample.  As a result, we are planning to select a global random seed for use in the number generator that handles the randomization.  This seed will be changed with some frequency (probably hourly or daily) but will have enough persistence to ensure some consistency across calls.

Whenever either of the above two sort options are available, we will likely make these the default ordering.
