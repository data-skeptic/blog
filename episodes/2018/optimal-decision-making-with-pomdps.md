## Optimal Decision Making with POMDPs

In a previous episode, we discussed [Markov Decision Processes](https://dataskeptic.com/blog/episodes/2018/markov-decision-processes) or MDPs.  An MDP is defined by four parameters in the tuple $\big \langle S, A, T, R \big \rangle$.  These variables are the states, actions, transition function, and reward function, described previously.

An MDP assumes that the state of the world is completely observable to an agent.  This is true in many games, like Chess.  While players cannot directly observe each other's minds and what strategies their opponent might use, the location of every piece is common knowledge to both players.  In this way, the state is *fully* observable.

Yet in many situations, the state is not fully observable.  We can generalize the concept of an MDP to a Partially Observable Markov Decision Process or POMDP, and extend the same ideas to a more general class of environments in which an agent cannot directly observe the full state.

A simple example of a partially observable environment is Texas Hold 'em Poker.  Remember that the true state includes every detail of the game - who has what cards in their hand as well as the order of the cards in the draw pile.  Each player can observe their own hand, but not the hand of their opponents.  Similarly, no players can observe the draw deck, but as the [community cards](https://en.wikipedia.org/wiki/Community_card_poker) are drawn and placed on the table, all players can view them.

The same idea generalizes to more real-world problems as well.  When you negotiate the purchase of a house, both the seller and the buyer have private information.  A smart (often legally required) step in the process is getting inspections and appraisals.  From the buyer's perspective, these services are useful in that they reduce uncertainty about the home.

One problem a homeowner would like to avoid is termites.  A smart buyer can learn some of the visual signs of termite infestation/damage by doing a few basic Google Image Searches.  Those images will equip most buyers to notice obvious signs of termites, but not necessarily train their eye to be keen of all damages.  Perhaps the table below might describe how well a random person can detect a termite infestation.

|              | Found Evidence | Found No Evidence |
| ------------ |:--------------:|:-----------------:|
| Has Termites | 65%            | 45% |
| No Termites  | 10%            | 90% |

The rows represent ground truth.  The columns specify whether or not the prospective buyer believes they found evidence of termites.  When termites are present, the buyer is just a bit better than chance at discovering the evidence, doing so correctly 65% of the time.  Note that this has nothing to do with how likely a home is, in general, to have termites.  Simply that *given* that it does, the buyer has a limited ability to notice.

For the case of no termites present, the buyer makes a false positive 10% of the time.

Given these weak changes of discovering the truth, a buyer should really consult a professional.  [ Get your name here by contacting advertising@dataskeptic.com if you're such a professional :) ]

Presumably, the trained inspector has a better observation function like the one below.

|              | Found Evidence | Found No Evidence |
| ------------ |:--------------:|:-----------------:|
| Has Termites | 98%            | 2% |
| No Termites  | 5%            | 95% |

Thus, the buyer should very much like to consult with the inspector on this matter.  Yet, contracting the inspector does not give access to ground truth.  It simply generates a report which we shall call an Observation.  In POMDPs, $\Omega$ is the set of all possible observations.  In our termite example, that would be $PassedInspection$ and $FailedInspection$.  POMDPs also include $O$, the observation function.  The observation function takes as input, a particular state, action, and observation, and returns the probability of this combination.  Put simply, if you happen to be in state $s$ and you do action $a$, what are the odds you will observe $o$.  If your house happens to be infested with termites, and you hire an inspector, what is the probability they will find the infestation?  By the table above, 98%.  Defining the observation function more formally, you get $O : S, A, \Omega, \rightarrow [0,1]$.

The observation function captures imperfections in the sensors available to an agent.  Those sensors can be something as simple as the card you've got in your hand or as complex as all our visual and auditory senses.

In order to do anything useful with a POMDP, you have to *know* this function.  In other words, for a home buyer to use a POMDP to do optimal decision making, they would need to know the reliability of the inspector as shown in the table above.  Although this is a criticism highlighting the limits of the formalism's robustness, this limitation still permits a vast set of interesting problems where POMDPs are applicable.  Further, the methodology could perhaps be extended to learn this function.

So we now add $O$ and $\Omega$ to the tuple giving us the formal definition of a POMDP:

$\big \langle S, A, T, R, \Omega, O, \delta \big \rangle$

I snuck in an extra variable called $\delta$.  This is the discount factor.  It should also be there in the MDP definition, but our previous episode and blog entry left it out for simplicity.  This is a value in the range $[0, 1]$ which specifies how to value further expected rewards.  In other words, a dollar today is better than a dollar tomorrow.  But is it better than a two dollars tomorrow?  Probably not.  What's the minimum tomorrow value to be worth waiting for?  Depends on your discount factor $\delta$.

We need to generalize our definition of the transition function $T$ from the original MDP definition.  In that definition, we had a probability distribution over the next state based on the current state.  The observation that we will get in the partially observable world is going to inform this function.  The POMDP definition is $T: S_t, A_t, O_t, S_{t+1} \rightarrow [0, 1]$.  In the vernacular: given a particular state, action taken in that state, and observation made while taking that action (all this at time $t$), what's the probability of going into a particular next state (at $t+1$)?

This tuple is the definition of the POMDP.  It's nice in that it provides a formal, well defined framework which can be used to describe a wide variety of problems in a common language.  Just about any situation you can think of can be expressed in the form of a POMDP.  Although it's not done much, nothing is stopping us from using this idea to analyze the differences and properties of stochastic games in a manner analogous to the way a computational theorist studies the properties of classes of algorithms.  Yet, POMDPs are not widely thought of as abstract tools in this way.  There mostly thought of as *tools* for solving problems.

The algorithms for solving POMDPs are known.  Implementations like [pomdp-solve](http://www.pomdp.org/code/index.html) exist.  If you can specify your problem in the form of a POMDP and provide it as input to that program, it will return you an *optimal* solution to your problem!  No programming required.  Just provide some JSON file like this:

```
{
	"S": {"TERMITES", "NO_TERMITES"},
	"A": {"BUY", "NO_BUY"},
	"T": [...],
	"R": [...],
	"Omega": {"PASS_INSPECTION", "FAIL_INSPECTION"},
	"O": [...],
	"delta": 0.752
}
```

... and that's all there is to it.  Just state your problem, submit it to `pomdp-solve` and wait.  And wait.  And wait and wait and wait and wait and wait.  Because solving this problem suffers from the [curse of dimensionality](https://dataskeptic.com/blog/episodes/2015/the-curse-of-dimensionality).

If we ignore intractability for the moment, we can be certain of finding the optimal behavior to adopt under any circumstance.  When you "solve" a POMDP, the result is a policy.  The policy is a finite state machine.  Think about that for a moment, because it's rather remarkable.  A finite state machine has no memory.  It's a rather "dumb" thing.  Following the instructions of a finite state machine is a rather mindless behavior.  Yet it's optimal.  Using it is computationally efficient.  There would be no surprises running it in some production system.  Memory needs and computational needs would be trivial to estimate.  If some useful system was managed by a POMDP, that system could be very easily maintained and verified.  This would be ideal for critical systems which simply *cannot* fail.

So the policy that one gets by solving a POMDP comes in a very nice form.  How do we arrive at it?  I won't cover this fully here.  If you're eager to go down this exciting rabbithole, the core answer is using the [Bellman equation](https://en.wikipedia.org/wiki/Bellman_equation).  The best place to go next is [The POMDP Page](http://www.pomdp.org/).  Everybody, get over there.  That site should be Alexa Top 50.  A wealth of good information on POMDPs available for you.





### LT Script
Reminder of MDP, cut most from the show
Partial Observability
lady tiger - prize and penalty
how would you play?
85%, -100 -1 10, 
optimal is two counter
change reward, change behavior
solution is policy fsa ~ ai
curse of dimensionality
approximations of belief state, qomdps, deep pomdps.



