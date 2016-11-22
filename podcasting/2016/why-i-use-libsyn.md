## Why I Use Libsyn

From time to time I get asked by new and aspiring podcasters how to get started and grow an audience.  In particular, someone asked me where to host their show, so I decided to share some thoughts here.

Data Skeptic uses a service called [libsyn](https://www.libsyn.com/).  Here's why I choose it.

When I decided to start podcasting, getting started looked very easy to me.  I already had some basic audio recording equipment and I quickly discovered that Podcasts were nothing "fancy" from a technical perspective.  A podcast is just a RSS feed the contains some metadata about episodes and a link to where the MP3 files can be found.

I was initially planning to put my files on a CDN somewhere (most likely Amazon S3) and write a cronjob that polled that location looking for new files, and re-wrote the feed file when new elements were uploaded.  Simple.

My hesitations started to arise first and foremost around tracking.  I wanted to know who was listening, and I wanted those download numbers to be a sort of secondary feedback mechanism so I could see what types of content were most appealing to my audience.  Although the basic Libsyn package doesn't give you stats, the still affordable $7/mo plan does.  There's a few limits there around your ability to drill down.  To be honest, I once upgraded to see the more advanced stats, but found them static and a bit uninteresting after one review.

I also chose Libsyn because they are (to the best of my knowledge) the largest host of podcasts.  No podcatcher (does anyone still call it that?) in the world is going to build their software to without compatibility for Libsyn feeds.  Similarly, if iTunes (the dominant source of listens for me, as it turned out) is presumably talking to the Libsyn folks about any new features or changes they're planning.  My expectation is that Libsyn would "have my back" in any such changes or new options.  Also, I thought having a *.libsyn.com feed address might get me crawled and indexed by the long tail of sites doing something with podcasts.  I'm not sure how fruitful that last part has been, but it was part of my thinking.

My podcast has grown tremendously over the last two years in both listenership, quality, and scope.  It was overdue for me to rebuild the show's website recently.  What was previously a static site now has a backend database.  I found that it would actually be quite easy to replace Libsyn since I have basically all the software in place managing my podcast as is.  All that's missing is a script to render the database of shows to the right XML format triggered on any new episode insert.  Despite that option, I plan to stay with Libsyn for two reasons.

First, because I've never had a single issue.  My show has never been down or inaccessible.  I can't recall any downtime on their site, much less the accessibility of my episodes to my audience.  I trust Libsyn for reliability.  On the occasional cases when I hear from fans that they're having a problem listening, I can pretty confidently assert the issue is on their end, and help them diagnose, rather than checking my own logs or setup.

Second, because I hope we'll see new innovation coming from Libsyn.  I'd much prefer an API where I could push new content and pull back my stats.  I have no idea if that's on their roadmap, but as podcasting continues to crawl into the mainstream, the demand from a wider set of producers is likely to necessitate innovation in podcast hosting.  I'd rather they build it than me!
