## Yet Another Reason to use HTTP Status Codes Correctly

If you are not yet familiar with HTTP status codes, I'll give a quick primer, but the detailed specification from w3 can be found [here](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html).

If you want just enough knowledge, just learn about 200, 301, 404, and 500.  I believe those are the ones you are likely to encounter the majority of the time.  404 you should be familiar with already.  200 means success.

HTTP status codes should be used to convey an extra bit of metadata for the piece of software that is making the request.  In the case of something like a 301 (permanent redirect), perhaps a browser should update your bookmark.  In the case of a non-200 request, a crawler might choose to raise an exception and wait for it's opperator to decide what to do, rather than continuing to crawl pages that might not exist or contain the content that is expected.

I was especially annoyed recently at an airport, where the wifi provider has a terrible implementation.  After connecting, the system first forces you to do a log-in of some kind.  Even if it's free, they usually want you to acknowledge their terms of service or something like that.  While I have no problem with that, I do have a problem with them intercepting these requests and responding with a 200 status code (success).

This poor implementation choice caused me two types of problems.

First, my podcasting app attempted to download some new media that it had discovered but was waiting for wifi to download.  I have it configured this way to avoid using too much data on the cellular network.  The airport wifi system responded with a 200, effectively tricking my app into thinking the media was available when requesting.  It downloaded garbage files (the website asking me to login) instead of the actual content.  Had this been built correctly, my app could have ignored the content and tried again later.

Second, I use a Chrome browser plug-in to automatically open tabs at scheduled times.  This is a critical part of my workflow.  When I encounter some site that I want to read but can't do so immediately, I will often schedule it to "open tomorrow" or "open this weekend".  A bunch of these pages which were overdue to be re-opened popped up as new tabs when I opened my computer.  Again, because the airport wifi improperly handled the requests, not only did that content not appear (login screen instead), but I also lost the record of the page I wanted to review.

Granted, you could blame my podcast app for not validating the file type as valid media.  Similarly, you could blame my tab scheduler for not providing some faculty for reviewing what was recently opened.  However, since both these systems implement the agreed upon w3 standard, I can't blame their behavior.  Why should those app producers bloat their software double checking for the mistakes of other systems?

Responding with inappropriate 200 status when it's anything but that can screw up caching and exception handling.  I wish there were a way of penalizing companies, services, and sites that fail to do so.  Admittedly, it's a relatively minor inconvenience, but one I think developers should take seriously.
