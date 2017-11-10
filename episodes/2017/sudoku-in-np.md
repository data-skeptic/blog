## Sudoku in NP

or the title as I prefer it to render...

Sudoku $\in NP$

Algorithms with similar runtimes are said to be in the same complexity class. That runtime is measured in the how many steps an algorithm takes relative to the input size.

The class P contains all algorithms which run in polynomial time (basically, a nested for loop iterating over the input).  NP are algorithms which seem to require brute force.  Brute force search cannot be done in polynomial time, so it seems that problems in NP are more difficult than problems in P.  I say it "seems" this way because, while most people believe it to be true, it has not been proven.  This is the famous P vs. NP conjecture.  It will be discussed in more detail in a future episode.

Given a solution to a particular problem, if it can be verified/checked in polynomial time, that problem might be in NP.  If someone hands you a completed Sudoku puzzle, it's not difficult to see if they made any mistakes.  The effort of developing the solution to the Sudoku game seems to be intrinsically more difficult.  In fact, as far as anyone knows, in the general case of all possible examples of the game, it seems no strategy can do better on average than just random guessing.

This notion of random guessing the solution is where the N in NP comes from: Non-deterministic.  Imagine a machine with a random input already written in its memory.  Given enough such machines, one of them will have the right answer.  If they all ran in parallel, one of them could verify it's input in polynomial time.  This guess / provided input is often called a witness string.

NP is an important concept for many reasons.  To me, the most reason to know about NP is a practical one.  Depending on your goals or the goals of your employer, there are many challenging problems you may attempt to solve.  If a problem you are trying to solve happens to be in NP, then you should consider the implications very carefully.  Perhaps you'll be lucky and discover that your particular instance of the problem is easy.  Sudoku is pretty easy if only 2 remaining squares need to be filled in.  The traveling salesman problem is easy to solve if you live in a country where all roads for a ring with exactly one road in and out.

If the problem you wish to solve is not trivial, or if you will face many instances of the problem and expect some will not be trivial, then it's unlikely you'll be able to find the exact solution.  Sure, maybe you can grab a bunch of commodity servers and try to scale the heck out of your attempt.  Depending on the problem you're solving, that might just work.  If you can out-purchase your problem in computing power, then problems in NP will surrender to you.  But if your input size ever grows, it's unlikely you'll be able to keep up.

If your problem is intractable in this way, all is not lost.  You might be able to find an approximate solution to your problem.  Good enough is better than no solution at all, right?  Most of the time, probably.  However, some tremendous work has also been done studying topics like this.  Are there problems which are not even approximable in polynomial time?  What approximation techniques work best?  Alas, those answers lie elsewhere.

This episode avoids a discussion of a few key points in order to keep the material accessible.  If you find this interesting, you should next familiarize yourself with the notions of NP-Complete, NP-Hard, and co-NP.  These are topics we won't necessarily get to in future episodes.  Michael Sipser's [Introduction to the Theory of Computation](https://www.amazon.com/Introduction-Theory-Computation-Michael-Sipser/dp/113318779X) is a good resource.


