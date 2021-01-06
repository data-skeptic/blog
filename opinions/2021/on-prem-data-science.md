## On-prem Data Science

I've helped several companies transition their data science efforts from on-prem solutions to the cloud.  Many years ago, this sometimes involved convincing executives that it was the right choice.  Today's executives know the cloud is typically the best solution and instead ask _how_ to make the transition.  Yet, there are still cases in which it's not clear what the right choice is.

When making a decision like this, there are four key areas to consider:

* Finance
* Efficiency of human capital
* Security
* Low level tech stack needs


### Finance

Almost ever startup has to go through the growing pains of getting a series of sensationally high bills from their Cloud Provider (AWS, GCP, Azure, etc).  This can sometimes lead inexperienced founders to fear the cloud, rather than optimize their usage of it.  When you consider the total cost of ownership, the cloud is almost always the fiscally responsible choice.  Thinking of the purchase of hardware as a one time cost is an easy mistake to make.  Maintenance costs are typically underestimated as is the time lost when auxiliary engineers outside your IT Ops group are pulled in to help solve especially puzzling problems in setup and configuration particular to your instance.


It's also easy to under-estimate how cloud savings can be achieved as the organization grows.  Cloud accounting is actually fairly intricate.  Most software engineers are not familiar with the intricacies of cost savings and reserved instances, nor are they often interested in these features.  Cost optimization for cloud infrastructure is actually a lucrative consulting practice for many professionals who specialize in this area.  Not considering how to minimize the bill is another way in which costs can get skewed.

The somewhat rare exception in which on-prem hardware can make sense for your data science needs is when you require GPUs for training or inference.  These machines are especially costly in the cloud and I have been in the room when it was rigorously determined that a cost savings could be achieved with a small GPU focused data center or rack is set up.  Even still, one needs to carefully consider the long term use.  Is your team really going to be running all those GPUs at 100% and taking advantage of the hardware you bought?  Or will they do that for a few months, solve the problem, and let them mostly sit idle?


### Efficiency of human capital

New professionals enter the job market with training focused on cloud development.  While everyone has the potential to develop, empowering people to lean into their experience rather than learn a new path is almost always more efficient.  On the rare occasion when a cloud provider is down, your data science team can leverage the paid support contract you have with your cloud provider.  That support team is there singularly to alleviate urgent problems.  As will inevitably happen more often than the cloud provider, your on-prem solutions will go down.  Your team will need to be taken off their other duties to attend to the urgent problem.

Invariably, on-prem solutions require more training, can often promote home-grown approaches over proven technology, and pose a risk of making your team less efficient.


### Security

The most common reason I hear about companies starting or expanding on-prem solutions is for security purposes.  Depending on what you mean, this can be valid or invalid.

I occasionally meet professionals who hold the opinion that their deployments are more secure than what a cloud provider can offer.  This is possible, though not likely.  The cloud providers have entire teams dedicated to security.  They fight attacks and patch vulnerabilities across a wide portfolio of customers.  Often they have direct channels with key vendors or software providers.  They have the capital to entice the best talent money can buy and a motivation to do it.  They have teams whose entire mission is to keep software patched and up to date while delaying questionable patches that might not be urgent.  Are you seriously going to be Goliath?

Despite my cynicism, there are some valid security use cases for when on-prem solutions are the right choice for data science projects.  In the simple case, when local law requires it and the cloud providers haven't yet developed compliant solutions!  But in all such cases, that's temporary.  Cloud providers will always need to prioritize compliance with laws to maintain a presence in the area.


I've encountered executives who genuinely express a concern that the cloud provider (typically AWS) has the option to "peek" into the companies data.  In my opinion, this is "we didn't land on the moon" level of crazy.  It would be wrong to say that it's impossible Jeff Bezos took time out of his day to log into your private server and run some queries against your database, but I suspect he's got other things to be doing.  Yet could a rouge employee do something?  What about a government making secret requests which the cloud provider is forced to comply with and not notify you of?  There's plausibility in these arguments.  If your client data is _extra_ sensitive for some reason (e.g. medical health records), perhaps some component of your work should be managed on-prem.


### Low level tech stack needs

If industrial equipment, IoT, or edge computing are important topics to you, it's likely an on-prem solution is required by the problems you face.  Whether due to limited network access or a need for very low latency, many companies have no option but to leverage some on-prem solutions.  Most such companies are always working in a hybrid model.  The interesting questions are around how to most effectively make decisions locally while shipping the data efficiently to the cloud.

