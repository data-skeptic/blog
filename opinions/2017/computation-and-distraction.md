## Computation and Distraction

As a computer scientist, I try to size up most problems in terms of their computational complexity.  For those unfamiliar with the topic, this basically means trying to determine how much effort would be required to compute a solution given the size of the input step.

A classically efficient problem is finding if a particular word is in the dictionary or not.  You can first go to the middle of the dictionary and ask if your word should be before or after the center word.  This single test cuts the problem size in half.  Repeating that process of halving the possible location of the word in each iteration is called binary search.  It takes advantage of the fact that the dictionary is known to be ordered and thus, takes a very small number of steps to answer the question.  In technical terms, we call this a $O(\text{log} N)$ problem.

I'm also a fan of econometrics, yet find a flaw in one of it's common critical assumptions.  Econometrics typically studies situation in which independent people interacting with each other are perfectly rational and have common knowledge of perfect rationality.  Both these assumptions are problematic.  The second one is a bit more complex to discuss, so I'll leave that for a future blog post.

Assuming an agent is perfectly rational means that if an optimal solution exists, we assume they are sure to find it.  When interacting with other agents, the optimal interaction is an equilbria, in which none of the agents have any motivation to take actions outside of that equilibria.  From the onset, this can be a dubious conclusion.  Psychologists have demonstrated many situations in which people behave in irrational ways.

While very simple games often do have known equilibria, for complex games involving stochastic processes, it is typically the case that our current understanding of game theory and each individual problem has not yielded any known equilibria solution.  In many cases, the equilibria that are known are understood by only very adept econometricians.  How could we expect the average person to discover and act on them?

One argument is that optimization in a situation like this runs on a broader time scale and works a bit more like evolution.  If two businesses are competitors, they will either start competing in an equilibria state, or one of those businesses will eventually dominate the other.  The winner of such a competition (or both companies in the event an equilibria is reached) should not necessarily be labeled as smart, rational, or strategic.  It could very well be that the company adopted a strategy at random and it just so happened that their strategy was dominant over their competitors.  We cannot automatically conclude that the leadership team is wise and perfectly rational.  The may have achieved that equilibria without fully understanding it's advantages.

When it comes to certain contests involving humans, I believe we're at the start of an era when we have to consider modeling agents as boundedly rational beings.  It's true that computer hardware has a significantly smaller density of integrated circuits than the density of neurons in the human brain.  At least for now that's true.  However, eepending on the nature of the problem of interest, the massively parallel nature of the human brain will not necessarily offer an advantage.

For tasks that are intensely computation, an algorithm is very likely to outperform human achievements.  We've been seen an increasing number of examples like this since approximately the 1980s.

I was struck by a comment made by Peter Backus on last week's episode of Data Skeptic, and I wanted to follow up with a few thoughts of my own regarding the computational demands of chess.

Peter said that chess would eventually be a solved problem for a computer.  While I do fully agree with this statement, I think the ultimate provably optimal strategy might not be a direct application of backwards induction as he describes.  To be sure, backwards induction is a powerful technique used in modern approaches to chess algorithms.  Those algorithms consistently outperform the best human players.  Yet, we still don't call chess a "solved" problem yet, because the algorithms cannot confidently be shown to always win or draw.

Interestingly, in the case of Checkers/Draughts, the Chinook program has been proven to always win or draw - you can never beat it under any circumstance.

Peter made a very interesting point when putting forward the hypothesis of stereotype threat theory to explain the performance gap measured when female players face male opponents (listen to the episode for details about his work).

We can think of a chess playing human as a machine with a finite number of computational resources available to search the game space.  They likely have a cache of pre-computed solutions from their training and prior experience that allows them to recognize certain board configurations as advantageous or disadvantageous.  Their memory lets them prune the search space efficiently.  I have every reason to believe that human beings have, move or less, the same basic hardware.  In electronic computer equivalent, this is like saying our CPUs are all the same and we have the same amount of RAM and disc space.

When players of equal skill (as measured by their Elo ratings) compete, we can assume that their cache of known good and bad configurations is is probably about the same.  If so, the prune their search spaces equally well, and the game comes down either cases where one player is more familiar with games in similar configurations as they arrive at, or cases where one player has a bit more luck in selecting seemingly equivalent moves.

If one of the players is distracted by external details, then the very fact that they are spending time considering those details has a computational cost.  If stereotype threat affects a player, then ever moment they spend pondering the expectation they feel is a moment *not* spent thinking about the game.

As Peter says in the episode, "that distraction eats up some 'RAM'".  I'm not sure if RAM or CPU is the better analogy, but from a computational point of view, this argument is compelling to me.  Their work puts a number of good controls in place to mitigate for confounding factors.  One might even claim that they've eliminated all claims and thus reduced their experiment down to purely a measurement of the effect of stereotype threat.

Whether that's indeed the case or not, this is an interesting study.  I'd love to learn about more research which tries to capture the impact on performance of an agent that is experiencing some sort of computational distraction.
