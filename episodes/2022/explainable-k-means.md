## Explainable k-means

As machine learning models grow in complexity, many have criticised the resulting models for being "black boxes".  In response, the sub-field of explainable machine learning or explainable AI was created.

For a problem like k-means clustering, which is solved in an unsupervised way, the result is a mapping from data points to one of k clusters.  Yet natively, the algorithms that solve this problem don't provide complete guidelines for how the model arrived at the particular clustering result.

The result of the clustering algorithm provide boundary lines (or planes or hyperplanes) that describe how to partition your data.  This allows you to deterministically cluster new data points, but it offers no intuitive as to why the particular boundaries chosen are appropriate.

In this episode, Kyle interviews Lucas Murtinho about the paper [Shallow decision treees for explainable k-means clustering](https://arxiv.org/abs/2112.14718) about the use of decision trees to help explain the clustering partitions.
