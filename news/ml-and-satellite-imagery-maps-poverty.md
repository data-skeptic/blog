## Machine Learning and Satellite Imagery Maps Poverty in Africa

Last year, a department within the United Nations published several global ideals, including eliminating poverty by 2030. However, as many experts argue, fixing wealth disparities requires first knowing the locations of the world's poorest places. Economic data is often scarce or not collected in poor countries, and analysts know they can take a notable first step towards getting rid of poverty by collecting data.

### Satellite Images Educate Stanford Researchers

Experts from Stanford University's Center on Food Security and the Environment quickly learned how difficult it is to obtain local data about poverty. Generally, people can point to areas of the world with problematic poverty levels, but find it significantly tougher to authoritatively determine the economic standing of certain communities.

After pondering issues associated with the dearth of local data, scientists realized useful information about areas of poverty already exists. Namely, it's from satellites, which transmit such information constantly. Before long, scientists discovered new ways of viewing the data to get details about poverty levels.

As a starting point, [they scrutinized satellite data](http://www.zmescience.com/ecology/world-problems/stanford-scientists-space-22082016/) showing the level communities used lights at night. Researchers hypothesized poorer places might use nighttime lights less often. However, they recognized a lack of nighttime lights doesn't indicate the degree of poverty, and agreed this method was misleading.

With that shortcoming in mind, Stanford's scientists took a closer look, although that was initially difficult due to a limited amount of available imagery. Standard methods of poring over such data work best when there's already a large informational pool to dip into, and that wasn't the case here. The researchers persevered and discovered the worthiness of comparing satellite images captured during the day and night and figuring out shared characteristics among impoverished communities.

### Developing a Machine-Learning Algorithm

The diligent scientists [developed a machine-learning algorithm](http://newatlas.com/stanford-satellite-imagery-poverty/44997/) that helped them contrast differences between the daytime and nighttime characteristics of the respective communities.

Thanks to fine tuning, the algorithm looked for things that generally represent economic prosperity, such as well-developed roadways and carefully tended, sprawling farmlands.

Working with big data sets with multiple variables is a constant challenge for people who work with machine-learning methods. However, those specialists usually follow a basic plan for getting started. Initially, they find a data set with a known target variable.

These scientists rely on the onboard computers of satellites in orbit. [Satellite computers must withstand extreme radiation](http://www.makeitdaisy.com/questions-to-ask-when-purchasing-an-industrial-computer/) to effectively record and transmit data back to scientists. In this case, the Stanford scientists trained their algorithm with millions of daytime satellite images.

Currently, daytime satellite data comes from Google Images and nighttime imagery from the National Geophysical Data Center. Engineers at the latter organization use their technology to view populated areas at a moderate spatial resolution.

During the Stanford project, each daytime picture had a corresponding number indicating the brightness of the area at night. Therefore, the algorithm spotted corresponding nighttime light values.

Next, the team trained an additional computer model that [accurately predicted previously hidden variables](http://www.sciencemag.org/news/2016/08/satellite-images-can-map-poverty) and contrasted the minute differences in image data, along with survey data about per capita income. The second model estimated the relative level of poverty from an asset-based index of wealth and consumption expenditures in 2011 dollar values. It also used a ridge regression model, which understands connections between land characteristics and lights.

This system can pull up high-resolution images for almost any part of the globe. Furthermore, the Stanford team expanded its methods and is now experimenting with different image resolutions to uncover alternative information, hopefully making poverty estimates even more accurate. Eventually, it may only be necessary to train the model with satellite imagery from regions scientists want to evaluate further, rather than millions of images.

While documenting the study's progress, scientists used their methods in African countries, chosen because of their typically high percentage of poverty, along with relatively strong existing survey data. As mentioned previously, survey data is scarce, often because it's not collected as often as required or at all. Data compiled between 2000 and 2010 by the World Bank showed 39 out of 59 African countries [collected two or fewer surveys that were extensive enough for worthwhile poverty measurements](http://spectrum.ieee.org/tech-talk/aerospace/satellites/fighting-poverty-with-satellite-data-and-machine-learning-wizardry).

The Stanford scientists concluded their satellite-aided method was better than existing approaches at exploring wealth distribution. Furthermore, since the satellite images already exist, this is a relatively cheap way of gathering information, not to mention an easily scalable option.

### Why This Method Is Superior

This is not the first time scientists looked at non-conventional predictors of poverty. In the past, mobile phone metadata from calls and texts was used instead of satellites as a predictor of wealth. Scientists polled 1,000 randomly selected participants from Rwanda about their mobile phone habits.

Survey responses were connected to metadata from a Rwandan phone company to compare and contrast the findings. However, mobile phone data isn't generally publically available like satellite images. Plus, Rwanda has millions of inhabitants, so a sample size of just 1,000 is arguably too small.

Even so, researchers learned [several interesting things from this mobile phone poverty indicator study](http://www.washington.edu/news/2015/11/30/uw-researchers-estimate-poverty-and-wealth-from-cell-phone-metadata/), including that wealthier people tend to buy bigger chunks of call credit than poorer individuals and usually make more overall calls than people with less income. Furthermore, the study showed poorer people in Rwanda generally received more calls than they placed, presumably because Rwandan callers pay fees.

### What's Next?

Experts not involved in the Stanford study suggest future methods of research about African poverty will follow the lead of the metadata mobile phone study above by combining their satellite imagery research with surveys. Using both types of information together gives a more accurate picture than either type of data on its own.

There's also a possibility of conducting this type of research in other parts of the world. Analysts suggest one of the reasons why the Stanford methodology worked so well is because the African countries chosen resisted the trend towards urbanization. Although the satellite imaging technology in urban areas may not be as effective as in the rural places, it'd probably still work.

The examples in this article shed light on efforts of scientists who not only know poverty exists, but also want to use their expertise, along with the available technology, to eradicate it. Thanks

to continual innovation, it's anyone's guess how the findings unveiled recently through satellite data, mobile phone metadata, and surveys may improve even more over time and help committed individuals move ever close towards making poverty a thing of the past.