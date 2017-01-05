## Music21

**INTRO VOICE-OVER**: Data Skeptic features interviews with experts on topics related to data science, all through the eye of scientific skepticism. 

**Host**: Michael Cuthbert has a PhD in musicology from Harvard and is presently associate professor of music at MIT. His scholarship and research explores medieval music as well as minimalism. In addition to his lectures and writing on music, he is also the primary investigator of the Music21 project, a Python library for flexible, computer-aided musicology analysis.

Mike, welcome to Data Skeptic.

**Mike**: Thank you! It's great to be here.

**Host**: I've been looking forward to this, because I've started playing around with Music21, and I'm excited to hear your own perspective and get some further details. Maybe we could start there. What exactly is Music21?

**Mike**: Music21 is a library of modules for being able to represent music and manipulate it. It's primarily focused on symbolic music - things like music theory ideas, chords, keys, scales and rhythms - that can be precisely represented in a computational framework. Then, we can use this to analyze large quantities of music or make comparisons across different musical genres or times and places.

The Music21 motto is ìListen Faster,î so it allows you to do the types of analytical procedures that people who are really interested music, professional musicologists, do all the time, but between a thousand and a million times faster than we can do it by hand.

**Host**: What's an example of one of those analyses the musicologists might be interested in?

**Mike**: One of the things that we looked at is how the baselines of pop songs change over time. There used to be a period where all the baselines, you know, classical music, tended to have a lot of jumping around that we call fourths and fifths. *[Rhythm Playing]* And then we have a period with a lot of moving down by thirds *[Rhythm Playing]*, and now we're in a period of a lot of moving up by thirds or things like that. *[Rhythm playing]*.

So now can we see these evolutions over time where we can pick out a few representative pieces and do it by hand. But with Music21, we can actually look at distribution of interval uses by a year, by decade or over a long period of time.

**Host**: What are some of the insights that have come out from that? Is music evolving faster than it did in the classical period, or are we repeating the same things we've seen before? What do we learn from some of those analyses?

**Mike**: I think it's unfair to talk about whether evolution has been faster or slower in any given period, because we tend to think of music in the past as not evolving as fast and being more static, because the things that we are most interested in changing aren't happening at that time, and things that we can't detect, like, you know, the vocal timbre, the color of the music. What we can find out from this is what qualities of music make it sound of a particular time.

The other thing that we can learn from this is what aspects of our music theory and education, what we're teaching people, aren't nearly as relevant as they once were. For instance, we're still teaching in all these music history classes that composers and songwriters avoid the parallel fifth. *[Rhythm playing.]*

And that's basically gone in the data sets that we can see. This is a rule that at some point was very helpful to people and that people today aren't finding helpful.

**Host**: When I think about music - maybe this is my own bias - at least modern music, I can label it by decade. That's what music was like in the ë80s and in the ë70s, but then I have these broad brush strokes of, you know, classical Baroque or Romantic periods, those are things that I see as static. If I were to really spend the time investing in looking at something like, let's say, Medieval music, would I see just as much variation over a ten-year period as I perceive in my own time period?

**Mike**: Even for a specialist like me, it's hard for me to really hear, well, *that's definitely from 1370 and not from 1360*. They told me they aren't doing that in 1373, in part because we don't have enough labeled data for even what were called the ground truths. It's hard for me even as a specialist in this music to get rid of all the biases that I have that make it hard for me to hear the subtle variations. But for Music21, and [a machine learning program](https://www.washingtonpost.com/news/innovations/wp/2016/06/06/googles-computers-are-creating-songs-making-music-may-never-be-the-same/), that's not hard. It doesn't come in with any of the biases about how music from the 1960s sounds quite different from 1970, or even 1360 and 1370.

I've been able to use Music21 to point out big problems, and some the dating of pieces and some of the things where we thought, ìWell, this absolutely sounds German - there's no way that a French composer was writing like that.î Well, actually, the computer systems know this piece has a 90% probability of clustering with the other French pieces and that's been really revelatory for me and my colleagues.

**Host**: So, I'm familiar with MIDI and I'll take for granted that listeners kind of know generally what that is - it's a digital format for the records given to an instrument, different from, like, MP3, that's recording the sound waves. MIDI is recording sort of the events that describe a piece of music. I have a MIDI library and I'm familiar with MIDI Python. I could use that to read all those events and presumably this music analysis. Why do I need Music21 if I know MIDI?

