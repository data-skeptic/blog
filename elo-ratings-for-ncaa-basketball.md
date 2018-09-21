## ELO Ratings for NCAA Basketball

After reading Kyle's blog post on creating [ELO rankings for chess](https://dataskeptic.com/blog/methods/2017/calculating-an-elo-rating) and fivethirtyeight.com's articles for [basketball](https://fivethirtyeight.com/features/how-fivethirtyeight-is-forecasting-the-2016-ncaa-tournament/) and [football](https://fivethirtyeight.com/features/introducing-nfl-elo-ratings/), I was psyched to try and create my own rankings and test them out.  Each year, [kaggle.com](https://kaggle.com) hosts a machine learning competition where participants put their prediction skills to the test for the NCAA tournament.

Most, if not all of you have probably filled out an NCAA tournament bracket where the goal is to pick the winner of each game.  Filling out a bracket gives you a rooting interest in each game and is one of the reasons the tournament is so popular.

The kaggle competition is slightly different from the typical tournament pool because instead of picking winners of games, the predictions are the probability team 1 will beat team 2.  So, instead of thinking deterministically, this competition forces you to think probabilistically.

In order to score each participant's entry, kaggle uses a log loss function.  Below is the log loss function for this contest:

$\frac{-1}{n} \sum_{i=1}^{n} \big[y_i \log(\hat{y_i}) + (1-y_i) \cdot \log (1 - \hat{y_i})\big]$

where:

<ol>
  <li>$n$ is the number of games played</li>
  <li>$\hat{y_i}$ is the predicted probability of team 1 beating team 2</li>
  <li>$y_i$ is 1 if team 1 wins, 0 if team 2 wins</li>
  <li>`log()` is the natural (base $e$) logarithm</li>
</ol>

For this competition, a smaller log loss was better.  The use of the logarithm offers extreme punishment for high probabilities which are incorrect.  The graph below gives you a good indication of how this works.

![plot of chunk unnamed-chunk-1](tools-and-techniques/2018/elo-ratings-for-ncaa-basketball_img/unnamed-chunk-1-1.png)

You can see that if you give team 1 very little chance of winning and they do win, the log loss is very large.  For example, if you gave team 1 a 0.1% chance of winning and they did win, the log loss would be 6.91.  If you set your probability at zero, the log loss would be infinite.  On the flip side, if you gave team 1 a 95% chance of winning and they did win the log loss would be 0.51.

This would be very important to understand in this year's competition because the biggest upset in tournament history occurred when a 16 seed beat a number one seed for the first time in tournament history.

My ELO rankings were created using the dataset from the competition.  We were given the outcomes of every NCAA Division 1 basketball game since 1985.  One of the decisions I had to make at the beginning was determining what kind of priors I would use with my initial rankings.  I decided to use a uniform prior for every team at the start of 1985 season knowing they would initially be wrong.  The initial prior for every team was set to 1500.  

I also stole a tactic from fivethirtyeight.com's system and regressed each team's ranking to the mean based on what conference they played in at the end of every season.  For example, if Duke's ELO at the end of the season was 1800, and the mean ELO of the teams in its conference was 1500, Duke would start the next season with an initial ELO of 1650.  

One of the things that makes ELO so enticing is its simplicity.  For chess rankings there is only one parameter, "k".  K represents how much the rankings will change after a game has been played.  A higher "k" will cause your rankings to change more rapidly while a smaller k will do the opposite.  A good way to think of it is a lower k will give more weight to your priors while a higher k will devalue them more.  In order to determine what value of k to use, I decided to take the value of k that had the highest winning percentage for NCAA tournament games since ultimately those are the games my entry would be judged on.  You can see in graph below k = 32 and k = 33 had the exact same winning percentage of just under 71.2%.  To break the tie, I calculated which k had the better log loss for the last two NCAA tournaments and k = 32 was the winner so I went with it.

![plot of chunk unnamed-chunk-2](tools-and-techniques/2018/elo-ratings-for-ncaa-basketball_img/unnamed-chunk-2-1.png)

One factor I also wanted to account for in my model was home court advantage.  During the NCAA tournament, the games are played on a neutral court so there wouldn't be a home court advantage.  However, during the season most of the games are played at a home site and so I wanted to take that into account as I updated my rankings.  Based on my testing, playing at home was worth about four points to the home team.  

So, how did I do?  When I back tested my model against the 2016 and 2017 tournaments my log loss was 0.5609 in 2016 and 0.5218 in 2017.  The log loss numbers themselves don't mean much, it just gives a way to compare the entries.  My 2016 entry would have finished in 135th place out of 598 teams and 210th place out of 442 teams in the 2017 competition.  

Heading into this year's tournament, here were the top 10 teams in my ELO rankings in order of strength:


```
##              Team  ELO
## 1        Virginia 2002
## 2       Villanova 1959
## 3          Kansas 1938
## 4        Michigan 1914
## 5     Michigan St 1908
## 6  North Carolina 1891
## 7          Purdue 1887
## 8            Duke 1885
## 9         Arizona 1881
## 10     Cincinnati 1854
```

Four of the top five teams in my ELO rankings heading into the tournament were number one seeds which made me feel like my rankings passed the smell test. At the end of the tournament I finished in 44th place out of 934 entries.  One of the reasons I feel like I finished as high as I did was due to the large number of upsets in the tournament.  When I compared my rankings to other competitors and fivethirtyeight.com, I consistently had smaller win probabilities for the favorites.  Therefore, my log loss for many of the games where upsets occurred was smaller than other participants in the contest.  

In summary, a very simple ELO model with just two parameters was used to predict the  probabilities of one team beating another in the NCAA tournament.  The model outperformed more complex algorithms which were used by other participants in a kaggle competition.  In the future, I'd like to test if a simple ELO model could be used to create accurate rankings, win probabilities and point spreads for other sports.  
