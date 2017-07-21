## Conditional Independence

In statistics, two random variables might depend on one another (for example, interest rates and new home purchases).  We call this conditional dependence.  An important related concept exists called conditional independence.  This phrase describes situations in which two variables are independent of one another given some other variable.

For example, the probability that a vendor will pay their bill on time could depend on many factors such as the company's market cap.  Thus, a statistical analysis would reveal many relationships between observable details about the company and their propensity for paying on time.  However, if you know that the company has filed for bankruptcy, then we might assume their chances of paying on time have dropped to near 0, and the result is now independent of all other factors in light of this new information.

We discuss a few real world analogies to this idea in the context of some chance meetings on our recent trip to New York City.

Formally, we would say that random variable $X$ is independent of $Y$ if:

$Pr(X \cap Y) = Pr(X)Pr(Y)$

When this does not hold, we represent the statistical relationship as:

$Pr(X|Y)$

If $X$ and $Y$ are conditionally independent given $Z$, we write that as:

$Pr(X \cap Y | Z) = Pr(X|Z) Pr(Y|Z)$
