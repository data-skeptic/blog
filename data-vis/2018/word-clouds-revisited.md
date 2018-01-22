## Word Clouds Revisited

Listeners to the Data Skeptic podcast will recall an episode in which I put forward a call to arms suggesting: [Let's kill the word cloud](https://www.dataskeptic.com/blog/episodes/2016/kill-the-word-cloud).  I gave my strongest arguments for why I hate word clouds, but I didn't provide any empirical support for my point of view.

I was delighted last year to learn about the paper [Taking Word Clouds Apart: An Empirical Investigation of the Design Space for Keyword Summaries](https://medium.com/@FILWD/taking-word-clouds-apart-alternative-designs-for-word-clouds-and-some-research-based-guidelines-df91129aa806) by Christian Felix, Steven Franconeri, and Erico Bertini.  Yes, [THAT Enrico Bertini](http://datastori.es/).

"Taking Word Clouds Apart" describes several well designed experiments to empirically measure the usefulness of word clouds (or perhaps the lack thereof?).  This is the next noteworthy study in a small but growing tradition of data visualization researchers applying rigorous experimental design to draw quantitative conclusions about the effectiveness of various forms of visualization.  In essence, which plot is "best" can be answered with precision rather than opinion.

The study has a short but complete set of about eight references to prior work (all of which were new to me, so I appreciate the references).  Despite existing work studying text visualizations, the study states:

> One problem we identify is a lack of systematic breakdown on the design space into relevant components.... In our study we focus exclusively on how to visually encode this information and how different solutions may lead to different performance outcomes.

The paper generalizes the idea of word clouds to keyword summaries.  When designing a keyword summary, one has several decisions to make:

1. How should words be positioned in 2D space? (e.g. randomly, ordered, by similarity)

2. How should font sizes be assigned? (e.g. uniformly, weight by importance)

3. What role should color intensity play? (e.g. none, weight by importance)

4. Should other visual elements be included? (e.g. a bar to indicate some numeric value associated with a word)

The study described in the paper leveraged mechanical turk workers.  They were presented with various keyword summaries and then asked to participate in one of four types of tasks.  I will discuss two here.

*Magnitude Judgment* is a common test in evidence based data visualization design.  Here, the goal is for any visualization to more efficiently and precisely convey information to the viewer.  Thus, we can quiz the viewer after a test, asking questions like "What were the top 3 most important terms?" and see how closely their answers differ from ground truth.  In this way, we can identify characteristics of effective data visualization.

*Keyword Search* measures the time required for a participant to locate the presence (or absence) of a given word.  For search tasks, the measurement of interest is how much time it took the reader to observe the requested detail.

For brevity, I won't share any practical examples, but I believe you can imagine real world situations where a decision in one of these two categories is required from a human.  If the display of textual data informs that decision, then doing it effectively is as important as the decision that has to be made.

A significant portion of the paper defines the protocol by which they will set up a test and execute it in as unbiased a manner as possible.  I found no criticism here.

### Results

For tests of keyword searching, the paper concludes:

> Our main finding is that ordered lists help people find words more quickly than using solutions where the keywords are arranged randomly and unordered

On the surface, this sounds like an obvious confirmation.  To search a randomly ordered list, will require you to look at every element in the worst case.  The degree to which the user is aware of any ordering, they may exploit it to speed up their search.  This is a very nice result which better articulates one of my main criticisms of what I called "word clouds", namely, that the randomness is at best a lost opportunity.

The results of the paper show that in the case of keyword search, 

My main take away here is that on search tasks, ordering helps.  The manner in which you choose to order the data can improve your data visualization, but only within the realm of what the reader is able to observe and exploit.

More interesting to me personally were the investigations into magnitude judgments.  How well can the reader correctly recall quantitative details of a visualization once removed?  The study shows that including additional marks improved accuracy.  In other words, displaying a given word or phrase inside a rectangle whose size is proportionate to the weight of that phrase yielded significantly improved results.

Here again, we have a nice result, and one that casts doubt on what I had referred to as "word clouds".  Font size seems to be an empirically inferior approach compared to use of additional marks (e.g. rectangles) to convey information.  This starts to look more like a bar chart summarizing textual data then a "cloud" of any kind.  I'm personally taking this result as a vote in favor of killing the word cloud.

Across these two types of trials, the study found conflicting results about what design choices were best.  Its easy to see that this is because, like any good data visualization, the best results are going to be yielded when design decisions are chosen in context of the data.

> Regarding the shortcomings often mentioned regarding traditional word clouds, namely, the lack of natural reading order and the use of font size to encode quantitative information we find that these negative effects seem to be circumscribed to specific tasks.

So is it still time to kill the word cloud?  For me, I think it's time to be more specific!  I shall apply the phrase "word cloud" only in situations that are etymologically rigorous.  A "word cloud" should be composed of words.  This eliminates the excellent suggestion of this study that you include additional markings to increase accuracy.  Further, "cloud" suggests something nebulous, in contradiction to the main findings about the usefulness of ordering.

Thus, I shall continue to demand nothing short of death for what I call word clouds, but I'm glad to see papers like this which advance our understanding of how to efficiently convey data to human readers.


