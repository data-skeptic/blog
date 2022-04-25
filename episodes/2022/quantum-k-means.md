## Quantum K-means

In this episode, we speak with Jonas Landman, a Postdoc candidate in Quantum Machine Learning at the University of Edinburgh. His Ph.D. and Postdoc thesis is centered around quantum algorithms for machine learning. Jonas speaks with us about quantum computing in machine learning. 

He begins by elucidating on the general idea that quantum computing is better than classical computing in all use cases. The postdoc candidate then gave an overview of how quantum computing works. Additionally, Jonas talked about the use of quantum computing in solving machine learning problems, particularly k-means using different strategies.

In this talk, Jonas referenced his [paper](https://arxiv.org/abs/1812.03584), where he and other researchers used a quantum circuit to compute the distance between two points in k-means.   He also discussed whether the [no-cloning theorem](https://en.wikipedia.org/wiki/No-cloning_theorem#:~:text=In%20physics%2C%20the%20no%2Dcloning,of%20quantum%20computing%20among%20others.) applies in the k-means quantum learning also called q-means. Going forward, Jonas explained how quantum computing helped in finding the distance in the classical k-means. This method makes each centroid iteration faster however the number of clusters, k may be a bit noisier. Jonas discussed why this was the case.

He also juxtaposed between q-means and k-means - how they have similar processes with respect to seed initialization and smart centroid initialization. In addition, Jonas explained what q-RAM means and how it was implemented in quantum learning. 

Jonas also talked about the other machine learning methods that quantum learning can be applied to outside k-means. These methods include Gaussian distribution, spectral clustering, etc. 

Speaking of the results in contrast with classical methods, Jonas explained how and why some results seemed counterintuitive. For instance, how in classical computing, the value of the vector components does not interfere with the running time. In quantum computing, however, it does. 

Jonas also spoke about the shallow quantum problem and how it applied in their work. Model evaluation of both quantum and classical learning was done using the MNIST dataset. He discussed some of the tradeoffs that played out in their observed result. 

Wrapping up, Jonas slightly touched on his [study](https://arxiv.org/abs/2007.00280) around spectral clustering in quantum computing and the findings from that study.

You can follow his work on the [arxiv](https://arxiv.org/search/quant-ph?searchtype=author&query=Landman%2C+J) or check some of his [Medium posts](https://medium.com/@jonasldmn).
