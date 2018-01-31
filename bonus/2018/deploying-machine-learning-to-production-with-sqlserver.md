## Deploying Machine Learning to Production with MS SQL Server

A dirty secret of machine learning in industry is how often people re-invent the wheel figuring out how to deploy their models into a production environment.  Largely, this is due to the lack of canonical tools that have all the necessary bells and whistles.  As a result, many people re-invent the wheel when figuring out how to take the work of their data scientists into production.

When my career began, it was common for software teams to be in languages like Java, .NET, Ruby, and PHP.  In contrast the people who today would probably have the title "data scientist" were more likely to use Matlab, R, or perhaps C++ or Perl.  Python was not yet so popular to my recollection.  In some situations, companies decided that taking work to production required the work of a data scientist (perhaps written in R) to be re-written in Java (or some other language) to be "production worthy".

Admittedly, you have one very nice benefit with this process.  When the second implementation occurs, it's implementors have the benefit of hindsight not available when the first group figured out how to do it.  What they create should be better structured and optimized.  Further, both systems should have exact parity, so it's a nice validation that should be easy to implement.

Having said that, this benefit is exponentially minimized by the inefficiencies of this process.  Since then the "translate for production" strategy has been widely acknowledged as the wrong approach.  Despite this, we still lack tooling that is robust, powerful, and ubiquitous for deploying, monitoring, and managing models in a production environment.  However, that's beginning to change.

Amongst the solutions being taken seriously by organizations is the use of model deployment into a SQLServer instance.  In this episode, I discuss the process with ???

Tobias
Close to data
Security (doesn't leave database)
