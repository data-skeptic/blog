## Review of Azure Text Analytics

I believe we're going to see a continued trend towards commoditization of certain data science services.  The classic example is spam filtering, but even more potential could come out of areas like computer vision and text analytics.  The field and therefore the marketplace are evolving quickly, so every so often I like to run a few tests to see where certain services stand in their development.

In this short post, I demo a quick result of how Microsoft Cognitive Services Text Analytics API does key phrase extraction on some recent posts from the dataskeptic.com blog.  Details on this API can be found [here](https://westus.dev.cognitive.microsoft.com/docs/services/TextAnalytics.V2.0/operations/56f30ceeeda5650db055a3c6).

On the positive side, these key phrases are clearly the result of some entity extraction process.  The selected phrases are extracted from my text directly.  While the selections might be informed by some transfer learning after an algorithm was trained on some external corpus, the system behind this API is doing more than trying to shoehorn my text into it's pre-existing, inflexible taxonomy.  I like that the API is robust in this way.

On the negative side, these labels aren't directly useful for me.  These might be useful to a manual process where a human reviewer picks the most applicable terms.  In time, enough reviews of this sort might enable a simple classifier to be built to post-process this list.  Similarly, these labels might be useful for ensembling.  Perhaps these phrases as features might be useful in a model you're working on.  Yet, on their own, I wouldn't use these programmatically directly.

The rest of this post are the keywords for each of those blog posts so you can judge for yourself.

### Bees, lasers, and machine learning
*Blog post*: [dev.dataskeptic.com/projects/2017/bees-lasers-and-machine-learning.md](dev.dataskeptic.com/projects/2017/bees-lasers-and-machine-learning.md)

*Phrases*: No results returned

### Computation and Distraction
*Blog post*: [dev.dataskeptic.com/opinions/2017/computation-and-distraction.md](dev.dataskeptic.com/opinions/2017/computation-and-distraction.md)

*Phrases*: No results returned

### Calculating an Elo Rating
*Blog post*: [dev.dataskeptic.com/methods/2017/calculating-an-elo-rating.md](dev.dataskeptic.com/methods/2017/calculating-an-elo-rating.md)

*Phrases*: No results returned

### Millions of People Can't be Wrong
*Blog post*: [dev.dataskeptic.com/opinions/2017/millions-of-people-can't-be-wrong.md](dev.dataskeptic.com/opinions/2017/millions-of-people-can't-be-wrong.md)

*Phrases*: steering people, People Ca, k people, intersection of people, person conceeded, large enoug population of people, truth, unidentified object, occured, logical fallacy, line of arguement, UFO believer, reasonable way, pseudo-science attempt, fundamental science, election of Barack Obama, tempting line of thinking, believers, argumentum ad populum, types of cranks, bit of melodrama, Donald Trump, unsourced statistic, candidates, popular opinion, effective rhetorical device, scientific community, eventual consistency, single candidate, sky, extra terrestrial hypothesis, example, favor, presidential elections, case, h2, conclusion, position, start, response, href, ordinary explanation, voting age, grain of possibility, difference, minds, small subset, race, correct information, noteably, assumption, point, debates, Americans, angles, popularity, occasion, time, resources, fact, verifiers

### Dropout Isn't Just for Deep Learning
*Blog post*: [dev.dataskeptic.com/methods/2017/dropout-isnt-just-for-deep-learning.md](dev.dataskeptic.com/methods/2017/dropout-isnt-just-for-deep-learning.md)

*Phrases*: Multiple Additive Regression Trees, specialization, regression tree problems, initial batch of trees, particular tree, decision tree, deficiencies of teh existing trees, given tree, href, deep learning, ensemble, increased accuracy, Boosting techniques, XGBoost algorithm, performance results, extention of MART, DART, training data, training error, regularization technique, algorithm onunseen data, Journal of Machine Learning Research, statement, clever optimizations including boosting, bias, balance, capacity, rate of memorizing features, significant improvement, controlled manner, Rashmi, Gilad-Bachrach, useful technique, interesting paper, Dropouts, areas, diversity, mini-episode, odds, tunes algorithms, wel lcaptured, potential, strategy, neural networks, method, objective, random forest, h2, ensembling process, deviation, turn, fashion, gradient descent, applications, saying, Authors, Subsequent iterations, loss function, models, speed, hoewver, reader, idea, domains, stage

### Studying Competition and Gender Through Chess
*Blog post*: [dev.dataskeptic.com/episodes/2017/studying-competition-and-gender-through-chess.md](dev.dataskeptic.com/episodes/2017/studying-competition-and-gender-through-chess.md)

*Phrases*: Peter Backus, economics of charities, economics of charitable, Studying Competition, col-xs, div class, competitive chess, structured study, br, Fellow, col-sm, study of gender differences, areas, Institut d'Economia, private provisioning of public goods, Sanchez-Pages, labor market outcomes, interesting economic topics, summary, paper, Barcelona, ideal arena, people, University of Manchester, href, Cubel, Guid, Performance, Evidence, Real Tournaments, colleagues, numerous confounding factors, Prior work, IEB, img alt, discussion centers, response, Lecturer, h2, src, Mañas, research, row, PhD, conclusions, guest, Understanding

### Weather Data and The Library Problem
*Blog post*: [dev.dataskeptic.com/methods/2017/weather-data-and-the-library-problem.md](dev.dataskeptic.com/methods/2017/weather-data-and-the-library-problem.md)

*Phrases*: No results returned

### Missing411
*Blog post*: [dev.dataskeptic.com/skeptical-analysis/2017/missing411.md](dev.dataskeptic.com/skeptical-analysis/2017/missing411.md)

*Phrases*: disappearances cases, surprising cases, number of missing cases, frequency of missing persons cases, author David Paulides, aspects Paulides points, people, Missing411 conspiracy, National Park Service, Missing411 series of books, national parks, scent, headline of Missing411, mysterious range, matter, formal conspiracy, height, canines, recent talk, Skepticamp, Monterey County Skeptics, search time, search teams, claims, wild tales of alien abduction, iframe width, formal claim, numerous appearances, frequency of disappearances, expert, canine tracking abilities, paranormal radio programs, realm of possibility, way inexplicable, dogs unable, mythology, cold conditions, element of mystery, frameborder, unusual circumstances, src, allowfullscreen, clothing, transdimensional bigfoot, idea, rate, h2, body - living, expected baseline, element of mysteriousness, arguement, attendee, data, monitoring, topic, evidence, direction, reporting, href, mind, entirety, sense, accuracy, reader

### Dropout
*Blog post*: [dev.dataskeptic.com/episodes/2017/dropout.md](dev.dataskeptic.com/episodes/2017/dropout.md)

*Phrases*: Dropout, given layer, particular input, fighting overfitting, Deep learning, given problem, h2, iterations of learning, Simple Way, time, computational resources, href, network, core idea, neurons, method, paper, technique, signal

### Street View for Address Verification
*Blog post*: [dev.dataskeptic.com/methods/2017/street-view-for-address-verification.md](dev.dataskeptic.com/methods/2017/street-view-for-address-verification.md)

*Phrases*: home of listener, new home, delivery theft, current home, residential home, fact home, delivery professionals, single family home, online retailers, UPS delivery person, Google Street View data, old address, safe areas, Address Verification, streetside view, use of signature, Fortunate online shoppers, large retailers, image labeling, apartment building, multi-unit, way, extact, h2, reducing loss, automated decision, deliveries, packages, future t-shirt owner, business, Linhda, box, day, concept, investment, cognitive APIs, customer service, Amazon Prime customers, fairly private enclosed spots, discretion, savings, preventative loss, relevant groups, things, major issue, neighborhoods, basic computer vision approaches, form of validation of decision, vehicles present, people, supplier, error, doubt, T-Shirts, Deep learning, urban setting, carriers, replacement costs, challenge, high frequency, inconvience, annoyance, occasions, recent order, regard, solid professional, right location, era, sense, short experience, Googled, door, circumstances, mention, time, light, sender, task, consumers, resentment, planning

### Machine Learning and Satellite Imagery Maps Poverty in Africa
*Blog post*: [dev.dataskeptic.com/news/ml-and-satellite-imagery-maps-poverty.md](dev.dataskeptic.com/news/ml-and-satellite-imagery-maps-poverty.md)

*Phrases*: No results returned

### Trying The Microsoft Computer Vision Api
*Blog post*: [dev.dataskeptic.com/tools-and-techniques/2017/trying-the-microsoft-computer-vision-api.ipynb](dev.dataskeptic.com/tools-and-techniques/2017/trying-the-microsoft-computer-vision-api.ipynb)

*Phrases*: No results returned

### Causal Impact
*Blog post*: [dev.dataskeptic.com/transcripts/2016/causal-impact.md](dev.dataskeptic.com/transcripts/2016/causal-impact.md)

*Phrases*: No results returned

### The Police Data Initiative and the Data Driven Justice Initiative
*Blog post*: [dev.dataskeptic.com/episodes/2017/the-police-data-and-data-driven-justice-initiatives.md](dev.dataskeptic.com/episodes/2017/the-police-data-and-data-driven-justice-initiatives.md)

*Phrases*: Data Driven Justice Initiative, Data-Driven Justice Initiative, White House Police Data Initiative, Chief Data Scientist, open data initiatives, Safety Data Portal, href, White House Office of Science, state governments use data-driven strategies, Kelly Jin, col-xs, Technology Policy, div class, Clarence Wardell III, criminal justice system, col-sm, police agencies, Digital Service team, Analytics Team, Chief Technology Officer, US Digital Services team, interviews, h3, things, current role, policy advisor, right services, City of Boston, low-level offenders, Task, mental illness, Century Policing, mutual service, Citywide Analytics Manager, member, img alt, recommendations, h2, county, Presidential Innovation Fellow, src, community trust, Disrupting Cycle of Incarceration, Department of Energy, Report, transparency, internal accountability, DDJ, episode, row, PDI, topic, Foundation, ul, br

### Appeal to Authority
*Blog post*: [dev.dataskeptic.com/opinions/2017/appeal-to-authority.md](dev.dataskeptic.com/opinions/2017/appeal-to-authority.md)

*Phrases*: authority fallacy, particular journal, authority claims, peer review process, journals of higher, information verse, audience, href, particular source, grok, sort of cargo cult of journals presenting knowledge, David Icke, high quality, particular subject matters, future articles, costs of aquiring new information, complex problem, bunch of, random articles of jargon generated, details, extensive validation, shapeshifting lizard, refined content, benefits of acting, question, general, making  context aware concessions, computational resources, individual datums, reputable sources of knowledge, field of expertise, papers, producers of pseudoscience, outright crankism, convincing arguement possible, lower quality, investment of time, bayesian, skepticism, rational people, conclusions of studies, posteriors, tide, high likelihood of correctness, posterior beliefs, sky, pre-publication, accuracy, Gravitational waves, direct explanation, data, Hillary Clinton, biological constraints, appropriate rhetorical technique, smart scientists, assertions, skeptical of appeal, meritocracy, strength, scandals, mini-episode, interesting situation, best logicians, topic, conversation, site, methods, contents, h2, arXiv, output, forms, arguements, mind, idea, repository, theory, odds, weakness

### Using Git as a CMS
*Blog post*: [dev.dataskeptic.com/meta/2017/using-git-as-a-cms.md](dev.dataskeptic.com/meta/2017/using-git-as-a-cms.md)

*Phrases*: code, blog-post-title, analytical blog post, pull request, guest blog submission, img alt, file share, src, Using Git, CMS, useful thing, writer, REPL nature, git metaphor, foundation, single file, using Jupyter, history, source files, place, Jupyter notebooks, cottage industry of fledgling projects, guest bloggers, content management system, data science, typical branching strategies, PRs, relevant files, h2, machines, programatically, needs, shot, frictionless publication, rm, external images, Wordpress, blind submissions, fork, special cases, coding environments, href, open source, size, sketch, knitr, output, interactive plots, headache, additional files, sense, large CSV, nit-picks, analysis, powerful tools, work, multi-day affair, short message, state, advanced features, list, available solutions, life, comment, directory, relative paths, pipeline, h3, kernel, backup, good solution, issues, memory, run, steps, commits, repository, results, instructions, topic, Latex, figures, period, touch