**Mike**: If you know MIDI, you'll definitely be able to work with any sort of programming package or any library to come up with the count of how many notes are above the treble clef staff, or what's the most commonly used rhythm. You don't need Music21 for that, and I'd encourage people that, if you want to go forward in this, use whatever is most beneficial there.

But Music21 has a lot of the algorithms that other researchers have developed for things such as analyzing keys and key changes or figuring out of all the notes that you are hearing at that point. What chord is it, and how does that chord function in this larger context, and you don't need to reinvent the wheel if you load your MIDI file into Music21 or collection of MIDI files.

In addition, there's a lot of richer data formats than MIDI, such as music XML, which encodes a lot of information from the score. This thing that sounds loud - is it forte or fortissimo? Loud or very loud in the score? Music21 can read all that information and work with it in a machine learning context as well.

**Host**: So if I want to ask myself a question, like, you know, ìWhat is Bache's favorite chord?î I can see whether it will be a daunting task if I just want to do it with MIDI. If I ask you to read some source code on error, that might qualify as the most boring podcast ever, but at the high level, could you walk me through what it would take in Music21 to write some code to answer that question? What's Bache's favorite chord?

**Mike**: So the first thing that I would do is we would load up in a foreign loop. Let's load each piece, because they are all independent of each other, and then we are going to go through and do something called **salami** slicing - that is to say, every single time that any musical event changes, we will call it a new vertical sonority, or chord. So, for instance, if I play a chord like this: *[Rhythm Playing in Background]*.

At the moment when there were two notes changed, we will call that two vertical sonorities, and then Music21 has some analysis packages that can reduce the number of chords of vocabulary reduction to be able to say, well, a lot of the things that, if you look at the sloppy slice, the thinnest slices of music look immediately like chord changes but don't actually function that way. They are a melody or some kind of passing tone.

So, then, with Music21, we can reduce the size of each piece from over a hundred melodic elements into maybe 10 chords per minute, and from there we can reduce this thing that looks like a chord and is actually, or can be thought of, as a restatement of another chord. So these notes, C, E, G, spread widely apart are actually the same as C, E, and G close together. We will reduce the number of records in that way so C, E, G written with the C and the E and the G written very widely spaced could be thought of as essentially the same chord as C, E, G written closely, or maybe even C and E without G. These are things that music theorists do all the time unconsciously or through training.

From there, it would be easy to go through and transpose all the chords so we might say, well, C, E and G has a very different function in the key of C than it does in the key of D minor, so we could then rewrite each of these chords not as letter names, but as a function so that one is the tonic and one key or the other is the sub-tonic, and the other technical things like that.

From there, it will be really easy to just put it into a counter object and put it all out and say, oh, I don't know, probably it's going to be G Major that's Bache's favorite chord. You know these are the things that come up, and then the fun begins, because as a musicologist, I want to know why. I want to suddenly have this data that has taken me years to get before.

And I can carve it in probably half an hour or an hour, and then I can start asking, well, you know, why is that his favorite chord? Why is it different from **Bantaverni's** favorite chord, who composed at the beginning of the Baroque era? With Bache dying in 1750, and **Monteverdi** living around the 1600s, and in this 150-year period that we tend to just throw together as the Baroque, what changed and how is that interesting?

**Host**: We started out at four loops where we load all the Bache pieces. Can Music21 help me find those pieces?

