## Parallel Algorithms

When computers became commodity hardware and storage became incredibly cheap, we entered the era of so-call "big" data.  Most definitions of big data will include something about not being able to process all the data on a single machine.  Distributed computing is required for such large datasets.

Getting an algorithm to run on data spread out over a variety of different machines introduced new challenges for designing large scale systems.  First there are concerns about the best strategy for spreading that data over many machines in an orderly fashion.  Resolving ambiguity or disagreements across sources is sometimes required.

The adage "take your computation to where your data lives" best encapsulates the most major change to coding in the era of big data.  Traditionally, one might query a database, read the results to their local machine, and then run some algorithm on that data.  Instead, the [Map-Reduce](https://dataskeptic.com/blog/episodes/2015/mapreduce) framework was born.  Later technologies like Spark sit on top more fundamental systems and provide users a highly optimized, straightforward way to derive insights.

While a lot has been written and shared about scaling up computer infrastructure to handle more in parallel, not as much attention has been paid to the computational complexity perspective on parallel algorithms.

Are there certain problems which can be solved in polynomial time by a cluster of parallel computers that cannot be solved in polynomial time by a single-threaded system?  Currently, we do not know.  At a high level this is similar to the open conjecture [P vs NP](https://dataskeptic.com/blog/episodes/2017/p-vs-np).  We call this question NC vs P or P=NC?

NC stands for Nick's class, named after one of the most influential researchers in this area, [Nick Pippenger](https://en.wikipedia.org/wiki/Nick_Pippenger).  If you read the formal definition of NC, it is the set of problems that are efficiently solvable by circuits with polylogarithmic depth and polynomial size.  I'll break down each piece of that independently.

"Efficiently solvable" should be an idea you already understand if you've been listening to recent episodes of Data Skeptic.  It means that the runtime depends on the length of the input.  As the input size given to the program increases, the runtim will also increase, but the rate at which it increases will be no worse than some polynomial number of steps in the size of the input, perhaps $n^2$ for some input of size $n$.

But what does efficiently solvable mean for a circuit?  Circuits are a little different, at least in their formalism, than algorithms.  Circuits have some fixed number of inputs, not a variable length like a Turing Machine.  In the context of circuits, we assume that there exists some circuit that is specially designed for each particular input length you might try.  It's call a circuit family.  If you had one, to use it, you'd first measure the size of your input, find the corresponding circuit that's useful for that length, and then feed your input into the circuit, and observe the output.  In this way, we consider the number of gates in a circuit as well as the depth of these gates.

The next characteristic of class $NC$ is that the circuits only have polylogarithmic depth.  The depth of a circuit is the number of "layers" the gates are stacked from input to output.  Its roughly analogous to the number of hidden layers in a neural network.  Your circuit may have gates that depend on outputs of other gates.  During computation, they have to "wait" for the earlier gates to propagate their signal forward to the output.  As circuits become deeper they may become more complex.  The slight slowdown for signal propagation is typically modeled as negligible.

So algorithms in this class have to be at most polylogarithmic in depth.  That's very shallow!  As the size of the input grows, you can only increase the depth of the larger circuits in a sub-linear fashion.

Lastly, the circuits must be polynomial in size, where the size is measured by the number of gates in the circuit.

Complexity classes like $NC$, and circuits more generally, are very useful tools for attempting to establish lower bounds.  This is an active area of research which seems to have a lot of open problems which a PhD student might be able to solve.

One open problem is $P \stackrel{?}{=} NC$.  In other words, are there any algorithms that can be solved using parallel computing which *cannot* be solved in polynomial time on a single threaded system.  Granted, parallel algorithms offer major speed ups.  A single threaded algorithm will take longer, but might it always be polynomial $n^k$ with some really large $k$?  This problem is unsolved.

Resolving whether or not $P=NC$ would likely provide extremely useful insights about how we should approach engineering massive scale computing infrastructure and high performance computing.
