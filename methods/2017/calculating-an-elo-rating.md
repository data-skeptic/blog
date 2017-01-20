## Calculating an Elo Rating

As discussed in the most recent episode, chess uses the Elo Rating System to assign it's competitive players a score which represents their ability.  A new player with no game history is assigned an intial Elo rating of 1000.  Any score above 2000 is regarded as an expert level of play.

One's Elo rating can increase or decrease as a result of each game played.  The system is designed such that a winning player has their rating increased proportional to the the difference between their Elo and the opponents.  When a grandmaster players a novice, they have the potential to increase insignificantly.  On the other hand, a novice beating a grand master would yield a huge gain.

Accounting for the difference in Elo of the players is an important feature of the rating system that removes the strategy of a powerful player "picking on" significantly worse players for easy wins and easy points.  Yet, it simultaneous seems to not discourage this sort of play either.  To be sure, there are strategies employed specifically to increase or protect one's Elo rating, but the system seems well designed to minimize these.

Elo is not the only system for measuring chess performance, and Elo itself has a few variants.  My intent in this post is to give you a general understanding of the mechanics of plain vanilla Elo.

Chess is not a binary outcome (win/loss).  Players may often arrive at a draw.  Let a win be represented by a value of 1, a draw by 0.5, and a loss by 0.  Let these values be represented by $S_i$, meaning that if player $i$ wins, $S_i = 1$ and $S_j = 0$.

Let $r_i$ represent the initial Elo rating of player $i$.  To update it, we first convert it using a logistic function such that:

$R_i = 10^{\frac{r_i}{400}}$

These scores are often interpretted to calculate an expectation of the game's outcome such that the expectation that player $i$ wins or draws against player $j$ is given by

$E_i = \dfrac{R_i}{R_i + R_j}$

A scaling value known as $K$ is introduced before we get to our final calculation.  This parameter helps to control the amount of change that can occur per game.  A very low $K$ value prevents change, while a high $K$ value causes new ratings to be dominantly informed by the most recent performance.  Different organizations use different values, but a common value is $K=32$.

Once the outcome is known, the updated Elo rating $r'_i$ is given by:

$r'_i = r_i + K \cdot \big(S_i - E_i \big)$

Notice how this hinges on the expectation of a win $E_i$.  If the game is expected to be a fair match (equally skilled competitors, $E_i=0.5$) then we should expect a draw ($S_i=0.5$) as a common outcome, which would not update the score.

Similarily, a chess novice competing against a grand master would have a very low expectation of winning, so a loss would only come with the expense of a few points.  A win, on the other hand, would provide a huge difference, and thus, earn the upstart player $K$ points.  A finite value of $K$ also means that a new prodigy player must still engage in many matches to raise their score.

Let's do an example where $r_i=1000$, new player and $r_j=2853$ (the score of top player Magnus Carlsen).

$R_i = 10^{\frac{1000}{400}} = 316.23$

$R_j = 10^{\frac{2853}{400}} = 13567505.30$

Thus, the expectation that the new player will win is

$E_i = \dfrac{316.23}{316.23 + 13567505.30} = .00233%$

If, by chance, this new player wins, their posterior scores will be calculated ($K=32$) as

$r'_i = 1000 + 32 * (1 - 0.0000233) = 1032.00$

$r'_j = 2853 + 32 * (0 - 0.9999767) = 2821.00$

I thought it was interesting to note that this system has a built in assumption of linear skill.  It assumes players can be measured on one axis, which also implies a transitivity of skill.  I suppose this is generally true, but I'm curious about how strategic the game becomes where different styles of play might allow for a break in transitivity among certain rated players.  The presence of any such break would surely result in strategic partner selection for many.

In summation, Elo is a nice system for competitive games which have multiple competitive encounters resulting in a win/draw/loss outcome.  It accounts for differences in competitors abilities and rewards points commensurate with the expected outcome of the game.  It is relatively stable to outlier events and requires players to engage in many rounds of competition to achieve high ratings.
