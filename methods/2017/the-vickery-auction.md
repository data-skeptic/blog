## The Vickery Auction

In tomorrow's episode of the podcast, I'll be discussing online ad auction markets with my guest.  Many of these ad serving platforms run as a real time auction, and a good deal of study has gone into deciding on the best mechanism for running those auctions.  By mechanism, I mean the process by which all participants get to offer bids, and the system decides which bid to accept, and what to charge the winner.

In truth, real online ad auctions are a bit more complex that what I'll describe in this post, but at their core is some idea either directly using or inspired by the concept of the Vickery auction.  In this style of auction, the person with the highest bid wins, but they have to pay the price offered by the second highest bidder.  Isn't the auction house losing money this way?  A specious case could be made for this claim, but if you trust the equilibria strategy, this mechanism has a few nice properties.  The equilibria strategy (discussed below) suggests that the "smartest" players should bid their actual true value derived from winning the auction as their bid.

Let's start with the claim, and then unpack it.  The Vickery auction's equilibria strategy (more on what that means later) is for all bidders to bid their true valuation of the good or service being offered.  In other words, if a piece of fine art is being sold and you believe your enjoyment of owning that artwork is equal to the enjoyment you'd recieve spending $100 in some other fashion, then the artwork's true valuation from your personal perspective is $100.

If the art were being offered for a fixed cost of $90, you'd be silly *not* to buy it, since you'd reap $100 worth of enjoyment.  If the art were being offered for a fixed cost of $110, you'd be silly if you chose to buy it, since you expect to gain less monetary enjoyment than the cost.

It can seem difficult or impossible to equate enjoyment of art with a particular dollar value.  If you're struggling with that concept, think of the idea in a more business setting.  Let's assume you sell widgets.  Each sale you make earns you $10.  In order to get sales, you first generate leads from people interested in buying widgets.  When you get your hands on a lead, you've found you have a 25% chance of convincing the person they should buy your brand of widgets.  That's often called the conversion rate.  On average, for every four leads, you get one sale, so on average, every lead generates an expected value of $2.50.  Another way of putting this is that for (on average) every four leads, you generate one $10 sale.

If you paid $2.50 per lead, you'd exactly break even.  You need to have some margin to profit from.  Depending on your minimum attractive rate of return (MARR), you're true valuation of a lead might be $2.00.  In this way, you might buy four leads which you are willing to pay $2 each, a total of $8.  You expect, on average, that one will convert, at a profit of $10, less the $8 advertising cost leaves you a $2 profit.

Naturally, if you could buy those leads for even cheaper, that leaves more profit for you to keep.  What if you're the best widget salesman in town?  All the other widget dealers have the worst widgets that ever did widget.  Why should you pay the full $2 per widget when you know full well your compeditors can only afford $1 per widget?

In a first price auction (where you pay exactly what you bid), you are encouraged to lower your bid strategically.  If you were somehow certain that the next bidder below you can only offer $1, your best bet is to offer $1.01, since you want to win, but not overpay.  In a first order auction, a smart agent would work hard at minimizing their bid.  The objective is to bid only a tiny amount above whoever will bid less than you.  You'll spend a lot of brain power and computational resources trying to guess that value and ultimately, offer as low a bid as possible while still expecting to win the auction.  Such a strategy might be great for you, but form the auction platform's perspective, it's not great.  In this case, the incentives are a bit perverse, in that the mechanism of the auction encourages participants to minimize their bids.

In the first price auction, you also have some adversarial behaviors that will come into play.  Let's say you're an underdog who realistically doesn't have a chance of winning.  Should you give up and go home?  Maybe.  On the other hand, what if you offer a bid that is not high enough to win, but high enough to cause your leading compeditor to incur additional expense?  Could you drain their budget by bidding them up?  Yes, in a first price auction, that sort of activity is essentially encouraged.

So the Vickery auction claims that it results in bidders who will choose to bid their true valuation.  Before we get into why you should believe this, lets explore why it's a nice result.  If bidders decide the best course of action is to reveal their true value to the auctioneer, then they will spend very little time trying to strategize how to bid.  Your true valuation should be pretty easy to decide.  If you adopt this strategy, you won't waste any time trying to compute the absolute minimum bid you can place and still win.  Similarly, your underdog compeditor won't waste any time trying to bid as high as possible to apply pressure to your cost.

That all sounds great, but why should we think anyone would comply with the assertion that the "best" strategy is to bid your true valuation?

It has to do with a concept in game theory known as an equilibria.  An equilibria is a set of strategies which players may adopt such that no player has a motivation to change their tactic.

Consider the game Rock, Paper, Scissors.  You can choose from an infinite number of strategies.  You might try and base your choice on what your opponent did last round, or what they did in the last ten rounds.  However, any regularity you might introduce (e.g. if you threw 'rock' last time, make sure not to throw 'rock' again next round) is a pattern.  Any pattern could be learned by your opponent.  Any pattern you generate could be exploited, thus it's best not to present any pattern.  The absence of a pattern is randomness, and therefore, flipping a three sided coin to randomly select your choice sounds like a promising option.

But what will your opponent do?  If they trust that you are behaving randomly, then there's no pattern for them to exploit.  If they do something silly like 'always show rock', at best, they will still only win one third of the time.  At worst, you'll see their pattern and exploit them.  Thus, if you're behaving randomly, the best choice is for them to also behave randomly.  There's no reason for either of you to deviate from this approach.

