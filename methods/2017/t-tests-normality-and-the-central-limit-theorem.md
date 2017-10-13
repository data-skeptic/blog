## T-tests, Normality, and the Central Limit Theorem

>Hi, 
>I was just listening to an old episode of Data Skeptic on the 'Student's t-distribution'.
>In the episode Kyle strongly emphasized that the populations that the samples are coming from need to be normally distributed. 
>I am currently studying [t-tests](https://dataskeptic.com/blog/episodes/2014/the-t-test) in an inferential statistics course and wanted to ask you if there is a misunderstanding here:
>I thought that one does not need to care what distribution governs the population (whether it is normal or not) because the sampling distribution will always be normally distributed due to [Central Limit Theorem](https://dataskeptic.com/blog/episodes/2015/the-central-limit-theorem). Maybe we are talking about different uses of the t-test. I was referring to the use of t-test to determine if a sample belongs to a population of a known mean or belongs to another population that is significantly different. In this case, the original population does not need to be distributed normally, am I wrong?

While they can be effectively used in combination, nothing intrinsically links the t-test with the central limit theorem.  If you can apply the central limit theorem, then indeed, you can expect that your independent trials become approximately normally distributed.  It's still worth doing a test of normality to convince yourself that this is the case, but the central limit theorem is pretty reliable in this way when you have a large enough sample available.

However, the central limit theorem also presumes you have something like groups of samples.  For example, perhaps you want to look at some interest measurement of demographic groups by the city they live in.  While the city one lives in could end up being totally independent of whatever you're measuring, this is a justifiable grouping in many situations.  Due to the central limit theorem, we'd expect that the means of samples taken from each city will be approximately normally distributed.

Yet, there could be some exceptions to this rule.  If those cities span two countries with vastly different economic circumnstances, then we'd probably expect a bimodal sampled distribution over income.  However, in my experience, issues like this are usually obvious to anticipate and avoid.

However, the central limit theorem isn't always readily applicable in an obvious way.  Let's say you have 100 men and 100 women do the long jump, and you'd like to know if there's a statistically significant difference between their leap distances.  There's no clear way to apply the central limit theorem.  You'd want to perform your hypothesis test against these two populations of 100.

This situation highlights the importance of checking for normality in your sample.  First of all, we expect no one to have a negative leap distance in the long jump (although never underestimate the power of clumsiness :) ).  My non-evidence based expectation is that the distribution over distances would not, in fact, be normally distributed.  People's athletic training and aptitude will have a wide variance, likely resulting in something that looks more like [Gamma distribution](https://www.probabilitycourse.com/images/chapter4/gamma-color.png) with low $\lambda$.  This assumption being true, normality doesn't hold, and the t-test is not applicable.

A common approach many take is to then transform your data to make it normally distributed.  While this is a good suggestion, it's one to execute with a bit of skepticism.  There are a lot of researcher degrees of freedom in that transformation that could cast doubt on the result.
