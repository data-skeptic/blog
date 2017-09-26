## Feature Engineering Github Commits

I got a great question from a listener, a snippet of which is below.

> I have a question about how to provide context to data fed into ML algorithms. For example, I was thinking about how to predict the next git commit in a code repository. While training the model it seems crazy to input and output the entire repository because most of the time >99% of the code will remain unchanged. It seems more plausible to train on code diff's from one commit to the next. BUT, then the context of the git commit within the repository as a whole would be lost.
>
> I could see a similar problem for predicting the next sentence in a novel. How can you train that model efficiently while still keeping the context of the beginning part of the novel?

This is a great question for two reasons.  It highlights a very real world use case that isn't typically covered in your average ML class, and its about a dataset I've long thought had tons of untapped potential: predicting *things* from the data available on the github API.

The best answer comes down to what *thing* exactly we want to predict.  For example, a question like "which contributor will make the next commit?" has strong sequential properties, and I might tackle that with a recurrent neural network.  If the question was "how many commits will happen today", my instinct is to use ARiMA as a first stab.

Other predictions we might want to make could include:

* Does a given commit have a bug in it?

* Who will make the next commit?

* How much time will pass before the next commit occur?

* Does the most recent commit make the branch ready for deployment or is it still a work in progress?

* Is a given pull request likely to get merged into the project?

These are all interesting questions, but each require a slightly different approach.  To keep focused on the discussion about feature engineering, let's explore the question "Who will make the next commit?"

A common, useful feature in a lot of machine learning applications is to check how many times some previous thing has happened.  To predict if a transaction will be declined, have a feature counting the number of previously successful transactions available.  To predict a student's grade, their existing GPA is a useful baseline feature.  In this case, I'd expect that the most likely next committer is probably the same person as the most recent commit.  If true, an ML algorithm should pick up on this and find it very useful for projects with dominant contributors or contributors who, like me, often make a burst of several commits in a row.  That said, this is a useful but somewhat boring feature.

Another interesting personal example comes to mind.  If you review the commit log for dataskeptic.com, you'll find that when I make commits that affect a large number of files and use an uninformative commit message (e.g. "updates"), then you'll often find that my colleague Gleb will make the next commit in which he fixes a bug I introduced :)

The listener keenly notes that using the entire repository commit history seems like a bad choice.  It's actually rather impossible as most ML algorithms and approaches will require a consistent set of columns in the training set.  In other words, how do we normalize a short commit history and a long commit history to the same length?

To address this you typically need to do some clever feature engineering.  One common way is to include the most recent N events only as features.  A way I find more useful in general is to create features based on counters and rates.  For example, the number of commits in the last N days or the ratio of lines of code changed in a given commit compared to the number of lines changed in the last N days.  Techniques like this allow one to "flatten" a long history into a fixed length of features.  This does present some challenges between the training of the model and the actual production use, but the predictive power of such features generally justifies any hassle involved.

Most repositories have a long tail of contributors.  Even on large projects, I find the 80/20 rule tends to apply - 80% of the commits come from 20% of the commiters.  In this context, it would be particularly difficult to include every contributor as a factor in the model.  Approaching problems like this might require special modeling of the top N contributors or perhaps top P% of contributors.

Although I doubt if it would be worth the time investment, there could perhaps be some advantages in doing some curve fitting on things like the distribution of frequency of commits.  The optimal parameters to those curves could potentially be useful features.

Other metadata to look at could include things like:

* average lines of code changed per commit

* ratio of new files to modified files

* ratio of new lines of code to altered lines of code

* average number of files modified per commit

I expect the most useful features available for any prediction on a repository will have to do with the rate of certain events (e.g. ratio of commits this week to last week).  There also seems to be potential in the commit messages.  Every commit requires some message to be included to describe what the commit is about.  Yet, I've observed a common behavior (even amongst respectable developers) of providing next to useless commit messages (e.g. "updated", "wip", "commit", etc).  My initial intuition is that commit messages are fool's gold.

For the domain we're discussing, it seems obvious that more recent history should have a lot more value than the total history of a github repository.  There are likely motivations to build features off a finite horizon of data or discount older data in some way.

When tackling problems like this, I think it's important to consider the intuitive predictability of the task at hand.  Predicting if a given commit has a bug in it seems almost like a hopeless task.  Not just because of the Halting Problem, but because finding bugs is a non-trivial task.  Having said that, we can also say that the task we'd ask of a ML model is to detect the likely presence of a bug, *not* to find the bug itself.  In this way, its more like meta-bug finding.  It could be possible for a model to identify the tell-tail signs of a problematic commit.  Yet there's certainly still some upper limit on how predictable such an outcome can be.  Its important to ask questions about what seems plausible given the available features to the training.

All in all, the issue of training a model to recognize something about the current state of a system for which one possesses a history / audit trail / transactional log is a common but challenging problem.  It's usually tackled through clever feature engineering that summarizes the history in a meaningful way.  Predictions based on github commit history is an area that might just have some exciting low hanging fruit.