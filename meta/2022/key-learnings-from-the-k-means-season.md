# Key Learnings from the K-Means Season
At Data Skeptic, we just concluded the K-means clustering season. We were joined by accomplished Machine Learning researchers sharing insights, challenges, and future trends of their work. Without mincing words, the episode was packed with a lot of value. In this article, I will share with you some ideas that jumped out at me in the course of the season. The goal is that you are able to connect ideas across the different episodes and have a holistic understanding of what k-means is. In addition, you will have a bird-eyes view of how researchers have been engaging with the technique for various problem-solving. 

Let’s dive in. 

## #1\. Centroid initialization is an important step in K-means clustering

K-means clustering is done in three simple steps: centroid initialization, assignment, and recalculation. But across the episodes of the season, a handful of our guests spoke about the centroid initialization process. In the vanilla k-means approach, also called Lloyd’s algorithm, you define the number of clusters, k,  you wish to have, and then randomly partition the data into the k number of clusters. The initialization is completely random. From there, the algorithm finds a way of recalibrating until it gets the best cluster positions that partition that data. While this performs generally well, using Lloyd’s approach can limit the performance of your algorithm. Technically, this happens when you get stuck in a local minimum.

Researchers now use other approaches for centroid initialization. For example, the K-means ++ algorithm is a popular smart centroid initialization used today. It works by considering which random centroids have already been selected and selecting the centroid that has a large distance from the other existing centroids. Many of our guests spoke about the k-means ++ algorithm. 

But there were other algorithms used as well. Bernd Flitz, in the breathing k-means episode, spoke briefly about the LBG algorithm whose centroid initialization involves a codebook design alongside some encoding and decoding processes. Other algorithms mentioned were the random swap algorithm and genetic algorithm. 

Meanwhile, Jason, in the power k-means episode, spoke about the k-harmonic mean method. In this method, the harmonic distance from each point to the cluster center is taken into account in the performance function, making it more robust to the initialization of the clusters.   

  

## #2 K-means can be used as one side of a coin. 

In practice, k-means can be used alongside other machine learning algorithms. On the one hand, you could stack a supervised learning algorithm on top of the k-means for optimum results. On the flip side, you could use k-means as a supervised learning approach and another clustering algorithm as an unsupervised learning approach. One of our guests, Greg, applied this technique in his work. First, he used the DBSCAN algorithm to first determine the clusters of moving elephants. The result was a bunch of graphs without real meaning. Then, k-means was used as a way of classifying elephant clusters into premeditated labels. In other words, k-means was a supervised learning approach that classified the DBSCAN clusters into human settlements and water banks.

## #3 There should be a balance between computational power and the algorithm’s performance.

It is easy to get carried away with an algorithm’s performance. But throughout the season, we see guests giving special attention to their algorithm’s computational requirement. This helps to determine the practicality and scalability of the algorithm when solving real-world problems. 

In the power k-means episode, Jason contrasted the computational demand of the power k-means algorithm to Vanilla k-means. In power k-means, the algorithm was able to find the global minima in random restarts. Meanwhile, Lloyd's algorithm is NP-hard, meaning that it could involve iterating through the total number of datapoints before the global minima is found.

In breathing k-means, Bernd ensured that despite the complexity of his algorithm, the optimization is closely within the range of the k-means ++ algorithm. This stems from the fact that while k-means ++ performs repeated initialization, breathing k-means do a number of Lloyd’s algorithm iterations. So in the end, it averages out at roughly the same computational demand. 

## #4\. Model evaluation is a thoughtful process

In any machine learning problem, model evaluation is an essential step. It helps the developer measure the performance of the model and compare it to a base model. But across the several episodes, our guests put in a lot of thoughts in determining the best way to evaluate their model performance. 

For one, model evaluation can be done based on a unified dataset. In this case, you ensure that you evaluate your model on a dataset that has been used to solve the same problem with another algorithm. If your model outperforms the existing algorithm, you can conclude that your algorithm is better. Greg used this approach in his work. He measured up his model against another clustering algorithm called Optics. Sibylle, in the Matrix Factorization for k-means episode, also compared the accuracy and confidence level of her result to the conventional neural network algorithm. Also, Bernd compared the results of his breathing k-means algorithm to the popular k-means ++.

Another way of evaluating a model is by trying out different evaluation metrics. As an example, accuracy may not always be the best metric to use for a classification problem. In cancer detection problems, you would rather want to use recall. Ehsan, in the customer clustering episode, tried out different metrics such as k-medians and k-means. He had to critically think through the uniqueness of his problem - customer classification - to decide which technique was best for him. 

Mujtaba Anwer shared similar experiences. He used several metrics to evaluate the clusters. Metrics such as the within-cluster sum of squares (WCCS), silhouette score, Calinski-Harabasz index, also called the variance ratio criterion, and so on. 

## #5 K-means can be used for feature selection

In the power k-means episode, Jason spoke about the possibility of simultaneously using k-means as a feature selection algorithm. In his case, the algorithm did not only find clusters in the dataset but also intrinsically found the most important features that influenced the clusters. He accomplished this by using entropy weights as an extension of power k-means.  

## #6\. The result of K-means can be understood.

For real-world data with more than 3 features, it is difficult to intuitively understand the result of your k-means results. But from Lucas’ research work, as discussed in the explainable k-means episode, we see efforts to understand k-means results by replacing the borders of the clusters with the borders of a binary decision tree. In simple terms, the binary decision tree answers yes/no questions about the individual clusters, making it explainable. 

## Wrapping up

Throughout the season, we were inundated with eye-opening research that applied k-means. It goes to show how ubiquitous k-means have become and how the algorithm can fit into virtually any problem. Furthermore, it is apparent that progressive work is being done to better the performance of the vanilla k-means algorithm. This is indicative in the several other variants of k-means following Lloyd’s algorithm. They include power k-means, breathing k means, k means ++, explainable k-means, and so on.
