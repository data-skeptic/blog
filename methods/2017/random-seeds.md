## Random Seeds

I had a listener write in and ask a follow up question related to a discussion I had with [Daniel Whitenack](https://twitter.com/dwhitena) on a [recent episode](http://dataskeptic.com/blog/episodes/2017/data-provenance-and-reproducibility-with-pachyderm).  The listener was just starting to get into machine learning, and asked an interesting question people in a similar situation might benefit from hearing the answer to.

I asked Daniel about reproducibility on models that have inherently non-deterministic characteristics.  If you're new to the field, you're going to encounter a lot of jargon around this point.  The words stochastic, random, non-deterministic, and ergodic might all be used to describe things.  Each of these ideas is distinct and important in it's own right.  Yet, they all more or less mean the same thing when discussing the behavior of algorithms that generate machine learning models.

I'm going to adopt the phrase non-deterministic as my own personal word choice, and I'll explain precisely what I mean by it first.

A deterministic system is one which behaves in an entirely predictable way.  If you know it's current state and any changes being done to it, then the next step is knowable.  At no point does a deterministic system flip a coin to pick between left and right.  The choices are locked in forever from the moment of the system's creation.

A deterministic system is a bit like chess, given the players moves.  The pawn never rolls a dice and moves that many spaces ahead.  If the move is declared, the next board configuration is unarguable.

Non-deterministic systems, on the other hand, have some decision step made by chance.  Whether this decision is made by an agent interacting with the system, or is a metaphorical coin tossed by the system itself, a prediction of the future cannot be perfectly done.  One may have a perfect understanding of the statistical nature of the system, but this just quantifies the uncertainty.  A backgammon player can strategize about the game, but their strategy must account for the fact that a dice roll is going to introduce uncertainty about their future.

To some, it might sound like deterministic algorithms are in some way prefered.  I'd rather own a factory which is perfectly predictable than one which might do unexpected things.  In a deterministic factory, all potential failures or slow downs can be predicted and prevented.

There's an interesting discussion worth having one day about a computational theory perspective on that idea.  What if your factory was deterministic but calculating the failures took too much computational time?  That's a fun discussion for another day.

There's no intrinsic preference you should have between deterministic and non-deterministic algorithms.  You should prefer whichever class solves the problem you have.

Sometimes deterministic algorithms come with wonderful proofs of useful features like a guarentee of convergence.  These proofs are generally rigorous derivations which show mathematically that regardless of input, a particular algorithm on a particular class of datasets will always arrive at an answer within a finite amount of time.

If that sentence reads a bit like a legal contract, it's because I'm being very careful not to say something wrong related to computational theory.  A monumentous result is computer science is the [Halting Problem](https://en.wikipedia.org/wiki/Halting_problem), first described by Alan Turing.  The conclusion states that a particular negative statement is true.  Let's imagine you'd like to build a computer program which examines other computer programs and determines if the input program will eventually exit when given a particular input.  It is proven that this "inspecting" computer program cannot exist.

Why not?  We have virus scanners that scan other programs.  Virus checkers are not known to be perfect, and they're not expected to work on all programs and all inputs.  They try to identify virus software only, and they can be confident they'll give an answer to any input software because they're doing a limited check.

So when I say some algorithms come with nice properties like provable convergence in a finite time, they're able to do this without violating the halting problem result because they're only checking one single algorithm against a closed set of possible inputs you could give it.

Non-deterministic algorithms, on the other hand, rarely have such proofs of guarentee.  If there's any random component, there's always the possibility of getting the worst streak of bad luck possible on your random selections, and never finding a result.

Yet, many machine learning practitioners have found situations to prefer the non-deterministic models, often for their accuracy.  What we lack in the types of properties sometimes proven for deterministic algorithms, we gain in some statistical properties.  Occasionally, these get proven.  Something a bit like the central limit theorem kicks in and we have a nice probabilistic guarentee of some kind.  But sometimes, we also get empirical experiences like "it just seems to always converge and work pretty well even though we don't have a statistical arguement for why that's the case."

Non-deterministic approaches in machine learning are winning most contests, and I have a feeling we'll eventually start seeing novel proofs of some of their statistic properties, giving us more confidence for their effectiveness which we might take a bit on trust today.

I don't think I really have to build much of a case for a machine learning practitioner to use non-deterministic algorithms, but I wanted to do some compare and contrast here before talking about practical implementations.

If two people use the same identical code to generate a model, but that model is created in a non-deterministic way, then we have absolutely no guarentees that they'll end up with the same model.

I'll make a stronger statement: in the general case, we can say for certain that the models being identical is fleetingly unlikely.  A bit by bit comparison of the two models will almost never find them to be copies of one another.

Yet, these models could be behaviorally equivalent.  If my model to predict $y$ from $x$ is of the form $y = x \cdot 8 / 2$ and your model is $y = x \cdot 4$, then a string based comparison of serialized versions of our models are not equivalent.  Yet, for every input, we'll return the same output.

This idea could be carried further into models that are "more or less" the same, responding to particular inputs with the same output in a large percentage of inputs, and differing only on a small percentage of inputs.  If you have a well posed problem with a unique solution, this is probably what your result will be.

If your problem has a unique solution which can generally be found in the given time period of your choosing exists, then multiple runs of your algorithm, all making choices in part informed by randomness, will almost always find this unique solution or tiny variations similar to it.  Some rare set of runs might have really bad luck and never find anything close to the one unique solution, but that should be rare and somewhat noticable.

A problem with many solutions might consistently good solutions, which is also a nice result.

A problem for which your algorithm isn't smart/capable enough to finding good solutions or cases when you have too small a dataset or too limited of computational resources, your results will vary a lot by the algorithm of choice.

Thus, it is important to try and reproduce your own result from multiple runs and compare them.  The variance in the produced models will tell you a lot about how good of a job you're doing looking for a solution.  I think most data scientists working on larger scale problems spend most of their time in this stage - disecting the output model, comparing it to other runs, and looking for possible points of failure to correct.

You want to run your machine learning algorithm multiple times, and you want to see how the non-deterministic nature plays out by having them all randomize differently.

A technique I want to recommend is always starting your runs from a different random seed which you carefully track.  Let's say you generate 10 models on the same input data, and the cost of doing so (cloud computing cost and time spent waiting) is prohibitive.  If 9 out of 10 of those models are more or less behaviorally equivalent, but 1 out of 10 has a much higher accuracy, wouldn't you want to know why?

We should go in with a suspicion of overfitting while sticking to innocent until proven guilty.  In practice, I rarely see.  I find most often the variance across models is somewhat nominal.  But sometimes I want to regenerate an exact model.  Other times, I might be working in a sensitive environment, knowing that in the future, someone might want to deeply audit a particular decision made due to it's significance.  To do that, you need to keep the random seed you used.

So long as you can rely on your computer to generate the same sequence of random bits from the same starting see, a non-deterministic algorithm, once seeded, becomes a deterministic one.

When I start a project, I typically my random seed as I build up my code.  If I'm bug hunting or checking things, I want a deterministic response so I'm not chasing after ghosts.  Once I've got my code up to speed, I start randomizing that seed, and always tracking outputted model with it's starting seed.
