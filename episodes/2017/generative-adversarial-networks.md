## Generative Adversarial Networks

GANs are an unsupervised learning method involving two neural networks iteratively competing.  The discriminator is a typical learning system.  It attempts to develop the ability to recognize members of a certain class, such as all photos which have birds in them.  The generator attempts to create false examples which the discriminator incorrectly classifies.  In successive training rounds the networks examine each and play a mini-max game of trying to harm the performance of the other.

In addition to being a useful way of training networks in the absence of a large body of labeled data, there are additional benefits.  The discriminator may end up learning more about edge cases than it otherwise would given typical examples.  Also, the generator's false images can be novel and interesting on their own.

The concept was first introduced in the paper [Generative Adversarial Networks](https://arxiv.org/abs/1406.2661).
