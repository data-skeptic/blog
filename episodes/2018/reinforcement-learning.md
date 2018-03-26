## Reinforcement Learning

In many real world situations, a person/agent doesn't necessarily know their own objectives or the mechanics of the world they're interacting with.  However, if the agent receives rewards which are correlated with the both their actions and the state of the world, then reinforcement learning can be used to discover behaviors that maximize the reward earned.

**Thanks to [brilliant.org](https://brilliant.org/dataskeptic) for sponsoring this episode.**

This mapping from an agent's history (all the observations and experiences they've ad so far) to a choice of actions is known as a policy, often represented in the literature with the symbol $\pi$ for some reason.

In a reinforcement learning scenario, an agent's goal is to maximize the amount of reward they are able to collect.  Doing so almost always requires learning about the world and and balancing the exploration of what to try with the exploitation of what the agent has learned so far.

In this episode we briefly touch on feature based reinforcement learning and deep learning - two techniques that are helping fight the [curse of dimensionality](https://dataskeptic.com/blog/episodes/2015/the-curse-of-dimensionality).
