## Kalman Filters

A Kalman Filter is a technique for taking a sequence of observations about an object or variable and determining the most likely current state of that object.  In this episode, we discuss it in the context of tracking our lilac crowned amazon parrot Yoshi.

Kalman filters have many applications but the one of particular interest under our current theme of artificial intelligence is to efficiently update one's beliefs in light of new information.

The Kalman filter is based upon the Guassian distribution.  This distribution is described by two parameters: $\mu$ the mean and $\sig$ the standard deviation.  The procedure for updating these values in light of new information has a closed form.  This means that it can be described with straightforward formulae and computed very efficiently.

You may gain a greater appreciation for Kalman filters by considering what would happen if you could not rely on the Gaussian distribution to describe your posterior beliefs.  If determining the probability distribution over the variables describing some object cannot be efficiently computed, then by definition, maintaining the most up to date posterior beliefs can be a significant challenge.


