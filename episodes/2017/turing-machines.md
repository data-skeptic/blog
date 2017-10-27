## Turing Machines

TMs are an model of computation at the heart of algorithmic analysis.  A Turing Machine has two components.  An infinitely long piece of tape (memory) with re-writable squares and a read/write head which is programed to change it's state as it processes the input.  This exceptionally simple mechanical computer can compute anything that is intuitively computable, thus says the Church-Turing Thesis.

Attempts to make a "better" Turing Machine by adding things like additional tapes can make the programs easier to describe, but it can't make the "better" machine more capable.  It won't be able to solve any problems the basic Turing Machine can, even if it perhaps solves them faster.

An important concept we didn't get to in this episode is that of a Universal Turing Machine.  Without the prefix, a TM is a particular algorithm.  A Universal TM is a machine that takes, as input, a description of a TM and an input to that machine, and subsequently simulates the inputted machine running on the given input.

Turing Machines are a central idea in computer science.  They are central to algorithmic analysis and the theory of computation.
