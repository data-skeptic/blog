## Notes on Uber's Experimentation Platform

I attended the [Chicago AI & Data Science Conference 2018](https://www.ideassn.org/chicago-2018/) this past weekend.  I presented a talk, lead a panel, and had the opportunity to enjoy a number of interesting talks.  The particular talk I took the most from was given by Jeremy Gu and Mandie Liu, both from Uber.

These Uber data scientists work on the experimentation platform the Uber has built to help them extend testing into a variety of areas of the business.  This talk highlighted the wide breadth of use cases in the company and their high level strategy for dealing with each.

Uber conducts both randomized experiments, in which users are randomly routed to a test or control group, and observational studies, in which they don't have the option of controlling user behavior but can look for natural experiments or apply techniques like [causal impact](https://dataskeptic.com/blog/episodes/2016/causal-impact).

Naturally, their platform manages classical experiments.  Here classical means univariate and multivariate randomized design experiments that can be analyzed with garden variety tests like the [chi-squared test](https://dataskeptic.com/blog/episodes/2015/the-chi-squared-test) or the [t-test](https://dataskeptic.com/blog/episodes/2014/the-t-test).  Techniques like this are all that's needed for the majority of companies dabbling in A/B testing, but Uber's extensive platform demands a few more features.

Their observation studies cover situations like marketplace impact on trips.  For example, if some new pricing strategy is rolled out, it may be challenging to anticipate the effects on the dynamic system of drivers and users.  It's very likely that things like [Goodhart's Law](https://dataskeptic.com/blog/episodes/2016/goodharts-law) could become especially relevant as different changes are made.

Three interesting algorithmic areas that benefit from experimentation were mentions: the dispatch algorithm, pool algorithm, and pricing algorithm.

Beyond this, Uber may wish to ask questions like "Is the driver following the navigation directions or disregarding them?"  The refer to ideas like these as observational studies because they can't be tested for, just observed.  If a change is made to the navigational system, one would expect that drivers are no less likely (hopefully more likely!) to follow the nav.  For studies like this, they discussed a number of methodologies and techniques ranging from developing a synthetic control, using machine learning, or applying causal impact.

A novel area of testing discussed was continuous experiments.  This label covers cases where a gradual rollout of a change is desired or the test is intended to have some component of hyperparameter tuning.  Their system leverages [multi-armed bandit](https://dataskeptic.com/blog/episodes/2015/multi-armed-bandit-problems) strategies (in particular, I believe they use Thompson sampling) to optimize the best value of a number of competing options.

A good example of a continuous experiment is for content optimization.  For example, testing the optimal email subject line.  The presentors gave an example of subject lines specifically for UberEats as this program rolled out in Europe.  They tested a wide variety of possible subject lines, optimizing for open rates.  Their winning subject was "Delicious food delivered to you".  Someone surprisingly, this outperforms other subjects like "Ready to order, [firstname]?" which included some personalization.  Also of note is how marginal these improvements are.  Their winner was state to achieve a 31.8% open rate, and the lowest subject line shared garnered only 28.7% open rate.  Yet for acompany like Uber, naturally, those seemingly small improvements can translate into millions of dollars very quickly.  Thus, at that scale, there's a strong incentive to engage in testing behavior of this nature.

One particular case study shared was especially novel.  Uber uses their experimentation platform to do staged rollouts.  As Uber releases new features to their app, even small things can potentially have unexpected results or unforeseen consequences.  Through continous monitoring and some time series approaches, they actively monitor various telemetry from their mobile app to ensure that changes of any kind don't adversely affect key business metrics.

Overall this was an interesting talk.  I wasn't surprised in any way by the methodologies being used, but I am impressed by the extensiveness and completeness of the platform described.
