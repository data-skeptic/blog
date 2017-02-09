## OpenHouse Voting, Priorities, and Decision Making

The OpenHouse project requires certain decisions to be made on direction for the future.  When it comes to bugs, there's no controversy - fix them!  When it comes to product choices (what functionality should we have?) or design decisions (what color should it be?), the answer isn't always obvious.  We're going to introduce a formal decision making process which is outlined below.

### TL;DR

* Anyone is free to make suggestions, in fact, encouraged to do so
* A steering committee will be organize to provide direction beyond public suggestion
* All suggestions will be voted on via Slack
* Anyone can vote
* Votes are weighted by number of contributions
* 85% agreement is a majority
* Accepted proposals are converted into waffle.io cards for other contributors to work on
* Declined proposals are encouraged to resubmit in light of criticisms given during the voting period

Join our Slack channel via the widget on our [Contact Us](https://dataskeptic.com/contact-us) page.

### Details and Discussion

I'm finally getting around to accomplishing my next steps on OpenHouse, primarily, around implementing more frictionless ways to contribute.  Stay tuned for a few announcements on this, and our forthcoming epsiode featuring OpenHouse on Data Skeptic.

I've started to realize that certain steps forward are inherently opinionated.  For example, which content should we feature on our [Open House Gallery](http://gallery.openhouseproject.co/) page.  Right now it's a map, two rotating visualizations, and a table.  Could this be improved?  Absolutely.  Is the ideal design derivable from first principles?  Not at all.

I'd like to provide opportunities for people early in their product or design careers to make proposals for direction and have them seriously considered.  That's happened several time's in the project's life, but it's always been by the contributor making an appeal to me as the lead, and relying on me to follow through.  I have a plan to make this process simpler so people can contribute vision, not just bug fixes and code contributions.

For any current or future contributor, if they have an idea for an improvement, they can email it to kyle@dataskeptic.com with subject line "OpenHouse proposal".  We may introduce an automated system if I get a lot of these.  If so I'll update the docs here and notify emailers.  These will be written up and added to our [Trello board](https://trello.com/b/KsxRcumo/openhouse-roadmap-choices) under "Product Decisions" or "Design".  We will also generate requests in these Trello lists as a means of requesting "call for proposal" style help.

When volunteers come across cards like this and wish to make a contribution, they are free to execute the task requested.  This can be a great way to try one's hand at design or product management for the first time.  Public suggestions are always welcome, and in time, we intend to organize a steering committee that provides a suggested roadmap as well.

When a volunteer works on a "Design" or "Product Decision" task, their completed proposal will be announced in the #OpenHouse channel on dataskeptic.slack.com.  If you aren't already on our Slack channel, you can sign up on the [Contact Us](https://dataskeptic.com/contact-us) page.

Proposals like this will be voted on.  In a moment, I'll describe our mechanism for voting, but first I'll outline the decision making process.  We'll give 7 days for discussion on the topic and voting.  Anyone eligible to vote who does not give an opinion in 7 days shall be considered to have abstained.  Of the collected votes, an 85% majority will be required for agreement.

Note that a failed vote need not be the end of the road.  Negative voters are encouraged to provide guidance in the form "I would have voted for this, except it should be green and not blue".  In this way, a voting period might incite vigorous debate ending in a 0% agreement, followed immediately by a new proposal by the same person, which 7 days later ends in a 100% agreement.  In the event that a process like this is occuring, we'll consider allowing only 48 hours for the follow up decision.  These durations are considered important to be inclusive of people with valuable advice to contribute who check Slack somewhat irregularly.  Anyone checking once a week should be aware of all votes.

All votes will be weighted.  The weight will be given by the following formula:

$w = \text{log}(c + 2)$

where $c$ is the number of contributions the voter has made to any OpenHouse github repository.  In this way, someone with no contributions has a weight of $w = \text{log}(0+2) \approx 0.693$, a contributor with one commit has a weight of about 1.10, and a contributor with 100 commits would have a weight of about 4.62.

This weighting mechanism is introduced to provide a bias of decision making power to the people that are actually getting work done on the project.  It is logarithmic too prevent non- or infrequent contributors from having no voice.

In truth, not all commits are created equal.  Fixing a single spelling error in our documentation is much appreciated, yet it ends up getting weighted as equally important as a single commit of 10k lines of code.  Other complications exists... Individual developer style might be to produce more or less commits.  Some contributors might chase only low hanging fruit, while others work terrifyingly taxing tasks for months.  A pendantic user could write a tiny script that automates the correction of a single grammatical mistake rampant in our documentation, each resulting in one commit.  All of this is to say, this approach can potentially be abused even before we start worrying about [Goodhart's Law](https://dataskeptic.com/blog/episodes/2016/goodharts-law).

While the potential for abuse exists, it seems like a rather fruitless pursuit.  Our expectation is that the OpenHouse project is an unlikely target for any nefarious intent.  While it could be that the same people that covered up the Roswell incident, killed JFK, and faked the moon landing are all now heavily invested in real estate and have conspiratorial intent of deconstructing this project, this seems unlikely.  However, in the event that any controversy ever does arise, I'm appointing myself, Kyle Polich, to the position of supreme benevolent dictator for life (SBDL).  My one and only power shall be to override any decisions made if they seem to be in violation of the intent of the project.  If 85% vote to convert the problem into a 0day movie torrent sharing system, expect a veto.  But ideally, this will remain a mythical power.  In the even that the community ever finds me to be drunk with power, it is encouraged that they fork the project.

When a product or design decision has been made, any work to be done to delivery on the agreed objective will be immediately converted into cards on our waffle.io boards which are listed below.

[https://waffle.io/data-skeptic/openhouseproject.co](https://waffle.io/data-skeptic/openhouseproject.co)

[https://waffle.io/data-skeptic/home-data-api](https://waffle.io/data-skeptic/home-data-api)

[https://waffle.io/data-skeptic/home-data-gallery](https://waffle.io/data-skeptic/home-data-gallery)

[https://waffle.io/data-skeptic/open-house-crawler](https://waffle.io/data-skeptic/open-house-crawler)

So please check out our waffle boards above and see if there's anything you'd be interested in working on.  If you're looking to learn a new task, we're happy to help train you.  If you're looking to flex your existing muscles, that's great as well.

If you're keen to contribute from a design or product roadmap point of view, feel free to make suggestions or see our requests for proposals [here](https://trello.com/b/KsxRcumo/openhouse-roadmap-choices).
