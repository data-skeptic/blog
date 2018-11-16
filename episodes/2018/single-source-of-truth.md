## Single Source of Truth

In mathematics, truth is universal.  In data, truth lies in the where clause of the query.

As large organizations have grown to rely on their data more significantly for decision making, a common problem is not being able to agree on what the data is.

As the volume and velocity of data grow, challenges emerge in answering questions with precision.  A simple question like "what was the revenue yesterday" could become mired in details.  Did your query account for transactions that haven't been finalized?  If I query again later, should I exclude orders that have been returned since the last query?  What time zone should I use?  The list goes on and on.

In any large enough organization, you are also likely to find multiple copies if the same data.  Independent systems might record the same information with slight variance.  Sometimes systems will import data from other systems; a process which could become out of sync for several reasons.

For any sufficiently large system, answering analytical questions with precision can become a non-trivial challenge.  The business intelligence community aspires to provide a "single source of truth" - one canonical place where data consumers can go to get precise, reliable, and trusted answers to their analytical questions.