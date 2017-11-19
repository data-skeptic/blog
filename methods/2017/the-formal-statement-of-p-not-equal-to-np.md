## The Formal Statement of P not equal to NP

In the last episode of Data Skeptic, I asked Lance Fortnow about whether or not is was possible P vs NP was ill-posed.  He correctly pointed out that, while some surprising result come emerge (like showing its impossible to solve it), it can't be ill-posed, because the problem has a formal mathematical statement.  That statement is below.

$\exists L \in NP \hspace{5pt}$ such that $\forall M \in T, p \in P \hspace{5pt} \exists x \hspace{5pt}$ such that $M(x) \ne L(x) \hspace{5pt}$ or $M(x)$ runs for > $p(|x|)$ steps.

This blog post is a deconstruction of this definition and a some color commentary about it.

$NP$, of course, refers to the class Non-deterministic polynomial time algorithms.  In order to show that an algorithm is in $NP$, you only need to present the description of that algorithm (pseudocode is probably fine) which can verify a solution to a problem in polynomial time.  Finding that solution on the other time, seems to require brute force search.

Of course, you can prove an algorithm is in $NP$ doesn't it can't be solved efficiently by any known means.  Maybe *your* algorithm has many unexpected steps or fails to take advantage of some structure of the problem.  A more clever person might be able to present an equivalent algorithm that runs in polynomial time (class $P$).

This is where the idea of $NP$-Completeness comes into the picture.  In part because simple showing a problem is in $NP$ isn't enough, complexity theorists wanted a way to stack hard problems against each other.  Wouldn't it be interesting to be able to say "my problem seems like its equally as hard as another known problem".  Take that further.  What if you could demonstrate an equivalence between two problems, such that if you had a solution for one, you could use it as a tool for solving another?

