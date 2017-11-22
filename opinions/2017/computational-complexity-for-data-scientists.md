## Computational Complexity Theory for Data Scientists

As was announced a while back on the Data Skeptic podcast, the show is going to have running themes for the foreseeable future, in which we'll spend a few months talking about one topic or area.  We more or less did this earlier this year when we focused on deep learning following by a few episodes on deep learning in medical applications.  These themes will become more formal and more obvious going forward.

From October 2017 to the end of the year, we're focusing on the field of computational complexity theory.  At a glance, this is a discipline might not seem to heavily overlap with what most people consider data science.  I imagine it also won't seem naturally connected to scientific skepticism in most people's minds.  Our episodes and a few blog posts will help make the links and overlaps more illuminated.

I would also argue that complexity theory has made important contributions to logic and reasoning.   This field has been forced forced to seek out new ways of proving things when existing ways are proven to be ineffective.

So why should any Data Skeptic listener care about the theory of computation?  Let me share with you, my top reasons.

## Algorithms

When it comes to an understanding of algorithms, I find people that call themselves data scientists have a wide variance in their expertise.  For some, algorithms (often just machine learning algorithms) can be operated in a very "blue collar" way.  You can study Random Forest, XGBoost, SVM, Logistic Regression, etc., and gain an understanding of how to tune the parameters of these algorithms to good effect.  Surprisingly, this can be done with a very tenuous understanding of how those algorithms actually work "under the hood."

I personally think this is not enough.  I believe everyone should be learning the inner-workings of the algorithms you use.  But I will also admit, there's a lot of low hanging fruit in industry right now.  A basic understanding of how to apply machine learning can take you pretty far.  But eventually, you may have the opportunity to work on a truly interesting problem where the limiting factors aren't business process, lack of requirements, low quality data, or anything else are the inhibitor to progress.  At some point, making progress on a problem requires a very deep understanding of the ways in which an algorithm is *failing* to give you better results than might otherwise be possible.

The more advanced of us are sometimes fortunate to work on problems like that, requiring a deep understanding of the optimization techniques used in those algorithms.  Selecting an alternative loss function, regularizing in a clever way, or tuning gradient descent are exciting topics which aren't always necessary in every real-world problem, but rewarding when they are.

Most of what I've mentioned above could be described as "how does the algorithm work?", but there are important questions of "how long does it take to do it's work?" that are very important to ask.  This is the domain of computational complexity theory.  Ensuring your code has the predicted asymptotic results is a nice check.  If you know the theoretic results to expect, an empirical check of your code can help identify tricky implementation issues or areas where deep code optimization might help.

Knowing about complexity can also help you spot tell-tale signs about the class of problem you might be dealing with when you start getting into something brand new.  Sometimes it's a data scientist's job to convey to an organization that they're over-constraining a problem, and propose a similar but different problem to solve which is much friendly in terms of runtime.

## The Limits of Computation
The growth of the cloud and cheap compute resources have made it easy for people to mistakenly think every problem can be solved by just "scaling up".  Actually, that does work much of the time!  But for some problem, no matter how fancy the processor and how large the datacenter, certain problems are inefficient.  There are limits on what is computable.  Only by getting a very fundamental understanding of some key complexity classes and concepts can you appreciate the types of problems we're going to solve with data, and those that will require heuristics or something else.

## Big Data
In the era of so-called big data, sometimes, the most basic of calculations (like a standard deviation) are actually costly and non-trivial to compute.  Interesting probabilistic algorithms like count-min sketch and bloom filters are approximation tools that trade off some accuracy for speed.  Learning how the algorithms requires understanding complexity.  Applying the same approximation "tricks" in other circumstances may also be beneficial to you.

Parallelization questions in complexity typically fall into class $NC$.

Streaming systems, which have to work with limited memory in order to be fast often fall into various space complexity classes.


## Efficient Solutions
Being able to recognize if your solution is efficient in the *worst* case is critical to launching a web-scape technology.  There's a massive amount of traffic on the Internet.  If you tap into a large amount of it, statistically, you're going to experience a lot of outliers and a lot of worst case situations.


## Approximate Solutions
A good deal of the literature in complexity theory is about all the things one cannot do.  Understanding why a particular problem is hard is often the first step in recognizing how that problem might be approximated efficiently.  Some problems have proofs that they can't be approximated well, while others admit efficient algorithms with $\epsilon$ close optimality.  In real life, that's good enough for me!

## What it means to compute
At it's philosophical core, computer science can be described as the study of what it means to compute.  While thinking in those terms might not have any direct benefit to a data scientist, thinking about the tools we use can only make you more creative about how we apply them in the future.

## Machine Learning for Fun and Profit
In the episode titled [Stealing Machine Learning Models from Cloud APIs](https://dataskeptic.com/blog/episodes/2016/stealing-machine-learning-models-from-cloud-apis), guest Florian Tramèr explained to us how he was able to extract the models used by various cloud services.

What does that mean for you?

Let's say you come up with a very clever solution of some kind.  For example, given a picture of a garage sale item, you predict the market rate for the item by zip code.  Let's assume you've done a stellar job creating this system, and it's highly accurate!  You'd like to turn this into a business.  However, once you give someone your model, its trivial to copy it, and hard to monetize.  What if instead, you set up a web API where people sent you photos, and you returned the predictions.  The model never leaves your server, so the client must continue to pay-per-use to enjoy your creation.  Simple right?

Not quite.  That model can be stolen through some clever techniques, despite the presumed security offered by the veil of the API.  Granted, if your API is static, then it's probably not worth paying much for.  An adaptive, dynamic system might not be as easy to steal, or as useful without the updates, but regardless, the tools of complexity theory can be helpful in asking questions what can be learned about a black box system.

## Relationship to Deep Learning
Speaking of black box systems, we now live in a world where powerful tools are entirely constructed using machine learning.  We can't always tell you *how* our systems work, but we can empirically prove that they do.

What are the limits of learn-ability?  How big must our hidden layers be to solve a given problem?  Questions like these require a good understanding of complexity.

Generative adversarial learning has been a popular technique in recent years.  The adversarial aspect of the process seems to beg some fascinating questions that haven't really been articulated well yet about bounds on these adversarial behaviors.  Many game playing strategies are in complexity classes like $PSPACE$ and $EXP-Time$.

## Artificial General Intelligence
As breakthroughs in AI seem (presumably) to take us incremental steps closer to the creation of a machine that passes the Turing Test, complexity theory is the right tool to ask questions about the limits of mind and machines.  Is there anything a human brain can do that no computer can do?  If you think so, then you have the burden of proof.  What's to stop a computer from doing a very deeply accurate simulation of the human brain?  Is there any reason why that couldn't be done?  Not that I know of, but surly if I did, it would be a result in the language of complexity theory.

## The future
The above sections highlight the reasons I personally think someone interested in data science should care about computational complexity theory.  You'll notice I left off important topics like cryptography.  Very important, but not necessarily to a data scientist.

Similarly, interesting ideas like interactive proof systems and quantum computing just don't make my list, despite the immediate advantages we'd have with fast PCA, matrix inversion, and FFT that we'd get if a large quantum computer could be created.

If you're looking for a good place to start, check out [Introduction to the Theory of Computation](https://www.amazon.com/Introduction-Theory-Computation-Michael-Sipser/dp/113318779X).  If you're looking for something more advanced, [Computational Complexity Theory](https://www.amazon.com/Computational-Complexity-Theory-Park-Mathematics/dp/082182872X) is a nice book to get into after.


