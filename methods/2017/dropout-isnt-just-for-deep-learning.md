## Dropout Isn't Just for Deep Learning

We recently did a mini-episode on the regularization technique known as [dropout](http://dataskeptic.com/blog/episodes/2017/dropout).  Dropout is pretty widely known for it's application to deep learning.

Perhaps less well known are applications of this method in other areas such as regression trees.  Authors [Rashmi](https://people.eecs.berkeley.edu/~rashmikv/) and [Gilad-Bachrach](https://www.microsoft.com/en-us/research/people/rang/) wrote an interesting paper in the Journal of Machine Learning Research titled [DART: Dropouts meet Multiple Additive Regression Trees](http://www.jmlr.org/proceedings/papers/v38/korlakaivinayak15.pdf) which explores how the same idea can help prevent over-specialization in regression tree problems.

Techniques such as boosting have become extremely popular in decision tree learning for the accuracy and speed.  Most reader will be familiar with the much lauded XGBoost algorithm which employs many clever optimizations including boosting.

The author's objective and strategy for avoiding over-specialization is wel lcaptured in their statement that "unlike random forest, DART continues to learn trees to compensate for the deficiencies of teh existing trees in the ensemble.  It, hoewver, does so in a controlled manner to strike a balance between diversity and over-specialization."

Boosting techniques (like [Adaboost](http://dataskeptic.com/blog/episodes/2016/adaboost)) are often helpful, but not without the potential for error.  As one tunes algorithms for increased accuracy, the rate of memorizing features only present in the training data becomes increasingly likely.  As Rashmi and Gilad-Bachrach eloquently state, "this, in turn, can negatively impact the performance of the algorithm onunseen data by increasing the capacity of the model without making significant improvement to its training error."

DART is an extention of MART (Multiple Additive Regression Trees).  Mart essentially employs gradient descent.  After an initial batch of trees are trained, a loss function is computed.  Subsequent iterations involve trying to develop trees that can learn to recognize and minimize this loss.  The authors efficiently describe this saying, "The first tree learns the bias of the problem while the rest of the trees in the ensemble learn the deviation of the bias"

DART introduces dropout at this stage.  Instead of taking all trees in this ensembling process, trees are randomly discarded.  Just like when dropout is applied in neural networks, the amount of regularization can be controlled by how many trees are dropped.  In this fashion, the odds that a particular tree will be dropped are non trivial, and therefore, later models in the ensemble cannot rely too strongly on the results of any given tree.

The performance results observed are quite promising and I'm sure there are many domains for which DART will be a useful technique.  You can see those results in their paper which is found [here](http://www.jmlr.org/proceedings/papers/v38/korlakaivinayak15.pdf).