**Mike**: Music21 doesn't have that built-in capability, but I've been working with another project called Elvis, the [Electronic Locator Vertical Intervals Sonorities](http://elvisproject.ca/research/intro-poster.pdf), another one of these cases where I think the acronym preceded the expansion. The Elvis project has a large online database of all machine-readable symbolic formats that it was able to find on the Internet. MIDI and music XML, ABC, I believe, and other formats - they've all been collected there. There are other large repositories of huge numbers and MIDI files from the internet. I believe a Cornell researcher just acquired over 1 million MIDI files that are right for this kind of large-scale symbolic analysis.

**Host**: Wow, so it seems like a really pretty rich data set to work on?

**Mike**: Absolutely.

**Host**: So I'm familiar with different numbers of music formats. You mentioned MIDI and you mentioned music XML. I'm also a fan of a project called Lilypond. Can Music21 interact with all of these interchangeably?

**Mike**: Music21 can interact with music XML and MIDI, and there's some other formats - Capella, Noteworthy, Composer ABC - which is a large repository of tunes for the *Lord of the Rings* online project, and all other folks music. Music21 can read in all these formats and it can also produce LilyPond format, which is a text-based format that produces absolutely beautiful musical scores. It can't actually read in LilyPond except for the most basic files, because LilyPond files are actually a form of scheme source code macros, and so I would need an entire scheme interpreter to read everything that can possibly be there.

One of the other formats that I'm really proud Music21 works with on the output side is Braille Music Vode and Braille Music Notation, which I hope will be able to open up a world of scores to a much larger audience of people with sight difficulties who will be able to see exactly what this music looks like on paper.

**Host**: Interesting. I'm unfamiliar with that. If I see a printed page of it, would it look like anything sheet music?

**Mike**: It would look to us just like text braille, but for the most part, each cell encodes both a pitch name and duration. There are various ways of encoding chords that are very different from how sheet music encodes it, and it doesn't waste space on needing the vertical component and the horizontal component together to tell us the durations and the pitch, and so it actually in some ways is much more compact than conventional sheet music notation. There is always a chance that, if we were starting over today, we might use something much closer to how a braille encodes.

**Host**: How about the visualization side? Of course, when I have all my analysis, is there going to be a point when I perhaps detect a funny chord or something like that? I'd like to see a printed, you know, five-staff version of it. Can Music21 help me see music, as well?

**Mike**: Oh, absolutely. Since it's a computer-based project, one of the other things we can do is ask to tweak parameters. Of course, we can generate scores in real-time, and it's all a process where you want a very high-quality score that you're going to get published, so we can send it out to LilyPond or New Score Finale or some other music notation software packages that take a little bit of time to render the score, or through something that looks pretty good and is incredibly fast. We can send it out through a JavaScript library and render it in the browser, so there's a lot of things we can do to get immediate feedback in score notation.

If you don't read score, we can also generate plots, for instance, for piano, wall-style where the horizontal component is time and vertical is completely, just, what you know is being played on the piano. You can see each note. There's a lot of **YouTube** visualizations at this time, and you know I read music notation pretty fluently, but every once in a while I'll pull out a piano plot, mainly to demonstrate something to somebody who doesn't read music and all of a sudden I will see repetition patterns in the music that were never obvious to me before. So a lot of these visualization tools are even used by people who can't read the notation.

**Host**: So, you had mentioned earlier some of the built-in algorithms and processes that are available that Music21 gives a user for free. Could you give us maybe a teaser of what some of those are? About the depth and breadth of stuff that's available?

**Mike**: Well, one of the things that my students find really valuable is the ability to take a single melodic line and realize it into a fully realized harmonic package. They find that very valuable because it's generally the things that other teachers are making them do for homework.

Another really useful set of tools that Music21 has is a large collection of feature extractors. These are little tools that change some part of the musical score into a numeric representation. A guy named Cory McKay developed about 100 of them, and we've added about 50 more that can be applied to MIDI music and XML files and really be able to look at the rhythmic variance between one section and another, and how smoothly do the changes happen, and so on and so forth. And from these feature extractors, we are able to use off-the-shelf packages like Orange to really see how pieces of music relate one to another.

**Host**: When you mentioned feature extractor, and you've already mentioned machine learning previously, my head's going directly there. I can do some interesting classification and regression problems, given these data sets and tools. Do you have any favorite examples of work where other people, perhaps yourself, have utilized Music21 to do along those lines?

**Mike**: Yeah. I had a graduate student who thought it's really fascinating, trying to figure out where these classical pieces that tend to have core movements got there - fast, slow, dance and finale. This student used Music21 to figure out how small of an excerpt of a piece we need to have in order to know exactly which movement are we in, or even whether we can extend these to where in a piece are we. Sometimes we walk into a concert late or walk into friend's house and we turn on the radio and the piece is already in progress and we might not know the piece at all, like the computer, who has been trained on the score, and yet we have a really good sense of, ìWe should be nearing the end, it's too bad I missed it.î

Or, ìOh, good, this is near the beginning.î How we know that, and how good a computer is with it, I thought, was a really fascinating project.

**Host**: Was Music21 started out of just the sheer obviousness of, like, *Hey, there should be a cool library for working on music projects*, or did it arise out of some particular need you had to solve a problem? Or you are working independently?

**Mike**: Actually a little bit of both. I was working a lot on small fragments of medieval music at that point and, you know, we didn't save that much from the 15 century to the 14th century, so a lot what survived was little ripped-off stubs tucked into the binding of another book or something like that. And quite often, we have six notes from one staff and four notes from the next staff or three notes here and there, and I just felt like, you know, we should be able to identify these pieces. That should be enough of a fingerprint for me to be able to understand where this comes from.

And so I did what anybody else would have done. I Googled to see if there was an analysis package out there, and there was a very good one called Humdrum, which was developed in the late ë80s and early ë90s by David Huron at Ohio State University. But it was definitely from a different era - it was a series of cell-scripts where everything was piped together and there were no objects to represent various parts of the musical score.

And I thought this would be very difficult, because I also have to encode everything in Humdrum format and so I thought, well, I'm just not Googling well enough, so I kept looking around. I thought this was, as you said, it's a very obvious idea and I thought somebody else had worked on this.

And it had been out there and I just couldn't find it. I think that was around 2004, and I waited a year and couldn't solve my problem and I did a very thorough web search again and nothing came up, so finally, around 2006 I was teaching at MIT. My students wanted to work on projects like this and I said, aw, heck, I'll just go ahead and write it myself. And about I guess 10 years later, I fully understand why nobody else did it, because it ended up being a lot of work. There's a lot of tricky corner cases in almost everything in music, and that's why I think at this point there's only one project like Music21.

**Host**: Yeah, definitely. There's a stereotype that I know is wrong, but it's useful for conversation. We have sort of left- and right-brained people. If I stick to my - I guess it's right brain - more analytical side, Music21 is obviously the tool I want to pick up, and it was very intuitive for me to learn, but when I think about that stereotype of the left-brained person, which perhaps is where a lot of musicologists lie, it bears with that. Whether it's right or not, the stereotype of someone who is less technical or doesn't want things as rigidly structured are probably not computer programmers. But the intersection of musicologist and programmers is rather small. How well have you found that community has adopted to taking on this technology, maybe having to learn the code just to use Music21?

**Mike**: I will say that when I use Music21, it ends up confirming something that we've long thought in music history: everybody's very happy to have new technical tool in the toolkit. But when Music21 ends up refuting something that we've always been thinking, you know, then the difference between the left brain - I don't want to have a computer tell me the right way to analyze things - versus, you know, the more technical side, then it really does come out.

But there are more and more people who are going into liberal arts fields like musicology, especially like music theory, who are interested in programming and who know that this is important. Even if they don't want to personally do it themselves, they are interested in learning the basics of a toolkit like this to at least be able to do something like a note counting routine or a search for a particular figure.

So there's been quite a bit of adaptation and at least enthusiasm in the field, but as we all know who's programming and who's working with the data sets, it's a lot of work to get to the level of fluency with programming language to be able to really take an idea for something you would like to do or something you'd like to search for a proof and actually execute it.

Because of that, one of the most important things we've done in Music21 is really try to make it so that the naming objects are very close to what musicologist and musicians would think they should be, and things like the first measure of a piece is measure one and not measure zero with zero index, and all these little things to try to make it so that we can bridge the gap between the left brain and the right brain people so that musicologists can call up his technical programmer friend and she can write the code. You can make it possible for two people to work together with a shared vocabulary, and that's been very important for me.

**Host**: So in doing a lot of my research for the interview, I came across something I didn't quite understand and I thought I could ask you. There was some mention of the fact that we've well-studied melody and harmony. We understand these ideas, but we don't understand counterpoint as well. Could you tell me what counterpoint is, and why would it be the case that we don't have as good an understanding of it as we do melody and harmony?

**Mike**: Melody, as you know *[Rhythm Playing in Background]*, is something like that. And harmony - we're thinking of something along the musical score - that's really oriented on the horizontal axis. Then harmony would be a succession of chords, something like, you know: *[Rhythm]*. Counterpoint is the intersection of the horizontal and vertical, so while we are moving from chord to chord on an instrument like a piano or a guitar, or in an orchestra, the chord isn't moving but the individual notes within the chord are moving to other notes in the next chord.

How one note moves in one chord to its position in the next chord we call ìvoice leading,î and the interaction of all the notes in one chord that moves to all their new configurations in the next chord is counterpoint. In Latin: *usque ad punctum*, or point against point. What's challenging about counterpoint from computational standpoint is that there's lots of ways that we can think of analyzing one-dimensional data. So a melody, we can essentially put it in a list or an array or something of that sort. And a chord we can do the same, except that our array is oriented to 90∞ in the other direction.

But with counterpoint, we're really thinking of well, how do we look at the simultaneous movement of one verticality to the next and the way the composers solve the problem of, well, I want every note within a chord - especially in something like a choral piece - I want every note within a chord to move to the next chord in such a way that it has a beautiful melodic line at the same time. I want all of the chords to move together in a progression that has a beautiful harmony, so the melody and harmony have to be solved at the same time. It's a little bit like Rubik's cube solving. You know, you think you get one face done and oh, no, you've screwed up all the other faces.

The techniques for being able to analyze counterpoint required new algorithms. They are not especially difficult algorithms compared to some of the things the other data scientists that you've brought onto your podcast are doing, but they are new and they need to be thought of in musically cogent ways.

**Host**: So I know music has changed quite a bit stylistically, like we hear a lot of seventh chords today and there was a time when that was considered discordant and not a proper part of music. I know your research goes into Medieval music.

How does Medieval Music compare to Modern music? I mean, that's a general term, and it may be too open-ended of a question. Obviously it's different, as it has certain properties, but does it follow the same rules and structure, or maybe it just has to be parameterized differently than modern music? Or has everything changed and evolved?

**Mike**: Well, a lot of things have changed. When we're talking about medieval music, we're really talking about an era maybe from 500 to 1500 or 1400, so it's about three times as long as everything that's come after it that we listen to. So I can't really say about, you know, one thing that has happened since then, but I will say in the periods I mostly work on, toward the end of the Middle Ages - the 1200s 1300s 1400s - we are seeing a change going from the two consummate sonorities or the fourth. So I'll count one, two, three, four and the fifth, to the two, and the fifth, and the third and the fifth together. What we call simply a triad or just a chord.

And the chord began as an interesting dissident moment that you could put in the middle of a phrase, sort of like an ellipse, to say more is going to come. Because obviously we can't end on a sound like that.

And then, over time, the number of triads, these three-note cords that were being used in a row more and more and more, and I can plot the change in that overtime. Eventually, the triad became part of the stable sonority that didn't need resolution. And the same thing happens in the 1600s and 1700s with, as you mentioned, the seventh chord. *[Rhythm Playing in Background]* Those cords originally had a high amount of tension, and they can only be used in a place where they would be resolved to something more stable, and that's basically true up until the late 19th century with composers like Wagner and Strauss and Debussy, who start to see that as a stable sonority.

But I think really it changes with jazz. A Jazz composer will put in a piece what would be considered unstable sonorities before, *[Music Playing]* and its sounds like that you know. I'm not a very good pianist in general or a jazz pianist, but you know, something like that you can hear, oh, yeah, that's where you put down your gin and tonic or scotch and applaud. And that sounds like an end to us now, and a lot has changed over time and a lot of the time I wish that I could be put into cryogenic freezing and listen to what the music would be like 500 years now. I don't think it's changing. I think, you know, a lot of the best music still to be written is being written today and will be written.

I don't think that, even if I could use the computer to predict what types of things would come next, which some people think that Music21 can be used for - and it's possible - but it's not a question that interests me, because I don't just want to know what are the main trends that are going to happen next, but also how people are going to react. How are people gonna feel? What's the actual piece that's gonna be written with the things that are gonna change the future?

**Host**: I'm curious about the data set you have available to study medieval music. You are noting that some of it's coming through in just fragments of papers pressed between books and things like that. A lot has been lost, I presume. If I want to look at the complete discography of the Beatles, I might have some copyright issues. But I know all the information is there. How much of a struggle is that, to study that time period?

**Mike**: Well, actually, let me answer something that wasn't in the question first. You said lots have been lost. Actually, one of the first papers I did then was very mathematical and is actually showing that a large percentage of medieval music survives. So that one, that's the first thing that caught my colleagues' attention. There is a large percentage - maybe 40, maybe 50% - and maybe even more of the music that I'm studying survived.

We can look at statistical tests for being able to assert that, and so I think that this is the time to do it, because what we have is very representative of what was once written down out there. And one of the ways I know this is that usually these small fragments end up being a piece we already know. So we have a small piece of music. I can't think of the piece that goes with that, so much medieval music's lost - it's probably a new piece.

And once I had the math behind me, I said, well, okay, we are going to find most of these fragments are pieces that we already know, so because most of the pieces were probably the ones that survived, we can build the printed scores that musicologists have been making since the 19th century. Especially since World War II - there's a 24-volume, beautiful green set of books called [Polyphonic Music of the 14th Century](http://www.worldcat.org/title/polyphonic-music-of-the-fourteenth-century/oclc/491470464), and I think it's about 8,000 pages or something like that. I have a project where we entered it all into the computer. There was just no substitute if you want high-quality data for entering.

I thank my collaborator Ana Grau for really organizing this whole project.

So I have that as a data set, so I'm planning on releasing that set as soon as I can get what copyright concerns there are for 14th century music. Once I can, it will be the only data set of every known piece of music written on an entire century that's out there. So that's pretty exciting. We can't do that with every piece of 20th century music. It's just too big too, with too many copyrights, but we can do that with another era.

And some of the things I found were that at least 40 of the pieces that we thought were different pieces were actually the same pieces with new text and maybe a little bit of different decorations and moved up a key to something. There's at least 10 or 20 cases of composers that we thought their most important piece was such a unique piece of genius but actually seems to be copied or plagiarized from somebody else. So that should be pretty exciting, presenting that at the conference coming up in Vancouver. The big [musicology music theory conference](http://www.ams-net.org/vancouver/) in November.

**Host**: Oh, what a treasure. That's a great data set. So it's obvious to me that musicologists would want to use Music21. I of course see the immediate use for someone with some machine learning talent who wants to do some neat projects. Are there any other groups I'm not thinking of who would benefit from leveraging the library?

**Mike**: Definitely composers use it a lot. While I'm a musicologist primarily, I also compose, and so I try to think when I'm designing a new module, how would a composer use this repetition expander module or repetition finder to make something new?

How can we manipulate a particular scale algorithmically? So I'll use that in my analysis to figure out, well, is something happening in this section that's actually just a slight manipulation of the common scale? But a composer can use that in a reverse way to generate all the different permutations of a scale or manipulations that have a particular property and put it into her or his piece. So composers are big users of the system.

**Host**: Oh, very interesting. It makes sense, and so, in terms of getting involved, this is an open-source project. Is there room for contributors?

**Mike**: Absolutely. I would love to have more contributors. It's open-source, and you can find it on Github.

**Host**: Pretty cool. And if we want to get started playing around with it, where's the best place for me to get the ìhello worldî equivalent of Music21?

**Mike**: I think the best thing is just to download the package and then [you'll find docs on my team website](web.MIT.edu/music21). If you want to go directly to the docs, there's a tutorial user's guide. You'll see it starts petering out around chapter 15, but in 15 chapters there are very good examples of what you can do. And, you know, I hope people contribute more.

**Host**: Excellent. And I have links to all that in the show notes for anyone who wants to give it a whirl. Before we go, are there any other things you want to highlight around Music21 that may be interesting use cases? I came across Score Follower for example.

**Mike**: Some of the things that we are trying to do with Music21 and Score Follower is an attempt to automatically reduce a large, complicated score into the most important elements so you can follow along and have it synced with an audio file. That's something I've done with Vladimir Viro of [Peachnote](http://www.peachnote.com/).

Another project I've done with a great young researcher named Mora Church is to use music theory examples embodied in the Music21 library to improve what's called OMR. It's the musical equivalent of optical character recognition. The output for that is very promising, but it's not yet at the level that you can immediately use in any particular project. So we can use music theory to improve the OMR and, you know, maybe a third of the time we can take what was definitely wrong and make it absolutely right with what's written on the page, depending on what the problem is.

Host: Well, Mike, this has been fascinating. Thanks so much for coming on to share some of the story about Music21 and ways people can use it. I hope everyone goes out and checks out the website.

**Mike**: Thank you very much. Its been a pleasure.

**EXIT VOICE-OVER**: For more on this episode, visit [dataskeptic.com](www.dataskeptic.com). If you enjoyed the show, please give us a review on [iTunes](https://itunes.apple.com/us/podcast/data-skeptic/id890348705?mt=2) or [Stitcher](http:\www.stitcher.com\podcast\data-skeptic-podcast\the-data-skeptic-podcast).
