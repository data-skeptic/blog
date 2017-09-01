# Zillow

In this episode, our host Kyle Polich is joined by guest Andy Martin, who is a Research Manager  on the Zestimate data science team at Zillow, the largest real estate search website in the United States. While Zillow offers several advanced statistical predictive products, Andy and Kyle’s discussion focuses on the Zestimate, which is Zillow’s home value forecast, created to give sellers and buyers as much information as possible about homes and the housing market at no cost. 

Zillow maintains a living database of roughly 110 million homes in the U.S., including homes for sale, rent, and even those that are not currently on the market. The data that Zillow gathers is very heterogenous in nature, as it builds from a wide range of disparate sources, incorporating yearly tax assessments, public county records, listings of homes for sale, listings of rental properties and mortgage information. Due to the richness in data, the Zestimate has grown to be an indispensable tool for homebuyers and sellers. 

Broadly, ‘Zestimates’ are estimated home values based on statistical and machine learning models that analyze hundreds of data points on each property. The main ingredients for the Zestimate rely on two different types of data. The first is the county level Zillow Home Value Forecast which forecasts the Zillow Home Value Index (ZHVI) and is produced using a variety of the data that comes from tax assessors. The forecast is combined with data from folks who facilitate real estate transaction and include the individual characteristics of the property. Such data is often richer, as it includes the home’s features and the past behavior of its Zestimate. 

The Zestimate is a natural application of regression technique. The Zestimate modeling framework contains numerous submodels, each estimating a home’s value via different valuation approaches and data inputs. Since neither side of a transaction is unbiased, the Zestimate was designed to give a good starting point for the estimate value of a home that is independent of any biases from either the seller or buyer. This means that the listing price is not a factor in the valuation submodels. 

To evaluate the Zestimate home valuation, the data science at Zillow computes the median absolute percent error, which compares the Zestimate to the eventual sale price of a home. Over the years, the Zestimate has improved the median margin of error-- from 14% at the start of Zestimate to ~5% today. But Andy and his data science team at Zillow are continually working to improve the accuracy of Zestimate home valuation even further. 

In May 2017, Zillow launched the Zillow Prize, a competition administered through Kaggle with a one million grand prize, as a challenge to increase the accuracy of Zestimate. Over two rounds, participants will develop an algorithm that makes predictions about the future sale prices of homes.


###Links mentioned during the interview:

[Zillow Talk: The New Rules of Real Estate (book)](https://www.amazon.com/Zillow-Talk-Rules-Real-Estate/dp/1455574740)

[Zillow Price Competition via Kaggle](https://www.kaggle.com/c/zillow-prize-1) 

[Zillow’s data science blog](https://www.zillow.com/data-science/)

[Careers at Zillow](https://www.zillow.com/careers/)



<!--Andrew Martin graduated from Stanford University in 2013 with an M.S. in Statistics. After earning his Master's degree, he began an independent consulting practice specializing in statistics. In 2014, Andrew joined Zillow's data science team as a Senior Data Scientist. He currently works as a Research Manager on the Zestimate team at Zillow's headquarters in Seattle, WA. Previously, Andrew received a B.S. in Computer and Information Sciences in 2006 from the University of Washington. From 2009 to 2011, Andrew worked at the Democratic National Committee as an Analytics Engineer for the Obama for America team.
-->
