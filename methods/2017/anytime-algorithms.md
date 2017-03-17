Anytime Algorithms

On the last episode of Data Skeptic, Ruggiero Cavallo discussed an algorithm he and his co-authors devised for optimizing ad auction placement.  One interesting feature of their algorithm was that it calls into the category known as anytime algorithms.

All algorithms are functions that map from some given input to a an output.  For example, an algorithm exists which can be given an input of arithmetic instructions such as: $(7-2) * 5 + 1$, and return an output of $26$.  Obviously, there are several steps involved in arriving at that answer (subtract, multiply, add).  If you interrupted this algorithm early and asked for a bet guest of the answer, it could not have a useful guess.

In contrast, an anytime algorithm is one which can be halted early and is always able to provide some output.  If you interrupt the algorithm before it has a chance to halt "naturally", you may end up with an output that is a sub-optimal answer to the problem being worked on, but a decent output, and one which should monotonically increase with time.

A simple search algorithm like using depth first search to find the smallest element in a tree could be trivially converted into an anytime algorithm.  At the time of halting, the DFS algorithm would simply report the smallest element observed so far.  If it were allowed to continue the search, it might possible find a smaller element, or maybe not.  The more complete a search allowed, the more likely the answer is exactly or close to the true minimum.

Anytime algorithms are especially useful in resource constrained settings.

Game playing is one example of being resource constrained.  A well built chess playing engine probably has components that are anytime algorithms.  At a high level, much of what a chess algorithm does is some sort of search.  That search should always be tracking the best next move found so far.  It might be the case that a sub-system independent of the search is evaluating the likelihood of identifying a better move and deciding whether or not the halt the search to save time on the clock for later rounds.

In the case described by Ruggiero's team, the constraints are similar.  Users visiting websites do not with to wait in order to have the content of the page loaded.  Even if the ads are loading separately from the main content, the ad network wants to minimize the time to display the ads to the user.  While the promise of earning more revenue is tempting, it must be balanced with loading the page in an effective amount of time.

Autonomous systems rely heavily on anytime algorithms.  If a self driving car is headed into an unexpected, dangerous situation, acting quickly may need to take precidence over precise prediction of what exactly will happen next.  If the car is 95% sure slamming the brakes is an appropriate action, halting a deeper search to raise the accuracy to 99% certainty might not be the best use of the CPU cycles available.

Whenever the consequence of delayed reaction is relevant, its critical for systems to be based on anytime algorithms.  Without this interruptable feature, a machine might spend all of it's time advancing a progress bar, only to discover a missed opportunity or worse.