If you want to leverage machine learning but a cloud hosted REST API can't satisfy your latency demands, you're going to need to get creative!  While many offerings now exist to help you, phase one of your project will be making important build, buy, acquire decisions.  Ultimately, _something_ is going to be custom.

If possible, look for opportunities to train your model in the cloud while deploying as an on-prem for inference.  Truthfully, I believe this covers 90% of industry use cases.  The two exceptions being when models need frequent updates or when feature engineering needs to be done in real time.


## Strategies for effective hybrid infrastructure


### Environments, Environments, Environments

Your core dev ops teams should protect and maintain your production environment.  Depending on how you run your organization, they may provide a small or large list of additional services to other departments and teams.  Most of all, your dev ops team should lead by example without getting in the way.

A contention often exists between a data science team's needs and the services provided by a traditional dev ops group.  While "machines as cattle, not as pets" is indeed a wise strategy, there can be ad-hoc needs in the R&D phase of a project that need not be slowed down with process.  Teams and sometimes individual developers often benefit from having their own sandbox environment.  Use of such environments should be encouraged, not discouraged.  If the need of a data science team don't fit the template menu of solutions, then that menu probably needs to be improved.


### Embrace the tooling

Any successful strategy is going to require use of `docker`.  With the exception of any serverless components, all your software should be running in a `docker` container.  This makes your software truly universal and erases the configuration and setup nightmares of yesteryear entirely.

Similarly, the most popular infrastructure-as-code service `terraform` can help you deploy to the cloud or on-prem solutions alike.  Out-of-box, `terraform` makes it easy to deploy to all the major cloud providers.  Further, it supports a notion called a "Provider" which allows for user defined destinations to be implemented if necessary.  Even for complex cloud architecture, it's often the case that you're going to copy and modify a convenient starter script, rather than invent one from scratch.  Rarely is your infrastructure a completely unique snowflake.


### Fake your data

You take security seriously and want to do everything you can to prevent, detect, and mitigate intrusion.  Despite your best efforts you're still at risk to 0day vulnerabilities, rouge employees, and physical hacking attempts.  Assume the worst.  You've been breeched.  But what if all the intruder found in the safe was Monopoly money?

You can't fake your production data, but you can probably fake the rest of it.

A common practice is to make a replica of production data for analytical or development purposes.  Rarely does this data need contain personally identifiable information.  So scrub it!  Add a small amount of gaussian noise to some values to increase anonymity.


This can also be taken a step further where the entire environment is generated data - 100% fiction!  If this is appealing, you will need to invest a bit of effort into the software you use to generate this data.  If too simple, it will prevent your analytical or data science efforts from being successful.  But without a doubt, great progress can be made on fake data before ingesting production data in the final leg of your journey.


### Only as custom as necessary

A side benefit of modern cloud architecture is that developers are forced to do things the "cloud's way".  In my experience, this means it's more common for best practices and standard practices to be followed.  When a new engineer joins the team, can they get up to speed by only reviewing code and documentation?  If not, how long of a training must they go through?  How many of their colleagues have the institutional knowledge to give that training?

On-prem often seems to imply a culture of custom approaches.  There's too much to build.  No matter how talented your team is, they can't do it all.  Especially in your own data center, ensuring that your minimizing on custom approaches will pay great dividends in the technical debt you avoid.



## Recommended for further consideration

Looking for something to read next?  Here's a few suggestions.

[The Twelve Factor App](https://12factor.net/) - A short but thoughtful treatise on application development.  I'm a huge fan and can assure you that a design philosophy like this will give you the code portability that you surely need if you're interested in on-prem data science.

[Terraform Providers](https://registry.terraform.io/browse/providers) - Remember when I mentioned Terraform's Providers?  They have a bunch!  Surely something will be useful for your infrastructure.

[Data Science Tools and Other Announcements from Ignite](https://dataskeptic.com/blog/episodes/2017/data-science-tools-and-other-announcements-from-ignite) - An episode in which Kyle talks to Joseph Sirosh (Microsoft V of Cloud AI) about some recent Azure announcements.  It's an older episode now, but take note of the amount of thought cloud providers are putting into how to make their offering more enticing then your home grown on-prem solution.