Granted, if one person *does* deviate, the other has some incentive to deviate as well.  The idea of an equilibria is based upon this argueably shakey position.  An equilibria is based on the strategies selected by *all* participants.  The equilibria does not specify how anyone should behave if a player chooses to engage in off-equilibria play.  In this sense, game theory is incomplete.  It doesn't fully specify the decisions an agent needs to make outside the equilibria itself.  That's probably a topic for another blog post, however.  Let's get back to why the Vickery auction is compelling.

The bid a participant choses to offer can be categorized into three buckets.  Let us first define $V_i$ to represent agent $i$'s true valuation $V$ of the auctioned item.  Let us define the bid of agent $i$ to be $b_i$.  This gives us strategies for which $b_i < V_i$, $b_i = V_i$, and $b_i > V_i$.  Let's explore each case.

First, we assume the auction mechanism is known.  A Vickery auction is a second place auction, meaning that the highest bidder wins, but they have to pay $0.01 more than the person who bid right below them.  If Kyle bids $10 and Linhda bids $8, then Kyle wins, but he must pay $8.01 to collect the prize.

To analyze each outcome, lets think of ourselves as agent $i$, and we will either win or lose the auction.  In cases where we win, let's call the 2nd place bidder agent $h$.  In cases where we lose, let's call the winning bidder agent $j$.  This notation is a bit different from what you'd find in the literature, but a it is handy because $h < i < j$.

For strategies involving $b_i < V_i$ (underbidding), either $i$ will win or lose the auction.

If you (agent $i$) wins, they pay $V_h$.  Since $i$ won the auction, we know that $V_i > V_h$, so regardless of what $b_i$ was, the cost is the same.  Thus, there is no incentive to raise your bid above the unknown value of $V_h$.

If instead, you (agent $i$) loses, then it means $b_i < b_j$.  Darn, you lost!  Did you offer a bid $b_i < V_i$?  That would be a stupid thing to do.  If you could have bid more but still less than or equal to your true valuation, then you'd have stood to benefit from winning the auction.

Thus, if you are underbidding you might miss out on potential wins that would have been profitable.  Even if you win while underbidding, you don't really benefit from it because the potential for "savings" doesn't exist since you pay a price that depends on your highest ranked competitor.

From the above arguement, we can establish that underbidding is irrational.  But what about overbidding?

Let's assume you're not likely to win the auction, could you somehow impose a cost on your winning opponent?  After all, if you are the second place bidder, then your opponent is going to pay a price that you set.  Wouldn't you want that to be as high as possible to exhaust their budget?

Again, we have two possibilities.  Either you will win or you will lose.  If you happen to win, the definition of overbidding specifies that $b_i > V_i$.  In other words, you will leave the auction remorseful and feeling like you are worse off than when you arrived.  Thus, winning while overbidding is a disaster that backfires on you.

How about overbidding and losing?  Yes, this could damage your opponent, but it's a strategy that is not without risk.  We should admit though, that there might be some benefit here, so let's put a pin in that and move on.

The third and final possibility is bidding your true valuation (i.e. $b_i = V_i$), which I'm arguing is the optimal thing for you to do.  If you win the auction, then you pay price $b_h$.  Since $b_h \le b_i$, you at least got a fiar price, and maybe you got some savings if b_h < b_i$.  If, instead you lose, then you net 0 from the process.  Although someone else won, you did not overpay.

So compare these two outcomes.

When you bid your true valuation, you will, at worse, achive a wash, but at best, have some savings when $b_h < b_i$.

However, if you bid $b_i > V_i$, then a loss brings you no added benefit (equivalent reward earned to winning when $b_i = V_i$).  In this sense, both bidding your true valuation and overbidding each have an outcome that is net zero.  However, if you happen to win when overbidding, you end up losing value.  The alternate case under the equilibria strategy could earn you some savings if the runner up has a value $b_h < b_i$.

What's better, some chance of no value with some chance of savings, or some chance of no value with some chance of losing money?  It seems of your three options, underbidding, overbidding, or bidding your true value, the best results are likely to be achieved when bidding your true value.

If you can arrive at this conclusion, then our opponent hsould be able to arrive at it as well.  Thus, if you assume your opponents will behave rationally, then you assume they'll all start playing this equilibria strategy as well.  If that happens, then there's no need to worry about what happens with off-equilibria bidding.

Further, any participant that choses not to adopt this equilibria strategy is likely to result in the unplesant outcomes described previously.  If they continue to behave irrationally, it's going to cost them money, which presumably puts them at a disadvantage for competing with you in the long run.  In this way, one might conjecture that an irrational agent (one that fairs to find and play the equilibria strategy) will eventually run out of capital and be forced out of the market.  Thus, the market self selects to those participants that can identify and play the equilibria strategy.

This last bit makes a few leaps worth being skeptical of.  The equilibria strategy is incomplete in that it does not specify what behavior one should adopt when off-equlibria play is taking place.  Further, since we must trust that all participants share the epiphany of proper bidding strategies, it also assumes perfect rationality and a common knowledge of perfect rationality.  These are general criticisms of game theoretic approaches that must be addressed in wider domains beyond the Vickery auction, but they show up here as well.

Regardless of those criticisms, in the online ad auction marketplace, it does seem that the direct costs imposed make it unrealistic that a participant could behave irrationally for a long period of time.  However, with how liberal VCs sometimes fund flawed ideas, it's entirely possible that millions of irrational dollars could enter these marketplaces.
