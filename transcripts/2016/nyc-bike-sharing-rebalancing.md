## NYC Bike Sharing Rebalancing

Segment Intro: Data Skeptic features interviews with experts on topics related to data science all through the eye of scientific skepticism. 

**HOST**: Hui Xiong has a PhD in Computer Science from the [University of Minnesota Twin Cities](http://twin-cities.umn.edu/) and is currently a professor and Vice Chair in the Management Science and Information Systems Department. He's also the Director of the Rutgers Center for Information Assurance, an SCM distinguished scientist, and a senior member of IEEE. Dr. Xiong's general areas of interest are in data and knowledge engineering with a focus on developing effective and efficient data analysis techniques for merging data intensive applications. 

His recent work [Rebalancing Bike Sharing Systems](http://www.kdd.org/kdd2016/subtopic/view/rebalancing-bike-sharing-systems-a-multi-source-data-smart-optimization), A Multi-source Data Smart Optimization was presented at the KDD Conference earlier this year. And it's this paper I invited him here to discuss today. Hui, welcome to Data Skeptic. 

**HUI**: Thanks for the introduction. 

**HOST**: So maybe to begin with, could you tell us a little bit about bike sharing systems and what this rebalancing problem you're trying to solve actually is? 

**HUI**: Nowadays, in bigger of a city like New York City or Chicago or Los Angeles and also some other big cities in Europe and Asia, we have this result called the Bike Sharing System. So the purpose is to try to provide some missing links in public transportation system essentially in those cities so we will have a lot of stations. Those stations will provide the bicycles available for passengers to use. 

The key purpose for this bike sharing system, a key issue is to try to effectively balance the operation. The idea is very simple actually. During certain time periods for some stations, say for instance in New York City during the morning time, for some stations many people will take the bicycle and the ride to some other stations and then those stations will run out of bicycles. For some other stations, there are not enough docks available to put all these bicycles. 

So in this case, some stations, they're short of bicycles and there are some stations, they are having too many bicycles available there and the people cannot even put their bicycles to that station. So in this case, we will have to facilitate balancing operation to try to bring the bicycle from the station they already have too many available there to the station they don't have bicycle available. So this is what we call the rebalancing operation. 

In order to make this system to work effectively, the balancing operation is happening every day to make system more effective for people to use. 

**HOST**: Interesting. So the bikes rebalance from station to station. I know this, the work you and your colleagues did, this is new work. At least, it's new to me. 

**HUI**: Yes.

**HOST**: But bike share systems have been around for a while. So how was this problem solved historically?

**HUI**: In the history, we do have this problem called the inventory rebalancing problem. However, this problem is quite different. We do have some challenging issues. The first is say for instance in New York City, we have more or less 300 stations available. So in other words, this is a very large scale dynamic inventory optimization problem. 

The second challenge issue is the amount of what is dynamically dynamic inventory rebalancing is not the like traditionally people are doing this inventory rebalancing but we deal with some very static case. 

So basically, we hope this can be more frequently happening every day. Also, another big challenge is usually for the inventory rebalancing, they have to assumption. There's now result called the outlier station. So outlier station means that for some stations, their demand is so huge. This demand cannot be satisfied by rebalancing operation. 

So in other words, we needed to do this dynamically rebalancing with the existence in all these outlier stations. Actually, we do have the opportunity nowadays to try to make this rebalancing optimization happening is because of now we have a large scale of historic data. 

So in other words, now it's possible. We completely use data to our approach and it's always called the big data approach. We try to do this data to embrace the optimization. This is one major difference from traditional way we do this rebalancing optimization problem. 

**HOST**: So I definitely want to get into some of the specifics of the optimization. But for the moment, let's maybe just stay as the high level and assume you have the problem solved, that is, you know exactly which bikes need to move from station A to station B. Once you have that optimize plan in place, how was it carried out? 

**HUI**: In New York City say for instance, they 8 to 10 trucks and they are routinely moving those bicycles around. So basically, our research is trying to develop some optimized strategy. So we help try to schedule these rebalancing efforts in a more optimized way. 

So say for instance, we help them on how actually they can allocate their resource - their trucks and also try to make some plan for terminals and also help them for the scheduling for those kinds of continually. 

**HOST**: I see. So the service trucks move the bikes from station to station to rebalance and your optimization allows them to do so more efficiently. So if people working in New York City on bike sharing system haven't read your paper yet, maybe one naive thing they might try is go to the station that's most full, has the most bikes, and then take them to the most empty statement and drop them off there and then just repeat that process. Why would that be a poor solution? 

**HUI**: You mean the passenger? Tourist? 

**HOST**: The trucks. 

**HUI**: OK. Right now, the trucks, they can do this more like there's no guidance. So in other words, so we have more than 300 stations available there. For the common case, right now what they are doing is based on their experiences. Say for instance, they may receive the phone call or they may have those kinds of demands and they try to - say for instance, station A, they received the phone call, say, station A they're out of bicycle. Then they try to say bring some bicycle from the nearby station into that station. However, those situations are purely based on the experience. There's no guidance from all these different resource called the data effect. 

So our purpose is we try to understand the complete situation for every station. Say for instance, we know exactly for every station how many bicycles are available there. And also, we make the prediction in the next time period. So how many bicycles available in each station, we based on the current situation and also we based on our prediction result and we can do this optimized solution to try to schedule say for instance, for those 8 to 10 trucks more effectively. In this way, we can make the most use of all the bicycles available in the system. 

**HOST**: Yeah, I can see we're having a prediction is much better than waiting for a consumer complaint when the problems already risen. It makes sense to me that that's a big improvement. You had mentioned considering time. I can definitely see how weekdays versus weekends would have very different usage patterns and behaviors. Are there other factors you considered in formulating your predictions? 

**HUI**: Actually, that's a key point in the paper. Our prediction, say for instance, we predict that the pick-up demand and also drop-off demand for each station and we actually considered about the unique characteristics for this bike sharing system. 

Typically, the people using bicycle is affected by the weather condition. When we try to develop this prediction model to try to predict the pick-up demand and drop-off demand for each station, we considered the weather data. 

Say for instance, we considered the weather similarity between different time periods and also the raining days, snowy days. And also, we considered the wind, if whether windy and not windy, people will use the bicycle. And also we considered other weather conditions. 

So in other words, we considered temperature and wind and humidity and those information we use to try to capture difference and similarity. So in other words, we look at historic data. For one station, if we try to predict the pick-up demand for the next hour and we would look at the historical data, we try to catch top k most similar weather conditions. Then we try to use the demand in those periods as the prediction result for the current one.

**HOST**: That makes sense. Yeah, I can see where weather would be very important. I'm less inclined to ride in rainier inclement weather or things like that. It's not totally clear to me how you would compare the similarity of these two things because you have four different dimensions. Could you talk about how you formulate weather similarity? 

**HUI**: We considered the three types of similarity measurement. One is weather similarity. The second one is the temperature similarity. We considered the temperature similarity. And also, we considered the humidity wind speed and also the readability and similarity. All this information we extract from the weather report associated with different locations and the time. 

We would aggregate all these similarity measurements into one linear combination and we try to learn the parameter combined for each factor. 

**HOST**: Yeah, weather is a very novel and probably a very smart thing to include in the model. I'm looking right now at figure 3 in your paper, this being an audio podcast, I have to tell listeners to go to the show notes where they can get to your paper and see these figures as well but I'll describe it for those who can't. These figures are really intuitive. They describe how weather affects ridership. 

For example, I can see how as humidity increases, ridership decreases, and that makes perfect sense to me. I was surprised though at temperature. There's a point of discontinuity around maybe it's 48 degrees Fahrenheit in figure C where's there's a jump like a plateau. Do you have any insight into what that is or why people are behaving that way instead of a more like continuous gradient type of change? 

**HUI**: Yeah. We actually noticed this instance before. There might be some initial cause these things happening. One thing is we might have some missing data in the data we collected. That's the one thing that might cause these things to happen. 

However, because our prediction is based on this combined multiple factors so even one factor, they have some missing data or some noise, it will not impact too much on our combined prediction result. All our prediction results are very accurate. 

**HOST**: Makes sense. I think one of the strengths of your approach is that it's data-driven. So I was wondering if you could tell me a little bit about the raw data sets you have available. Where does your data come from? 

**HUI**: We have multiple data sources. One data source is the data from **[0:10:46]** system. This data can be publicly available and because they provide API so actually if you work with the API you can actually have this data free in a real time way to get all this data. 

So we have the location data for each station and also we have the demand information from every station. Say for instance, we connect with the API so every 5 seconds, we actually can read the data. So we exactly know how many bicycles are available in each station. And also, we get to access to the weather report for the New York City. So we have the weather data as well. So all these data we can have from public domain. 

**HOST**: Very interesting. So I assume you have information about the stations. We talked about how many open slots there are and things like that. But I'm curious about what you know about the individual rides. For example, if I went to a particular intersection and got a bike and went to a different place and drop it off, would you that transaction level data about me? 

**HUI**: So it works this way. For some bicycle riders, they have membership but we don't know exactly which rider actually take the bicycle due to this anonymity issue. But we do have ID. This ID cannot be linked to anyone but this ID can indicate if you have membership so we know you come back. But if you are a random passenger and using the system, we are not going to link to you come to the system or you disappear. 

This system first of all is purely anonymous. We do have one ID associated for every usage. However, if you have a membership so we might know that you come back. If you don't have a membership, we may not know if you come back again. 

**HOST**: I see. So I know a few people who are working in New York City and they're cyclists and they use that in their commute to go either from home to work or maybe from their subway stop to work and then back again at the end. I would guess if they do it every day, they're very efficient and direct which is easy to model. But there are also tourists and exercisers who have very different behavior. How do these different types of users affect your model? 

**HUI**: Yes. And actually, these are very interesting to help us predict our demand and the pick-up as well. If for some station, the usage is mostly coming from the people living around. Their usage pattern is more regular. If the usage pattern for certain station becomes more regular then the prediction for those stations becomes more accurate. 

In other words, we use these results for rebalancing efforts to be more effective. However, for some stations, most of the usage is actually coming from other people who are travelling to the New York City or they just come there for random use. So in this case, the usage for those stations become not so regular then in other words, our prediction result for those stations becomes less accurate. In other words, if we use this information for our rebalancing efforts then our rebalancing becomes less effective. 

**HOST**: So every optimization problem has an objective function you're trying to optimize for. 

**HUI**: Yes.

**HOST**: What are you trying to optimize for the rebalancing problem?

**HUI**: Let me first introduce our rebalancing strategy from a higher level. So this is a very challenging problem. First, we have more than 300 stations. So this is a very large scale rebalancing effort. If we're using the traditional way to do this rebalancing optimization, the problem is infeasible.  Infeasible means if we use all these data together, all these stations together, we cannot find an optimized solution. 

So instead, we have a new strategy to doing this. We first are doing the clustering.  We try to group the other stations available in the New York City into say for instance, 8 or to 10 clusters based on a lot of usage pattern we derived them first. 

For each cluster, we assign one truck. So in other words, one truck is only responsible for rebalancing operation we've seen in one cluster. So in other words, these bicycles will not go all the way to New York City. They are only stay in one region. We try to coordinate all these rebalancing efforts for all the stations available in this area.

This way, we reduce a very complex problem. It's more like the divide and conquer. We try to reduce the very complex problem into some small problem it becomes feasible. In other words, it's possible for us to finally optimize the solution using this region. 

**HOST**: That makes sense. And then one truck per region I suppose. But I assume there must be some additional constraints. For example, trucks don't have an infinite space. What are the other constraints you have to deal with? 

**HUI**: Because every truck, they only have a limited capacity, so that's another thing I just mentioned in the beginning. So another big challenge is outlier station. They have unlimited amount to go beyond any truck can be satisfied. So in other words, for all these outlier station, we first needed to identify and then remove those outlier station. 

In other words, our optimization system will not work due to the existence of this outlier station. So we were forced to remove all these outlier stations. Otherwise, the optimization cannot be done. 

**HOST**: When you have that clustering solution in place and each truck has been assigned its jurisdiction area, is it then a bit like the travelling salesman problem? 

**HUI**: Actually, it's more like divide and conquer. We try to divide a very big complex problem into a small problem for the big problem like large scale station rebalancing problem, it becomes infeasible we cannot find the optimized solution. Then we divide this big problem using custom technique into some smaller ones. Then using each cluster then we can find to optimize the solution for the rebalancing efforts. 

**HOST**: Got you. And then within those clusters, what are you trying to minimize or maybe maximize over for each truck? Is it minimize the fuel usage or the time? 

**HUI**: Basically, we try to minimize the movement for the truck to do and also try to make every station within the area so it becomes more available for the user request.

**HOST**: That's interesting. So am I correct in saying that the goal is to keep the stations at a balance between supply and demand? 

**HUI**: Right. And also try to help the truck to travel less and to move more effectively. 

**HOST**: So it seems like a pretty complex system, the whole bike share system. Even as the trucks are out there executing a plan, different cyclists are still getting and returning bikes at stations is always changing. 

**HUI**: Right. 

**HOST**: What are some of the added challenges that arise from the dynamic nature of this problem? 

**HUI**: Actually, that's the key from traditional inventory optimization problem. This is more like a dynamic rebalancing optimization problem. That's why the dynamic prediction for the station drop-off demand and the pick-up demand becomes very important. And that's why we have this prediction model used in the system. 

So in other words, so our estimation for the demand is actually based on the prediction result for every dynamic time period.

**HOST**: So I also wanted to ask about the clustering approach you took. I think it's a smart thing to do to help take an intractable problem and make it tractable. But I was wondering about certain geographic features or maybe urban features like one-way streets that might affect this. For example, could you be overlooking a good plan that runs down a long north-south street and not considered because it's centroid would look less efficient than a more dense cluster? 

**HUI**: Yes. So when we do the clustering, we actually considered about all these geographic factors. Say for instance, so we consider about the location information. First, we try to group the stations nearby together. If we group all these stations nearby together then we can help the tuck not to move far away, just within nearby and that is what will be more effective. 

And the second that we considered about that all these stations, how actually they transfer their bicycles. So say for instance, some stations, they have more highway connection. Say for instance, a lot of people just simply during the morning time, they would travel from station A to station B. So all these connected the usage information will also be used when we do the clustering. 

**HOST**: And is the clustering a one-time solution that the trucks will use presumably forever or for a while or you need to regularly re-cluster? 

**HUI**: Right now, we're doing this one-time solution. However, if we notice a highway usage have changed say for instance the people changed their usage pattern quite significantly, we might have changed our cluster result slightly. 

**HOST**: Your approach includes many useful subsystems such as the demand prediction and the interstation bike transition function. Could you describe the general architecture of how all these things fit together? 

**HUI**: In terms of general architecture, it's actually not that complex. Basically, we're starting from the data. We have the weather report data. We have the trips records data. And we have all stations latest data. These three types of data sources, we are provided with all these data information to us. Then based on these data, we develop these similarity measurements. 

This similarity measurements can help us to build a prediction model to predict the pick-up demand based on the station data and also the trip records data. We can build this bike dropoff demand prediction. Then eventually based on the pick-up demand result and also the dropoff demand prediction result, we can actually build this station inventory target level result.

Once we have these results that we can fit into the cluster results. So basically in parallel, we already do these clustering beforehand. So once we've divided the whole New York City say like more or less 300 stations into like 10 clusters, we can fit all these prediction results into each cluster. And then of course, we already removed all these outliers. Then we can base on our prediction result to try to optimize our rebalancing efforts to try to make the suggestion for the planning for the truck removal or how actually they can move for all the added different time period. 

**HOST**: So your approach depends on good pick-up and drop-off demand predictions? 

**HUI**: Yes. 

**HOST**: How does it perform on the training data that you have available? 

**HUI**: If we do not consider these prediction results, we just say it using the approach we just introduced. We do the clustering. We derived the idea at the station into different groups then we try to use the traditional optimization strategy based on the current status of each station. Then the result is much worse than we consider this dynamic prediction. 

**HOST**: And in terms of measuring the performance of your system, how do you go about calculating that? 

**HUI**: So basically, as we described, our approach - we have a unique perspective. First, that we consider about the impact from the **[0:21:27]** **outlier**. We illustrate that even our validation, if we have all these **outlier** stations, in other words, their demand becomes extremely large value, a number value, and that the existing truck cannot be satisfied, if we remove this **outlier** our solution becomes more doable. So we first illustrate the impact from outlier. So in other words, we must remove this outlier before we can do any rebalancing operation. 

The second validation, we try to validate the importance of this dynamic prediction for different pick-up stations and also drop-off stations. After adding this dynamic prediction for the drop-off prediction and also pick-up demands then we can actually improve our results significantly. 

**HOST**: The paper has some really promising results. Since its release, has New York City shown any interest in implementing your methods? 

**HUI**: That's one thing we have in mind. Right now, we just use the historic data and try to validate the effect of the strategy. However, it will be more important and also becomes more practical if we can work with Citi Bike Company and try to deploy the system and see how it works in the real world situation. 

**HOST**: Yeah, that would be very exciting. 

**HUI**: Right, right. And actually, we have been trying to contact the them and also I sent the paper to them and to see whether they can use our strategy in their system. 

**HOST**: Well, very cool. I hope something actually ends up coming from that. 

**HUI**: Yes. And that's the goal for our research work. We've been doing this fundamental research because we are from university, we're doing non-profit research. From my own perspective, I try to use this real world data in trying to solve the problem. I hope in reality the company can use our strategy and at least try in their system. 

**HOST**: One of the things that excited me about your work is that [it's based entirely on open data](https://www.data.gov/developers/open-source). So I could get access on the same things you have. I could reproduce it. 

**HUI**: Right. 

**HOST**: Perhaps I could improve it. And the city could benefit from all those improvements with no added cost to the taxpayer outside of making the data open. 

**HUI**: Right. And this research can also be validated by many other researchers because all this data is publicly available and also our strategy and our approach becomes very informative in the paper and that people can repeat our experiments and also can actually implement our strategy. 

In my research group, I have been working for different types of problems. The solution to these problems - actually, we now reached the experiences from our many other data-related projects. For data-manning practitioner, it's extremely important to start from the real world problem and also the real world data and that you eventually come up to the solution which can be repeatable and also can be implemented by the industry or other researchers. This actually I believe has a lot of meaning to the society and also to the industry. 

**HOST**: Absolutely. Maybe a wrap up, could you mention some of the other projects your research group is working on?

**HUI**: Yes, certainly. Recently, The Economist, you know The Economist Magazine, right? 

**HOST**: Definitely. 

**HUI**: The Economist Magazine, there's one journalist who interviewed me and they published not the KDD paper. And so basically, in The Economist, they features all of our research work and also publish the KDD 2016. For that to work, we developed one methodology which is also based on the data available in the public transportation system. We use those data for the passenger travel in the public transportation system to try to identify pickpockets. 

**HOST**: Oh yeah, the pickpocket paper. I saw that but I have not read it yet. But it's at the very top of my list. I'm excited to go through it. 

**HUI**: That's an interesting one. And also, I have been working on another major effort for the paper analytics. I'm not sure if you're aware of this area or not. 

**HOST**: I am not. Tell me a little bit about it. 

**HUI**: Well, the paper analytics is unlike the tradition way that people are doing this human resource. The traditional way that people doing are doing human resource is purely, let's put it this way, is not data-driven. So in other words, it's really subjective. 

We want to develop some talented intelligent system that is purely based on the data. It's data-driven. So in other words, our position can be really objective. And also, will be more scientific-oriented. And also, our approach will be more transparent because we based on all the complete information available for the traditional people doing human resource position are based on what is recommended information. In other words, the information for decision-making may not be complete. 

We want to develop talented intelligent system that's purely based on the data and also the information will be more complete. I can give you an example. Say for instance, for the staffing, how actually we can recruit people. So basically, we can try answer the question based on the historic data. We try to predict which person is a better candidate for certain types of position. We can do the matching between the talent and also the job positions. So this will be matched based on the predict modeling. 

And also, we can do many other things like we identify like the kids who just graduated from college, we identify which kids will become more successful in the company. So in other words, we can identify employee staff before they become a staff. 

Another thing we're doing is we try to understand how employee like a star employee will leave the company. We try to make a prediction which employees are going to leave. If this employee leaves the company, we have enough here in the pipeline available for this position if this person leaves. 

All this human resource operation can actually be developed based on the data. We have new ways to collect all these data. Say for instance, in the big company, we have all this ERP system becomes available. And also, we have developed a system available for our information about our employees, about routine operation management and also position making. 

So all these information systems allow us to collect a huge amount of information about the talent. So based on this information, we can develop this talent intelligent system. This system can eventually help us to do a lot of management acquisition like staffing compensation and the benefit. And also like how actually we can build the leadership among the employees and to make this become a data driven way to do things. 

I believe this is going to be the future for the human resource management. 

**HOST**: Yeah, I hope so. Any transparent analytical data-driven solution sounds like a good path to me. Well Hui, thank you so much. I really enjoyed all the work your research group is doing. I look forward to seeing what else comes from you guys. And I'm grateful you came on the show to share your thoughts with our listeners today. 

**HUI**: Yes. Thank you for inviting me to be here. It's my great pleasure to [introduce my research work](http://www.kdd.org/kdd2016/papers/files/rfp0553-liuAemb.pdf). 

**HOST**: Excellent: Well, take care, Hui. 

**HUI**: Yeah. Bye-bye. 

**HOST**: One quick announcement before we sign off. Santa Clara, California, November 4-6, 2016 is the Open Data Science Conference West. I'll be there. I'm not presenting, just attending, but I'm looking to meet up with anybody from the Data Science listener based or Data Science community in general. I'm going to plan some sort of informal meet-up. I don't have a location yet but I'm going to give you a URL to keep checking. It's DataSkeptic.com/ODSC, that's Open Data Science Conference. 

I'll post updated details because these sorts of things can often have a last minute change. That will be the official canonical place to find details about meeting up or hanging out or just getting in touch. Anyone who is there, be sure to come by. I'm giving out Data Science tech stickers so come say hello. 

And until next time, I want to remind everyone to keep thinking skeptically of and with data. 

**Exit Voice-over**: For more on this episode, visit [DataSkeptic.com](www.dataskeptic.com). If you enjoyed the show, please give us a review on [iTunes](https://itunes.apple.com/us/podcast/data-skeptic/id890348705?mt=2) or [Stitcher](http://www.stitcher.com/podcast/data-skeptic-podcast/the-data-skeptic-podcast). 