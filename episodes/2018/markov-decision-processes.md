## Markov Decision Processes

Formally, an MDP is given as the tuple $\big \langle S, A, T, R \big \rangle$.  The rest of this post will define each of these componenets.

The variable $S$ is the set of all possible states.  In the simple game of tic-tac-toe, each of the 9 squares can have one of three values: blank, $X$, or $O$.  There can be no more than $3^9$ possible states, however, that includes many states which are not valid tic-tac-toe games in play.  For example, a board filled with all $X$ values could never be arrived at.  You should take $S$ to be the complete set of all possible states of any given game or environment.

The variable $A$ is the set of all actions available to an agent.  This can be described in many different ways.  For example, the path of a video game character in a grid-based board game could have actions of GoUp, GoLeft, GoRight, GoDown.  Equivalently, the character could have the actions Rotate90Degrees and MoveForward to produce (relatively speaking) the same result.  Agents are given a no-action or "no-op" action in many settings.

Due to the extreme computational demands of solving an MDP, one often wants to take great care in defining sets $S$ and $A$ to be complete yet minimalist.

The variable $T$ is the transition function which specifies how the state evolves.  It takes as input, the current state, the action taken, and a next state.  It will return the probability that the proposed next state turns out to be the actual next state.  Consider a simple board game in which player $i$, currently in space $s_0$ commits to taking an action to move forward.  In this board game, to move forward, the player rolls a four sided die and advances their position forward that many spaces.  In this case, $T(s_i, GoForward, s_j)$ = 0.25 $\forall j$ s.t. $i < j < i + 4$. and $T$ returns 0.0 otherwise.  It can be formally written as $T : s_t \in S, a \in A, s_{t+1} \in S \rightarrow [0, 1]$.

Notice that $T$ depends on $s_t$ but does *not* depend on $s_{t-1}$.  Why should the transition function depend only on the current state and not on slightly older states?  While that is mathematically possible, it's unnecessary when the state is defined appropriately.  In constructing an MDP we must insist that the state be a "sufficient statistic".  That is to say, knowing the current state is enough.

In tic-tac-toe, several game paths could all lead to the same future state.  As a curiosity, you might be interested to know which one you took to arrive at the current state of the game, but it has no impact on the outcome of the game nor how to find an optimal strategy.  

Requiring that the current state be descriptive enough to not require information from the past may, on the surface, appear incompatible with certain games.  In baseball, for example, a player remains at bat until a rule specifies that their turn at bat is over, such as when the accumulate three strikes.  This is why we consider the scoreboard to be part of the state.  A tabulation of the number of strikes and balls is always present and available for use in calculating the function $T$.

The variable $R$ is the reward function.  It takes as input, the current state and the action taken, then returns a number representing the reward earned by the agent in that situation.  Formally, $R : s_t \in S, a \in A \rightarrow \mathbb{R}$.

Notice that, unlike $T$, $R$ does not depend on the next state.  Does this mean that agents think only in the present and do not consider rewards earned in the future?  Absolutely not.  An agent should certainly consider the value of taking their next action given the current state.  Doing *just* this is called a "horizon zero" agent.  Let's discuss that further after we define what it means to solve an MDP.

An MDP is a description of a system.  While my examples have been simple games, one could create MDPs that define Chess, Go, stock trading, driving, and countless other scenarios.

Generally, once you've defined an MDP, you want to solve it.  Specifically, you'd like to find the optimal strategy that an agent should adopt to reap the most rewards when playing the game.  This optimal strategy is also called the optimal policy.  A policy is any decision making process which maps from all possible histories of observations to a choice about what action to take next.  In this way, an MDP maps directly to the [agent model](https://dataskeptic.com/blog/episodes/2018/the-agent-model-of-intelligence).

Finding the optimal solution to an MDP can be computationally expensive on any non-trivial game.  This framework is deeply impacted by the [curse of dimensionality](https://dataskeptic.com/blog/episodes/2015/the-curse-of-dimensionality).  There are two general approaches to finding the optimal policy: finite horizon and infinite horizon with discounting.

For finite horizon search, one calculates only $h$ steps ahead to determine the optimal action to take.  This is a technique that is commonly used in chess-playing algorithms: consider every possible path the game could take looking forward for $h$ moves.  Out of all those paths, select the one that is most beneficial to you, and execute the first action down that path.  When next the player needs to act, they can repeat the same process, with one more observation and a sliding lookahead window of size $h$.

For infinite horizon search, one seeks a strategy that assumes the game continues to be played forever.  Commonly, playing forever is likely to yield infinite the possibility of infinite rewards.  Thus, one either tries to maximize for average reward or reward with discounting.  Reward with discounting involves ascribing less value to rewards earned further in the future.  For infinite horizon search, implementations typically stop searching when they can be sure that their current best policy is at least $\epsilon$ close to the actual optimal policy.