As mentioned in recent episodes two examples of problems in NP are Clique (like determining if there's a group of people where every single person in the group is mutually friends with one another and the group has at least 100 members) and Sudoku (the puzzle game).  On the surface, these problems appear to have very little in common.

Imagine you have a nice efficient Python algorithm for solving Clique problems in a file called `clique_solver.py`.  It accepts graphs in a specific format, and returns the answer to questions about the largest clique.  But what if despite having this very valuable piece of code, you actually don't care much for Clique.  Your true passion in life is solving Sudoku puzzles efficiently, but alas, you haven't been able to write a nice efficient file called `sudoku_solver.py`.

No problem!

All you need to do is fine a way to convert Sudoku puzzles into the equivalent graph problem, save them in the specific format your python code uses, and then solve the  Clique problem which is equivalent to your given Sudoku puzzle.  It might not be obvious how to do that, and I think the topic is out of scope for this discussion.  However, as long as you can do such a conversion efficiently (it's called a polynomial time reduction), then we're good to go.

There is a large and growing set of problems that are called $NP$-Complete.  A problem gets this status by showing that it has such an equivalence to other known $NP$-Complete problems.  If you can solve one efficiently, you can solve them all efficiently.

All this is to say that just because a problem is shown to be in $NP$ doesn't mean its certainly hard.  Ideas like $NP$-Completeness are introduced to help us understand what the *hardest* problems might be.

Let's get back to the formal definition, starting with the first term $\exists L \in NP$.  In plain English, this means that there exists at least one language $L$ in $NP$.  What do we mean by language.  Although not always appropriate, I often interchange the use of the word algorithm, problem, and language.  For some readers calling something a language might seem out of place.  If this doesn't bother you, feel free to skip the next two paragraph.

To understand what a language is to a computer scientist, let's get back to basics and start with an alphabet.  Every language has an alphabet.  The letters in that alphabet can be combined in a variety of ways.  For example, I can use the english alphabet to write the sentence "ababab efefefef cdcdcdcdcd fg".  This is *not* a sentence considered to be in the English language.  Similarly "Laptop cannon bakery black lodge" has familiar words but is also not considered to be a member of the set of all sentences in the English language.

Formally, a language is a set of sentences (let's call them strings from now on) which are considered to be in that language.  What is interesting from a computational perspective is to decide whether or not a given string is in a language.  For example, given a Sudoku puzzle, does it meet the criteria of being a valid puzzle (rows, columns, and subgroups sum up appropriate)?  My earlier sentence "ababab efefefef cdcdcdcdcd fg" is a valid sentence in the language of all words which are composed of repeating two letter sequences of consecutive alphabet characters.  It's extremely easy to check if a given sentence is in that language and to construct new sentences!

Later on, we'll see $L$ used as a function: $L(x)$.  The language $L$ is a function which computes sentences in a language given some input $x$.  An example of such a languages is the squared language, where $L(x) = x^2$.  Another more complex language could be the question answering language where an input string $x$ of "Who hosts Data Skeptic?" may have a formal output of "Kyle Polich with co-host Linhda Tran".

So the first part of the definition simply states that there must be at least one (possibly elusive) problem in $NP$ that the rest of the definition is going to talk about.  Let's move forward in the definition and learn more about the special language that's in $NP$.

On to this [universal quantifier](https://en.wikipedia.org/wiki/Universal_quantification): $\forall M \in T, p \in P$.  $T$ is the set of all Turing machines.  In other words, its literally the set of every possible program that every could be written.  $P$ is the set of all polynomials (i.e. $x^2$, $x^3$, $x^4$, ... $x^k$ for any arbitrarily large $k$).  So this bit of the definition just says that for all combinations of possible Turing Machines and Polynomials, either...

$\exists x \hspace{5pt} \text{s.t.} \hspace{5pt} M(x) \ne L(x) \hspace{5pt}$

Which is to say that the machine $M$ doing its very best effort to compute the correct output for $L$ applied to input $x$, there exists at least one $x$ where they are going to disagree, or...

$M(x)$ runs for > $p(|x|)$ steps.

Which is to say that machine $M$ is going to run for more than a polynomial number of steps, which by definition, means $M$ is not getting it's work done in polynomial time.

So we could possibly have a machine $M$ which is "pretty good".  It could run in polynomial time, but if it does, it's going to make mistakes.

If we demand that $M$ make no mistakes, then it can't possibly complete it's work in polynomial time for all inputs.

For readers looking at this for the first time, you might find this formal definition to demand unreasonable perfection.  Can't we be satisfied with some machine $M$ that's close enough?  What about a machine that's always correct and only runs in greater than polynomial time in a few rare cases?

Indeed, sometimes you are going to be fortunate and find yourself able to compute a solution to a problem in $NP$ in polynomial time.  Huh?

If you live in a country where all cities have exactly two highways and are connected like a ring, then you'll probably find easy solutions to presumably every graph problem in $NP$.  If you work on circuits which have no NOT gates (monotone circuits), lots of circuit properties are efficient to calculate.  If you try to color a map that's a well organized grid, your work should be pretty easy.  A graph with no edges has trivial clique solutions.

The question of $P$ vs $NP$ is not about cherry picked examples, but on whether or not *all* examples of a given problem can be solved efficiently.  This is why we see the $\exists x$ part of the definition.  While in reality, any language in $NP$ probably has a large (possibly infinite) set of nasty examples, it's enough to state that one such example exists.

What if you had a machine $M$ which, given input $x$ ran for polynomial time and gave the same result as $L(x)$ most of the time?  In fact, let's say $M(x) = L(x)$ in all cases except for one very puzzling input $x'$.  Couldn't you start with $M$ and create $M'$ which as a few additional line of code to first checks if the input equals $x'$, if so output the correct response which you've hardcoded, if not, run as normal?

This idea is wrong on a number of levels.  In fact, it's kind of flawed from the beginning since we state in the definition $\forall M \in T$, which means we considered every possible Turing Machine that every could be.  For a given $M$ drawn at random, there's a high likelihood you could find some $M'$ which is a little closer to $L$.  However, the idea of "hardcoding the pre-calculated outputs of tricky inputs" can only take you so far.  You're either going to end up with a description that's infinitely long or you're going to hit some other barrier along the way.  Unless, of course, $P=NP$.

While the formal definition, for me, is not as intuitively satisfying as an English description using phrases like "witness string" and "polynomial time verification", it's important to recognize that this is the formal definition.  Understanding it can give you a greater appreciation for the problem as well as highlight the mathematical qualifications necessary to resolve this conjecture one way or the other.

