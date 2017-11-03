## The Computational Complexity of Machine Learning

In this episode, Professor Michael Kearns from the University of Pennsylvania joins host Kyle Polich to talk about the computational complexity of machine learning, complexity in game theory, and algorithmic fairness. Michael's doctoral thesis gave an early broad overview of computational learning theory, in which he emphasizes the mathematical study of efficient learning algorithms by machines or computational systems. 

When we look at machine learning algorithms they are almost like meta-algorithms in some sense. For example, given a machine learning algorithm, it will look at some data and build some model, and it’s going to behave presumably very differently under different inputs. But does that mean we need new analytical tools? Or is a machine learning algorithm just the same thing as any deterministic algorithm, but just a little bit more tricky to figure out anything complexity-wise? In other words, is there some overlap between the good old-fashioned analysis of algorithms with the analysis of machine learning algorithms from a complexity viewpoint? And what is the difference between strategies for determining the complexity bounds on samples versus algorithms?

A big area of machine learning (and in the analysis of learning algorithms in general) Michael and Kyle discuss is the topic known as complexity regularization. Complexity regularization asks: How should one measure the goodness of fit and the complexity of a given model? And how should one balance those two, and how can one execute that in a scaleable, efficient way algorithmically? From this, Michael and Kyle discuss the broader picture of why one should care whether a learning algorithm is efficiently learnable if it's learnable in polynomial time.

Another interesting topic of discussion is the difference between sample complexity and computational complexity. An active area of research is how one should regularize their models so that they're balancing the complexity with the goodness of fit to fit their large training sample size. 

As mentioned, a good resource for getting started with correlated equilibria is: [https://www.cs.cornell.edu/courses/cs684/2004sp/feb20.pdf](https://www.cs.cornell.edu/courses/cs684/2004sp/feb20.pdf)




<div class="row">
        <div class="col-xs-12 col-sm-3">
                <img alt="Michael Kearns" src="src-the-computational-complexity-of-machine-learning/michael-kearns.png" />
                <br/>
                <p><i>Michael Kearns</i></p>
        </div>
        <div class="col-xs-12 col-sm-9">
		Michael Kearns is a Professor and the National Center Chair at the Computer and Information Science Department at the University of Pennsylvania. He holds a secondary appointment in the Department of Economics with joint appointments in the Wharton School's Department of Statistics and Department of Operations, Information, and Decisions. Michael is also the founding director of the Warren Center for Network and Data Sciences and the founding co-director of Penn Engineering's Networked and Social Systems Engineering Program. In addition, he is chief scientist of MANA Partners, a trading, technology, and asset management firm. Michael holds a Ph.D. in computer science from Harvard University. His research interests include topics in machine learning, algorithmic game theory and microeconomics, computational social science, and quantitative finance and algorithmic trading.
        </div>
</div>
