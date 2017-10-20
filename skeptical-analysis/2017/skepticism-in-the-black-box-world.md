## Skepticism in the Black Box World

In recent years, much discussion has taken place about machine learning models being black boxes.  Some models are said to be so complex that a human can't comprehend the function these models compute.

Whether implicit or explicit, many commenters will describe this as a negative feature of those models.  I entirely disagree and find these objections to be rather misleading.  At the end of the day, a model is a tool like any other.  When I encounter a tool I don't think works well, I abandon it.  This is an easy thing to do if that tool is something like a voice recognition API.  If I'm dissatisfied with the results of one, there's a free market of other tools I can test out.

Yet those who complain the most about black box models typically point to use cases like criminal sentencing or hiring/firing decisions.  In fact it's true that the justice system has adopted models that have been shown to be rather definitively biased.  In my opinion, it was a mistake to start using such tools.  The question we should be asking is who approved the adoption of the tool without adequate inspection?  Asserting that models have no place in such proceedings is pure alarmism.  In a world where judge's pass more lenient sentences after lunch than before, clearly there is room for improvement.  *Properly applied* data science should certainly be a contributor to those improvements, ideally in an open source and transparent way.

Let's say you have a decision to make.  You are given access to two different models that make a prediction/recommendation to help you in your decision making process.  Both models boast identical diagnostics.  Accuracy, F1-score, true positive rate, and every other metric shows us that these models have equivalent predictive power.  One model is so complex, one can only look at it's inner workings by a careful study of rote arithmetic, calculating layers of transformations from input to output.  The other model is clearly stated in the form of a few parameters that have intuitive definitions.  Of course, we should all prefer the intuitive model in this case.

What if the complex model boasts significantly higher accuracy?  Should we always chose it?  Not always.  Interpretability certainly has value.  Depending on the use case, there's a strong argument for preferring interpretable models, and our criminal sentencing example exemplifies it.  An interpretable model in that case allows inspectors to raise objections.  A dependence upon zipcode, for example, can readily be pointed out as a possible correlate with a demographic feature, implying the model carries an unjust bias.  On the other hand, it's important to note that the absence of any reasonable objects also leaves us with no grounds for objection on the basis of possible bias.

What if instead of criminal sentencing, we were considering purchasing a home.  Two real estate models offered to you attempt to predict the future value of the home.  One is complex and boasts a very high accuracy.  One is interpretable but has a pitiful accuracy.  I don't know about you, but I'll take my chances with the empirically proven yet complex model to inform my decision.

All models can be tested.  Whether the model is a black box due to the complexity of its internal workings or due to it being proprietary, it can always be inspected through experimentation.  The truth has nothing to fear from scrutiny.

An effective test of any black box system must be conducted exactly like any well designed experiment.  It should clearly state the claim of what the model can do and develop a protocol which can falsify the claim.

Yet even before we talk about experimental design, we can talk about a few useful heuristics that can better inform an aprori skeptical point of view.

I like to ask two important questions about any truly impressive claim I hear related to machine learning or artificial intelligence.

1) Would I expect a modestly well trained human to be able to perform the task performed by the model?

2) Would i be skeptical of a claim that a human could perform the task?

3) Does it seem reasonable that the training data could contain enough information to allow the performance of the task?

Let's first consider these heuristics applied to medical diagnosis.  We've seen many recent advancements in deep learning applied to medical diagnosis.  In fact many former guests of the podcast developed systems that claim to achieve human level accuracy.  This is truly an impressive feat of these researchers.  Yet, it definitely fails the first test.  If a well trained doctor can perform a diagnosis with some accuracy, then eventually a machine will be able to do the same.  The doctor is just a sensor array and a processing core.  Machines can be constructed with similar sesnor arrays and processing cores.  We cannot take for granted that just because we can imagine a computer performing a task, that surely one does.  But in other domains this heuristic is very useful for forming an initial opinion.

On the other hand, let's apply this rule to the stock market.  We know that the majority of stock traders perform no better on average than buying a simple index fund.  If a hedge fund claimed a consistent 40% return above this baseline, we have good reason to start from a position of skepticism for a number of reasons.  Most notably in this context, the first rule heuristic above.  This is not to say that a trading algorithm cannot possibly out perform humans.  Perhaps one will eventually be invented that does.  There's not reason to assume that machines are limited to the maximum precision of what humans can achieve.  But for difficult tasks, human experts are a worthwhile benchmark to always compare agains.

This leads us to the second heuristic - would I be skeptical if a human being accomplished the feat.  Given what I know about markets and how they are distructive to information, I am very skeptical of any the claims made by many financial professionals.  I apply the same skepticism to algorithmic traders.

What about medical diagnosis?  We are now seeing results in the literature of some models outperforming human experts on certain classification tasks.  Results like these will continue to grow.  There will probably come a day when certain medical diagnosis are left entirely to machine learning, when they are demonstrably superior to their human equivalents.  However, these "better than human" results are often marginal improvements.  If a doctor emerged into the public eye stating that they've spend 80 hours per week for the last 10 years focused exclusively on studying one very specific diagnosis, and that their accuracy exceeds all their peers by a marginal amount, I would not be immediately skeptical of this claim.  Thus, many medical imaging breakthroughs pass this heuristic, paving the way for plausibility and further testing.

Now to our last heuristic - is it reasonable to think the training dataset has enough information to enable the model to achieve the stated results?  This is, of course, a case by case consideration.  Correctly classifying a skin condition with 99.99999% accuracy does not seem unachievable.  Correctly classifying the remaining lifespan of a patient with this accuracy is patently absurd regardless of the amount of data collected on their medical history.  A wide gradient of possibilities exists in between.

As you hear claims of impressive machine learning models, I'd be curious to hear if you find my heuristics useful in your analysis.

