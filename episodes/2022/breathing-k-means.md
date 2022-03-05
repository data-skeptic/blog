# Breathing K-means

In this episode, we interview Bernd Fritzke, an experienced financial expert and academic researcher. Bernd has research experience in self-organizing networks from the 90s and recently started a research study in K-means algorithms. He specifically discusses his latest work with us - The breathing K-means algorithm.

Bernd began by explaining why neural networks have experienced massive exposure in the last couple of years and how he got interested in it after years of working in the financial sector. 

He then went on to explain the specific areas that require improvement in K-means despite the many other alternate algorithms in the field. The first step to improving an algorithm is to understand what a bad result looks like? For K-means, it is a situation where the centroids cover a large area of distributed vectors – something Bernd spoke about. 

While novel K-means variations such as K-means ++ attempts to deliver smart centroid initialization and then run Lloyd’s algorithm, Bernd’s breathing K-means model goes beyond that. He extensively discussed the uniqueness of the model and how it worked. He additionally talked about the steps you can take to appreciably reduce the algorithm’s error. 

Since this algorithm has a number of multi-level steps during implementation, one would worry about the computation cost. Bernd however cleared the air on the computational demand when running the breathing K-means algorithm and how he managed to keep it relatively inexpensive. Another consideration was the time it takes for the algorithm to run and converge to a global minimum. 

Going forward, Bernd discussed how efficient the K-means breathing algorithm is when stacked against other K-means variants such as the K-means ++. Bernd then spoke about how some algorithms perform differently based on the dataset it was trained on and how the breathing algorithm is robust to a wide range of datasets, even real-life datasets. The challenge was to objectively compare K-means algorithms using a unified dataset. He explained how the main problem was not just good centroid initialization but vector quantization among vectors.

Another important subject of discussion was the interpretation of results. While K-means could cluster data quite quickly, the perceptual meaning of those clusters is largely vague. Bernd discussed how the breathing K-means tackles this. He also spoke about how he managed to have a balance in both computational efficiency and algorithm performance. 

Wrapping up, Bernd discussed other similar similar works to the breathing K-means algorithm. That includes the [simple random swap algorithm](https://journalofbigdata.springeropen.com/articles/10.1186/s40537-018-0122-y) and [genetic algorithm](https://scholar.google.com.au/citations?view_op=view_citation&hl=th&user=gOBacy8AAAAJ&citation_for_view=gOBacy8AAAAJ:u-x6o8ySG0sC) by Pasi Fränti from Finland.

Finally, Berned discussed an important attribute of breathing K-means – the ability to freeze (or delete) centroids without plunging the algorithm’s performance.  Interestingly, Bernd created a PyPI package where you can install breathing K-means on your local machine. The PyPI package is called [bkmeans](https://pypi.org/project/bkmeans/) and can simply be installed with pip.
