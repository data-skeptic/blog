## Louvain Method for Community Detection

Without getting into definitions, we have an intuitive sense of what a "community" is.  The Louvain Method for Community Detection is one of the best known mathematical techniques designed to detect communities.

This method requires typical graph data in which people are nodes and edges are their connections.  It's easy to imagine this data in the context of Facebook or LinkedIn but the technique applies just as well to any other dataset like cellular phone calling records or pen-pals.

The Louvain Method provides a means of measuring the strength of any proposed community based on a concept known as **Modularity**.  Modularity is a value in the range $[-1, 1]$ that measure the density of links internal to a community against links external to the community.  The quite palatable assumption here is that a genuine community would have members that are strongly interconnected.

A community is not necessarily the same thing as a clique; it is not required that all community members know each other.  Rather, we simply define a community as a graph structure where the nodes are more connected to each other than connected to people outside the community.

It's only natural that any person in a community has many connections to people outside that community.  The more a community has internal connections over external connections, the stronger that community is considered to be.  The Louvain Method elegantly captures this intuitively desirable quality.

Louvain Modularity $Q$ is given by this formula:

$Q={\frac {1}{2m}}\sum \limits_{ij}{\bigg [}A_{ij}-{\frac {k_i k_j}{2m}}{\bigg ]}\delta (c_{i},c_{j})$

Let's deconstruct this in reverse order, beginning with the $\delta$ function.  This is a typical delta function - a function that returns 0 or 1, much like a classifier.  It's two parameters $c_i$ and $c_j$ represent the communities of $i$ and $j$ respectively.  If $i$ and $j$ are in the same community, then $\delta$ returns a value of 1, otherwise 0.  Think of the delta function like a sort of "switch".  When it's "on", we'll count the connection, otherwise not.

Moving backwards in the Modularity equation, our next term is a sum over all possible links $i$ and $j$.  For each pair of people, $A_{ij}$ represents the edge weight between $i$ and $j$.  This is the strength of the connection shared by the two people.  The value $A$ is an adjacency matrix.  In some cases all one has is binary data, but a stronger result is generally produced when these edges are weighted in some way.  A naive approach applied to Facebook data might consider only if two users are friends.  A more sophisticated approach might weight those friendships based on interactions of some kind.

The values of $k_i$ is defined as $\sum \limits_{j}{A_{ij}}$, or the sum of all of $i$'s weights.  In this was $k_i$ and $k_j$ help to normalize for users that hold large number of connections.  The volume of connections is prevented from biasing the results because each additional connection is weighted weaker and weaker.

Lastly, $2m = \sum \limits_{ij}{A_{ij}}$ or the sum of all the weights in the graph (times 2 since it's symetrical).  This is a normalizing factor to ensure that all results, regardless of $A$ end up in the desired range $[-1, 1]$.

Modularity is a metric describing the strength of the communities $c$ that have been provided.  Naturally, our next step would be to optimize the selection of $c$, rather than some guess and check approach.  That algorithmic process is a great topic for a future show.





For any two notes $i$ and $j$ (where $i \neq j$), we iterate 