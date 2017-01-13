## Dropout

Deep learning can be prone to overfit a given problem.  This is especially frustrating given how much time and computational resources are often required to converge.  One technique for fighting overfitting is to use dropout.  Dropout is the method of randomly selecting some neurons in one's network to set to zero during iterations of learning.  The core idea is that each particular input in a given layer is not always available and therefore not a signal that can be relied on too heavily.

As far as I know, dropout was introduced in the paper [Dropout: A Simple Way to Prevent Neural Networks from Overfitting](https://www.cs.toronto.edu/~hinton/absps/JMLRdropout.pdf)
