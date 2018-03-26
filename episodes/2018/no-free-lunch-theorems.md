## The No Free Lunch Theorems

What's the best machine learning algorithm to use?  I hear that XGBoost wins most of the Kaggle competitions that aren't won with deep learning.  Should I just use XGBoost all the time?  That might work out most of the time in practice, but a proof exists which tells us that there cannot be one true algorithm to rule them all.

This episode is titled "No Free Lunch Theorems" (plural) because there are to well known theorems bearing the same name.  NFL for optimization and NFL for machine learning.  There's room for further NFL type proofs.  What they share in common is that they state that certain classes of algorithms have no "best" algorithm because on average, they'll all perform about the same.  Athletes that compete in the Olympics might be assumed to be outstanding athletes.  However, no one athlete is going to win gold in every event.

The core observation for understanding theorem is to know that a NFL theorem consider applying two algorithms over all possible problems.  Assume we have a large dataset from which we drew this sample:

|Food item   |Has seeds|Is Red|Is Vegetarian|Contains Dairy|Contains Meat|Is a root||Is Vegan|Could be Kosher|Is a Fruit|
|------------|:-------:|:----:|:-----------:|:------------:|:-----------:|:-------:||:------:|:-------------:|:--------:|
|Carrot      |No       |No    |Yes          |No            |No           |Yes      ||Yes     |Yes            |No        |
|Cheeseburger|No       |No    |No           |Yes           |Yes          |No       ||No      |No             |No        |
|Eggs        |No       |No    |No           |Yes           |No           |No       ||No      |Yes            |No        |
|Apple       |Yes      |Yes   |Yes          |No            |No           |No       ||Yes     |Yes            |Yes       |
|Pineapple   |No       |No    |Yes          |No            |No           |No       ||Yes     |Yes            |Yes       |
|Soba noodles|No       |No    |Yes          |No            |No           |No       ||Yes     |Yes            |No        |
|Red Potatoe |No       |Yes   |Yes          |No            |No           |Yes      ||Yes     |Yes            |No        |

While this table contains too few examples, you can imagine where a large training set in this format might allow you to train a machine learning model that predicts any of the last three columns.  In fact, for exact of these three use cases, we can expect our machine learning algorithm to output a model which has high interpretability, even without a tool like [LIME](https://dataskeptic.com/blog/episodes/2016/trusting-machine-learning-models-with-lime).

There are any number of classifications we might be interested in predicting, such as whether or not Yoshi (our lilac crowned amazon parrot) would eat the particular food.  From the list above, she'd eat everything there!  Any assignment of true/false values are a possible "problem" that we might want to solve with machine learning.  For the three examples above, surely machine learning will be successful at making predictions given sufficient training examples.  Yet, if we allow any assignment of values, then we're talking about a lot of possible functions we might want to learn.  When we think that broadly, the NFL theorem tells us that there's no one "best" algorithm.

While this is a correct proof, it can sometimes be taken out of context.  It doesn't mean that some algorithms aren't practically better than others.  The NFL theorem considers the space of all possible functions to be learned.  In practice, we are probably only interested in a small subset of all possible functions.  If you could find a way to rigorously define which problems are "interesting", perhaps you'd be able to prove that one particular algorithm is universally better than another when applied only to the interesting ones.
