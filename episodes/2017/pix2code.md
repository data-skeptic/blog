## pix2code
In this episode,  [Tony Beltramelli](https://tonybeltramelli.com/) of [UIzard Technologies](https://uizard.io/) joins our host, Kyle Polich, to talk about the ideas behind his latest app that can transform graphic design into functioning code, as well as his previous work on spying with wearables.

Tony and his team at UIzard Technologies recently developed [pix2code](https://arxiv.org/pdf/1705.07962.pdf), which leverages deep learning to transform graphic user interface screenshots into lines of code. [pix2code](https://github.com/tonybeltramelli/pix2code) takes a clever approach based on Convolutional and Recurrent Neural Networks that allows the generation of computer code from a single GUI screenshot as input. This new method is an achievement because mapping a structured image to a language description is a very difficult task.

All it needs is a single image of a design for a graphic user interface (GUI) to work. Once the neural network is trained to recognize the image, it begins to produce the code that creates the graphical user interface. Moreover, the model can generate source code for a range of different platforms --iOS, Android, HTML, and so on-- from a single input image with over 77 percent accuracy. The trick to being multilingual is to use a special Domain Specific Language (DSL) that describes the UI and then is compiled to the specific language. 

Below is an overview of the architecture of pix2code model. The visual component is handled by a convolutional neural network and the language part is handled by a Long Short Term Memory (i.e. a feedback network). 

<img src="https://user-images.githubusercontent.com/17261080/27221124-c9cadcc6-5287-11e7-9d38-c4234af92912.png" width=800 />

In order to train the neural network, Tony’s team at Ulzard Technologies needed to overcome three main problems. The first being computer vision, as computers won’t automatically understand the context and cannot instinctively identify the objects present, as well as their characteristics. Secondly, there is the language problem-- teaching the network to understand text so it could create the correct samples is a difficult task. Finally, the network had to be trained to understand the connections between code, text and corresponding images. In other words, the network needs to connect all three while generating codes.

According to Tony, Generative Adversarial Networks (GANs) could potentially be used in the future to improve and update pix2code. Previously, GANs have shown promising accuracy when generating sequences and images. However, applying GANs to the problem of generating computer code from an input image is a relatively unexplored research area. For this reason, a major obstacle is the need for a lot of training data to train deep neural networks to recognize unseen samples.

Here is a video demo of how pix2code works: https://www.youtube.com/watch?v=pqKeXkhFA3I&feature=youtu.be

### deep spying
Also, in this episode, Tony talks about his Master's thesis, titled [Deep-Spying: Spying using Smartwatch and Deep Learning](https://arxiv.org/pdf/1512.05616.pdf). During his graduate studies at the IT University of Copenhagen, Tony collected movement data from a [Sony SmartWatch 3](https://www.sonymobile.com/us/products/smart-products/smartwatch-3-swr50/) and was able to accurately discern what was being typed on an external keypad. 

The idea behind what Tony has coined "deep-spying" is that a hacker with access to the sensors (e.g. accelerometer and gyroscope) on a piece of wearable tech could use a malicious app to record the tiny motions of the wrist, process the data, and figure out which keys were entered. His study expanded on [previous work](https://www.ece.illinois.edu/newsroom/article/11762) done by Romit Roy Choudhury, an Associate Professor at the University of Illinois Urbana-Champaign, who showed how wearable devices, such as a Samsung Gear Live smartwatch, can be vulnerable to hackers.

Using a deep learning algorithm, Recurrent Neural Network - Long Short-Term Memory (RNN-LSTM), Tony trained an artificial neural network to recognize when specific buttons on a keypad were being pressed, based on a smartwatch's motion sensor. Even without the training, the Deep-Spying model could infer keystrokes with reasonable accuracy. The source code is available at [GitHub](https://github.com/tonybeltramelli/Deep-Spying).

Here is a video demonstrating how Deep-Spying operates, by taking gyroscope and accelerometer data from a Sony SmartWatch 3: https://www.youtube.com/watch?v=ZBwSfvnoq5U


<div class="row">
        <div class="col-xs-12 col-sm-3">
                <img alt="Tony Beltramelli" src="src-pix2code/tony-beltramelli.jpg" />
                <br/>
                <p><i>Tony Beltramelli</i></p>
        </div>
        <div class="col-xs-12 col-sm-9">
		Tony Beltramelli is the founder and CEO of UIzard Technologies. He specialized in machine learning during his graduate studies at the IT University of Copenhagen and ETH Zurich. His research work on the application of deep learning was featured in international media such as WIRED, Forbes, The Huffington Post, The Next Web, Gizmodo and more.
        </div>
</div>
