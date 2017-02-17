## The Limits of Deep Learning

The last few years have brought breathtaking breakthroughs in image, video, and audio recognition using techniques we broadly label as deep learning.  The most optimistic of people will tell you that true general artificial intelligence will inevitably occur when we can finally build and train a network of comperable size to the human brain.  My own thoughts on that conjecture need to be confined to the "opinions" section of this blog.  At least, until my arguments are a bit more rigorous.

But if we focus on the current state of available hardware, are there limits to what deep learning can do?

I'd like to discuss one concept I believe is formally "off limits" for the network to learn, and why I think so.

I believe no deep learning approach will achieve human level accuracy classifying music by genre from the audio data alone (i.e. no external features or metadata provided).

Can a deep learning approach do a fairly good job recognizing the music style being played in an arbitrary song?  Absolutely.  The reason we label some music jazz and other music punk rock is because they are observably different styles of music.  They follow different rules of composition.  They favor different choices of performance and technique.  They exclude certain musical attempts from being considered part of the genre because its too different from the abstract canonical idea of the genre.

Its entirely plausible for deep learning to recognize instrumentation, translate sound to sheet music, extract rhythm, interpret lyrics, detect chord progressions, and develop feature representations for a large number of novel aspects of music.  The presence of a a distorted lead guitar playing fast arpedgios over a driving double bass beat in a bizarre time signature can quickly be identified as a metal song.  The inclusion of a tuba and accordian playing well established chord progressions and rhythms might quickly be labeled as polka.

But what happens when Eminem uses a polka song for the basis of one of his creations?  Do we say it's polka or hip-hop?  Is it both?

Speaking of polka, how would the neural network classify the works of Wierd Al Yankovic?  What about the larger body of music broadly described as "funny music" including cover songs re-written with science fiction lyrics.  I'm told this is called fark.  My ears can identify fark music by the presence of lyrics pertaining to star trek, but I do so by leveraging my understanding of culture.  I might mistakenly label such a song as "indie rock" if the lyrics were in another language.

A great deal of external knowledge is necessary to precisely define the genre of music a song belongs to.  There's also a large amount of variance.  My ears can discriminate between the various epocs of ska which we are sometimes labelled old school, 2tone, and 3rd wave.  Many listeners might mistakenly label ska music as reggae (a derivative of ska).  Clearly, humans are going to be limited by their familiarity with certain genres.  We're also going to have disagreements about certain taxonomical classifications, but I'm sure we could find that human perception has some upper bound of accuracy on this task.

Whatever upper bound is achieve, I claim, will dominate the success rate of deep learning approaches, unless they've overfit the problem.  We bring a great deal of cultural information to the table when humans sit to classify music.  Deep learnings by optimizing towards intermediary abstract representations of the input data.  Some of the nodes in a neural network are going to fire strongly at the presence of minor seventh chords.  Later layers of the network will rely on these m7 nodes, and others, to reliably label music as jazz.  However, they're not going to have any way of representing external cultural clues that are not contained in the information content of the music itself.

Human listeners can bring that external data to the problem in a manner somewhat akin to transfer learning.  I imagine at some point we'll start seeing bayesian methods and pre-training starting points as successful tools for tackling a challenge like this.  Additionally, if its true that more general artificial intelligence will emerge when enough hardware is available, then we must simultaneously acknowledge that this massive infrastructure will require massive training data, just as we humans have from the moment of birth, to build up cultural knowledge that helps to shape problems we ask the models to tackle.
