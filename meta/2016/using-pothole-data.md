## Using Pothole Data

Earlier in 2016, we did an episode about the data of [potholes](http://dataskeptic.com/blog/episodes/2016/potholes).  After Linhda had a pothole related biking accident, we reported the issue to 311 and later went in to the LA City Data Portal's 311 dataset to see how our incident was described in their records.

I had planned on collecting all the other pothole complaints as well and doing some exploratory data analysis.  As it turns out, there's a few issues we encounter along the way which are discussed in the episode.

After a talk I gave last month, someone asked me what I would have done if I had a high fidelity dataset on pothole locations.  I've had a little time to formulate my answer a bit more cohesively, so here's what I would have done.

First off, I want to be explicit that I'm talking about having a good quality *reported* pothole dataset.  I think having some sort of sensor network that is able to physically detect them with any precision is unrealistic due to costs.  I don't think some satellite photo analysis is realistic either, due to many concerns, the two most significant being resolution and occlusion.

Let's also put the idea of using a cell phone's accelerometer out of scope for this discussion. 

If we're relying on human reported data, then we can't ignore a significant amount of reporting bias.  Whether it be due to lack of time, lack of care for one's community, or cynicism of the effectiveness of government, many (most?) people probably can't be counted on to call.  People are unreliable sensors for this purpose with a high rate of type ii errors, and probably few type i errors.

We must also consider that potholes can effect a larger group of people than just those living nearby.  This is especially true on major thoroughfares.  Primary arteries are likely to have high frequency of reports for this reason.  Yet, they by definition have more wear and tear, so its unclear whether we have lower risk of an unknown pothole on smaller or major streets.

To avoid falling victim of reporting bias, something would need to be done.  I might make an assumption that each neighborhood has a constant reporting rate.  Perhaps people living in neighborhood A report twice as often as people in neighborhood B.  If so, they do this consistently across most or all issues; no neighborhood is exclusively ambivolent or sensitive specifically to potholes.  That might be a useful way to normalize, but I think it's probably a mistake.  It ignores my earlier point about people passing through neighborhoods.  It also ignores the composition and frequency if issues in a given area.

With these realizations, my next step would have been to look for reporting patterns (however biased) related to available geographic features and street data.  I can use the Open Street Map to get some metadata about roads and estimate if they're major or minor streets.  I can probably use some altitudinal data as well.  I learned during this episode that water is the source of potholes.  Since water tends to roll downhill, surely altitude is a useful feature.

With some road and altitudinal data in hand, I'd try to build my first model.  Yes, reporting bias will add noise to it, but I expect I should be able to find some relationship.  Most likely, I'd find out a few details that a civil engineer already knows :)

I'd also look for sequential patterns.  Does the recent history of pothole reports give me predictive power over future pothole reports?  In a way, such a finding might be invariant to the reporting bias.  I'm not sure this pattern would certainly be there, but I'd check for it.  If any amount of information is available, the city could exploit this to plan pro-active search and fill opperations.

Once I had some understanding of any patterns available in the reports, I'd next want to understand more about the city's opperational processes.  Despite many of our expectations, the city does not have infinite resources.  They are bound by budgets that derive from the taxes so many of us we want to minimize paying.

What are their options and costs for repairs?  Are they bounded by the material to fill the potholes (unlikely) or the labor to do it (probably)?  Would it be more cost effective to schedule an optimize path to travel and fill that takes 8 hours and is executed as a single day of work?  Or is it most cost effective to have four 2-hour trips to clustered areas?

The dataset should give us a good model of the state of potholes in the city and a probabilistic transition model of how that state changes.  What's missing is a clear understanding of how the city acts on it.  Surely its more complicated than "fill pothole at this lat/lng" as an atomic action.  Sequential planning must get involved, which means we need to understand the cost of the city to create a utility function.  With *that* in hand, we could perform a true optimization.

When I started the episode, I had only a tiny hope that things could be carried through to that optimization.  My objective was more to tell a story *about* the data and see where it too us during the investigation.  From what I understand, the city has been making process on the data front.  In the near future, it might be possible to take a project like that the next ten yards.

