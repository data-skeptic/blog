## Being Bayesian

This episode explores the root concept of what it is to be Bayesian: describing knowledge of a system probabilistically, having an appropriate prior probability, know how to weigh new evidence, and following Bayes's rule to compute the revised distribution.

We present this concept in a few different contexts but primarily focus on how our bird Yoshi sends signals about her food preferences.

Like many animals, Yoshi is a complex creature whose preferences cannot easily be summarized by a straightforward utility function the way they might in a textbook reinforcement learning problem.  Her preferences are sequential, conditional, and evolving.  We may not always know what our bird is thinking, but we have some good indicators that give us clues.

For example, Yoshi will often make distinct squeals to indicate delight.  Often, upon encountering an especially appetizing morsel, she might make this delight sound.  However, she can also make the sound for reasons other than delight at the food (type i errors) and she might be very happy with the food yet not make the delight sound every time (type ii errors).

In this way, the delight sound is an imperfect measurement.  It gives us some information from which we can infer her preferences, but not perfect information.

Bayes theorem takes this familiar form:

$P(A|B) = \dfrac{P(A|B) \cdot P(B)}{P(A)}$

In this situation, let $A$ be the fact that Yoshi likes a particular food and let $B$ be the event of the delight sound occurring.  What we'd really like to know is whether or not she likes the food.  Yet, she cannot tell us directly.  So we apply Bayes theorem to transform this conditional probability to the one on the right side of the equation.

Now we have $P(A|B)$, or the probability that she lives the food *given* that she made the delight sound.  

This is followed by $P(A)$ or our *prior* probability that she likes the particular food.  Where does $P(A)$ come from?  In our simple example, we'd probably use our personal best estimates to define the prior.  That's not particularly rigorous, but it works.

Near the end of our conversation we finally touch on the fact that doing Bayesian inference can often be quite computationally expensive, but that under certain assumptions or conditions, there may be efficient solutions.  A great example of this is the Kalman Filter which is a special case in which Gaussian distributions (defined by parameters $\mu$ and $\sigma$) are a sufficient statistic for describing all acquired knowledge elegantly with two parameters.
