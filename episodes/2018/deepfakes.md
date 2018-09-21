## DeepFakes

Digital videos can be described as sequences of still images and associated audio.  Audio is easy to fake.  What about video?

A video can easily be broken down into a sequence of still images replayed rapidly in sequence.  In this context, videos are simply very high dimensional sequences of observations, ripe for input into a machine learning algorithm.

The availability of commodity hardware, clever algorithms, and well designed software to implement those algorithms at scale make it possible to do machine learning on video, but to what end?  There are many answers, one interesting approach being the technology called "DeepFakes".

The Deep of Deepfakes refers to Deep Learning, and the fake refers to the function of the software - to take a real video of a human being and digitally alter their face to match someone else's face.  Here are two examples:

* [Barack Obama via Jordan Peele](https://www.youtube.com/watch?v=cQ54GDm1eL0)

* [The versatility of Nick Cage](https://www.youtube.com/watch?v=BU9YAHigNx8)

This software produces curiously convincing fake videos.  Yet, there's something slightly off about them.  Surely machine learning can be used to determine real from fake... right?  Siwei Lyu and his collaborators certainly thought so and demonstrated this idea by identifying a novel, detectable feature which was commonly missing from videos produced by the Deep Fakes software.

In this episode, we discuss this use case for deep learning, detecting fake videos, and the threat of fake videos in the future.