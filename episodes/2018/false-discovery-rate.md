## False Discovery Rate

A false discovery rate (FDR) is a methodology that can be useful when struggling with the problem of multiple comparisons.

In any experiment, if the experimenter checks more than one dependent variable, then they are making multiple comparisons.  Naturally, if you make enough comparisons, you will eventually find some correlation.

Classically, people applied the [Bonferroni Correction](https://dataskeptic.com/blog/episodes/2016/bonferroni-correction).  In essence, this procedure dictates that you should lower your [p-value](https://dataskeptic.com/blog/episodes/2014/p-values) (raise your standard of evidence) by a specific amount depending on the number of variables you're considering.  While effective, this methodology is strict about preventing false positives (type i errors).  You aren't likely to find evidence for a hypothesis that is actually false using Bonferroni.  However, your exuberance to avoid type i errors may have introduced some type ii errors.  There could be some hypotheses that are actually true, which you did not notice.

This episode covers an alternative known as false discovery rates.  The essence of this method is to make more specific adjustments to your expectation of what p-value is sufficient evidence.  If you create totally random data (I recommend doing this as homework) and then running statistical tests on that data, you will find your empirical results to be remarkably aligned with what theory tells you.  Tests on random data will give you 5% false positives with a p-value of 0.05 (by design) and you will get *uniformly* distributed p-values over all trials.  Try this same procedure looking for correlations (spurious or otherwise) on *real* data and you'll always find a non-uniform distribution.  Why?

What I referred to as "real" data is only considered real / valid because it's describing something that's interesting.  Whether it's your personal finances, rain water data, sports scores, or observations from the LHC, these are all datasets. that describe something systematic.  The only dataset we could think of which is totally random that certain people might take an interest in is the lottery.  Systems of interest produce data with correlations.  Regardless of how noisy the data is or the precision and completeness of your observations, the dataset won't be totally random.  Thus, performing arbitrary statistical tests on it will *not* yield the same uniform distribution of p-values.

This is the kernel of wisdom that helped seed the FDR methodology.  Using these techniques, one can achieve more "discoveries" (test hypotheses which turn out to be true) than you would with the Bonferroni Correction, however, you do this by accepting a controllable false discovery rate.  Essentially, of those novel discoveries you're achieving, some predictable percentage of them are incorrect.

Here are some coding links that might be useful to you:

* [FDR in sklearn](http://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.SelectFdr.html)
* [A more extensive python package](https://github.com/puolival/multipy)
* [FDR in R](http://strimmerlab.org/notes/fdr.html)
* [A quick example notebook](https://martinos.org/mne/stable/auto_examples/stats/plot_fdr_stats_evoked.html)





