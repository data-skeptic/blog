## Very Large Corpora and Zipf's Law

The earliest efforts to apply machine learning to natural language tended to convert every token (every word, more or less) into a unique feature.  While techniques like stemming may have cut the number of unique tokens down, researchers always had to face a problem that was highly dimensional.  Naive Bayes algorithm was celebrated in NLP applications because of its ability to efficiently process highly dimensional data.

Of course, other algorithms were applied to natural language tasks as well.  While different algorithms had different strengths and weaknesses to different NLP problems, an early paper titled [Scaling to Very Very Large Corpora for Natural Language Disambiguation](https://courses.cs.cornell.edu/cs674/2004sp/materials/banko-brill-acl2001.pdf) popularized one somewhat surprising idea.  For many NLP tasks, simply providing a large corpus of examples not only improved accuracy, but it also showed that asymptotically, some algorithms yielded more improvement from working on very, very large corpora.

Although not explicitly in about NLP, the noteworthy paper [The Unreasonable Effectiveness of Data](https://static.googleusercontent.com/media/research.google.com/en//pubs/archive/35179.pdf) emphasizes this point further while paying homage to the classic treatise [The Unreasonable Effectiveness of Mathematics in the Natural Sciences](https://www.dartmouth.edu/~matc/MathDrama/reading/Wigner.html).

In this episode Kyle, shares a few thoughts along these lines with Linh Da.

The discussion winds up with a brief introduction to Zipf's law.  When applied to natural language, Zipf's law states that the frequency of any given word in a corpus (regardless of language) will be proportional to its rank in the frequency table.

