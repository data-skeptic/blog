## How America voted in 2016: datasets to help us figure it out

Buried in the Comey news last week was the release of a dataset by the U.S. Census Bureau that gives us one of the most complete looks at how people voted in the 2016 presidential election—the [November 2016 Voting and Registration Supplement](https://www.census.gov/newsroom/blogs/random-samplings/2017/05/voting_in_america.html) to the Current Population Survey.

2016 voting patterns might not seem like a particularly newsworthy topic today, more than six months after November 8. But it's time to revise the initial narrative of how people voted, a narrative [gathered from exit polls](https://www.nytimes.com/interactive/2016/11/08/us/elections/exit-poll-analysis.html). 

Although good for figuring out how people voted in aggregate, exit polls are not meant to be sliced and diced into precise demographic subgroups.

Here is a list of datasets that have come out since the election that can help us better understand  2016 voting patterns and demographic breakdowns:

### Voter File Data

**What is it?**

* In order to understand how people voted, you need to first figure out who votes. Whether or not you voted is a matter of public record (who you voted for isn't), and this information is in each state's [voter file data](http://voterlist.electproject.org/). 

**How can I get it?**

* Getting ahold of voter file data is tricky, and it can be costly. Also, only some states collect information on race or ethnicity. Firms like Catalist and TargetSmart use statistical models to try to match voter files to demographic charactersitics.

**Where can I read about it?**

* Nate Cohn, ["A 2016 Review: Turnout Wasn’t the Driver of Clinton’s Defeat."](https://www.nytimes.com/2017/03/28/upshot/a-2016-review-turnout-wasnt-the-driver-of-clintons-defeat.html) *NYT Upshot*, March 28, 2017.

### The Cooperative Congressional Election Study (CCES)

**What is it?**

* The CCES is a large-scale national survey of more than 50,000 American adults administered online by YouGov/Polimetrix. It's been around since 2006, when a consortium of 36 universities came together to study the midterm Congressional elections. 

* During presidential election years, the CCES has a pre-election wave from late September 2016 to late October and a post-election wave in November 2016.

* This year's CCES surveyed 64,600 respondents.

**How can I get it?**

* Preliminary data from the 2016 post-election wave was posted on the [Harvard Dataverse](https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/GDF6Z0) on March 3, 2017. 

* The release is [not final](https://twitter.com/b_schaffner/status/837733474639413253) because the data have not yet been vote validated. Vote validation is the process of double-checking that the people who said they voted actually did vote, according to voter file data. The survey's post-stratification weights will be re-calculated based on this information. 

* This is the first year the CCES has done a preliminary release, "given the tremendous interest in the 2016 election and the eagerness of scholars to understand what happened," said Brian Schaffner, the co-PI for the study. According to Schaffner, a final release, along with a data guide, should be up by early to mid-June (for reference, [here's](https://dataverse.harvard.edu/file.xhtml?fileId=2688939&version=8.0) the 161-page guide from 2012).

**Where can I read about it?**

* Alexander Agadjanian, ["How the 2016 Vote Broke Down by Race, Gender, and Age."](https://decisiondeskhq.com/data-dives/how-the-2016-vote-broke-down-by-race-gender-and-age/) *Decision Desk HQ,* March 8, 2017.

* Geoffrey Skelley, ["Another look back at 2016: Comparing the exit poll and the Cooperative Congressional Election Study."](http://www.centerforpolitics.org/crystalball/articles/another-look-back-at-2016/) *Sabato's Crystal Ball,* March 23, 2017.

* Jason Weeden, ["Comparing Samples from 2016: Exit Polls vs. ANES vs. CCES."](http://www.pleeps.org/2017/04/10/comparing-samples-from-2016-exit-polls-vs-anes-vs-cces/) *We the Pleeple: Social Science for the Pleeps,* April 10, 2017.

### The American National Elections Study (ANES)

**What is it?**

* The ANES is a joint project of the University of Michigan and Stanford University to understand public opinion and voting behavior in U.S. elections. It's been around since 1948. 

* The 2016 ANES consisted of a pre-election survey between September 7 and November 7, 2016 and a post-election survey between November 9 and January 8, 2017. It combined face-to-face interviews of 1,181 respondents with online surveys of 3,090 respondents.

* For the first time, this year's ANES asked respondents for access to their Facebook timelines in an attempt to see how much individuals were posting about the election. At this point, the ANES staff hasn't decided whether or how they will make this information public. 

**How can I get it?**

* The initial release of the 2016 data was posted on March 31, 2017, though there have been [subsequent releases with updates](https://twitter.com/electionstudies) since then. The final update will likely be out this fall.

* The dataset is available [here](http://www.electionstudies.org/studypages/download/datacenter_all_NoData.php) (registration [required](http://www.electionstudies.org/studypages/download/registration_form.php)).

* UC Berkeley's [Survey Documentation and Analysis (SDA) query tool](http://sda.berkeley.edu/archive.htm) has aggregate ANES data available for certain cross-tabs and regressions. 

* This website, [Analyze Survey Data For Free,](http://www.asdfree.com/search/label/american%20national%20election%20studies%20%28anes%29) is another good resource for figuring out the nuts and bolts of analyzing the data (using R), created by independent consultant Anthony Damico.

**Where can I read about it?**

* Thomas Wood, ["Racism motivated Trump voters more than authoritarianism."](https://www.washingtonpost.com/news/monkey-cage/wp/2017/04/17/racism-motivated-trump-voters-more-than-authoritarianism-or-income-inequality/) *WaPo Monkey Cage,* April 17, 2017.

* Jason Weeden, ["Comparing Samples from 2016: Exit Polls vs. ANES vs. CCES."](http://www.pleeps.org/2017/04/10/comparing-samples-from-2016-exit-polls-vs-anes-vs-cces/) *We the Pleeple: Social Science for the Pleeps,* April 10, 2017.

### Voting and Registration Supplement to the Current Population Survey (CPS)

**What is it?**

* The U.S. Census Bureau has collected voting and registration data since 1964. This information is released in the November CPS supplement every two years following national elections.

* This year's survey included about 56,000 households and was conducted from November 13 to 19, 2016. Included are U.S. citizens 18 and older.

**How can I get it?**

* The CPS supplement was released May 10, 2017. Summary tables are available [here](https://www.census.gov/data/tables/time-series/demo/voting-and-registration/p20-580.html). You can get customized historical reports by logging onto [Data Ferret](https://dataferrett.census.gov/).

**Where can I read about it?**

* Thom File, ["Voting in America: A Look at the 2016 Presidential Election."](https://www.census.gov/newsroom/blogs/random-samplings/2017/05/voting_in_america.html) *Census Blogs,* May 10, 2017.

* May 10, 2017 Twitter thread by Nate Cohn, starting with ["Census data on 2016 turnout is out. Almost exactly as expected."](https://twitter.com/Nate_Cohn/status/862327580015415296)

* Nate Cohn and Amanda Cox, ["The Voting Habits of Americans Like You."](https://www.nytimes.com/interactive/2016/06/10/upshot/voting-habits-turnout-partisanship.html?_r=0) *NYT Upshot,* June 10, 2016 — uses CPS data, among other sources, to estimate voting patterns in 2012 (and 2004) by race, education, gender, age, and state. GitHub repo [here](https://github.com/TheUpshot/2004-2012-presidential-election-model). Looking forward to seeing a 2016 update!

* Nate Cohn, ["There Are More White Voters Than People Think. That’s Good News for Trump."](https://www.nytimes.com/2016/06/10/upshot/there-are-more-white-voters-than-people-think-thats-good-news-for-trump.html) *NYT Upshot,* June 9, 2016. Particularly the section labeled "An Older, Whiter, Less-Educated Electorate" (with expanded methodology).

### Other post-election polls

**Edison Research** conducts the [national exit polls](http://www.edisonresearch.com/behind-numbers-2016-national-election-exit-poll/), which are funded by a group of major media organizations. Other groups conduct their own polls.

The **Asian American Legal Defense and Education Fund (AALDEF)** surveyed Asian-American voters on Election Day and found a markedly higher percentage of them who said they voted for Hillary Clinton than indicated by the national exit polls. AALDEF sampled more Asian-Americans than Edison. It also provided questionnaires in a variety of Asian languages as well as in English (Edison polled in English and in Spanish). The [report](http://aaldef.org/TheAsianAmericanVote2016-AALDEF.pdf) came out in April and was covered by [*NPR*](http://www.npr.org/2017/04/18/524371847/trump-lost-more-of-the-asian-american-vote-than-the-national-exit-polls-showed).

Similarly, the polling firm **Latino Decisions** has argued that the national exit polls [got the Latino vote wrong](https://www.washingtonpost.com/news/monkey-cage/wp/2016/11/11/in-record-numbers-latinos-voted-overwhelmingly-against-trump-we-did-the-research/). According to their [Election Eve survey](http://www.latinodecisions.com/2016-election-eve-poll/), Clinton did better among Latino voters than the exit polls suggested. Analyses of [California](https://www.washingtonpost.com/news/monkey-cage/wp/2016/12/02/donald-trump-did-not-win-34-of-latino-vote-in-texas-he-won-much-less/?utm_term=.0d99b4ead7bf) and [Texas](http://www.latimes.com/opinion/op-ed/la-oe-pedraza-latino-vote-20170111-story.html) precinct data by Francisco Pedraza and Bryan Wilcox-Archuleta are consistent with this claim. However, Harry Enten's analysis for [*FiveThirtyEight*](https://fivethirtyeight.com/features/trump-probably-did-better-with-latino-voters-than-romney-did/) indicates that although Clinton did better among Latinos than exit polls suggested, Trump might have done better among this demographic than Romney did in 2012.

The **USC Dornsife/Los Angeles Times post-election poll of California voters** was conducted by SurveyMonkey. In the [*L.A. Times*](http://www.latimes.com/politics/la-na-pol-california-presidential-poll-20161116-story.html), David Lauter compared results from this survey to SurveyMonkey's national post-election poll.

### What else?

See any important datasets or reports that are missing from this roundup? Let us know by leaving a comment below.

