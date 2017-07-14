# Estimating Sheep Pain with Facial Recognition

Animals can't tell us when they're experiencing pain, so we have to rely on other cues to help treat their discomfort. But it is often difficult to tell how much an animal is suffering. The sheep, for instance, is the most inscrutable of animals. However, scientists have figured out a way to understand sheep facial expressions using artificial intelligence.

On this week's episode, Dr. Marwa Mahmoud from the University of Cambridge joins us to discuss her recent study, "[Estimating Sheep Pain Level Using Facial Action Unit Detection](http://www.cl.cam.ac.uk/~pr10/publications/fg17.pdf)." Marwa and her colleague's at Cambridge's Computer Laboratory developed an automated system using machine learning algorithms to detect and assess when a sheep is in pain. We discuss some details of her work, how she became interested in studying sheep facial expression to measure pain, and her future goals for this project.

For sheep, severe pain is commonly associated with diseases such as mastitis or foot rot, which causes the foot to rot and is extremely painful. Sheep within large flocks are often prone to both of these diseases, and early detection would lead to faster treatment and pain reduction. However, the sheep as prey species have adapted to hide the visible signs of pain or sickness to prevent being targeted by predators. Hence, it can be challenging for their owners to get insight into the sheep's emotional state. An automated system to detect pain could be a handy tool for farmers, who could take the affected sheep to receive a diagnosis and early treatment from their veterinarian. 

The newly developed system identifies different parts of a sheep’s face, evaluating the face with a standardized measuring tool created by veterinary scientists to recognize and measure pain. The [Sheep Pain Facial Expression Scale (SPFES)](http://www.sciencedirect.com/science/article/pii/S0168159116000101) was developed in 2016 by Dr. Krista McLennan, a former postdoc at the University of Cambridge, to gauge a sheep’s pain levels by looking its facial expressions. The scale defines five major changes that occur when a sheep is in pain: their cheek muscles tighten, eyes are narrower, ears fold forwards, lips pull down and back, and their nostrils take on a "V" shape. The SPFES then scores the extent of each changed characteristic on a scale of 1 to 10 to measure the severity of pain. Although the SPFES has been reported to show high accuracy, training people to correctly use the tool can be time-consuming, and reliance on individual perceptions can change case to case, resulting in inconsistent scores. 

A dataset consisting of roughly 500 photographs of sheep undergoing treatment for pain-related conditions was used to train the model, by labeling each image with five features: nose, left ear, right ear, left eye, right eye. Within the images, they then classified characteristics of the ears, nose, and eyes into nine facial "action units" (AUs), which were assigned a pain level. (AUs are further described in the episode, so tune in!)Early test results showed that it is capable of estimating pain levels with about 80% degree of accuracy, which means that the system is learning. However, in order to make the system more robust and applicable to other animals, they would need much larger datasets. 

If you're able to be in Minneapolis, MN on August 23rd or 24th, consider attending Farcon.  Get your tickets today via [https://farcon2017.eventbrite.com](https://farcon2017.eventbrite.com).

<div class="row">
        <div class="col-xs-12 col-sm-3">
                <img alt="Marwa Mahmoud" src="src-estimating-sheep-pain-with-facial-recognition/marwa-mahmoud.jpg" />
                <br/>
                <p><i>Marwa Mahmoud</i></p>
        </div>
        <div class="col-xs-12 col-sm-9">
		Marwa Mahmoud received her Ph.D. in Computer Science at the University of Cambridge, England in 2015. She is currently a Postdoctoral Researcher in the Graphics and Interaction Group at the University of Cambridge Computer Laboratory, where she studies emotional inference from gestures and expressions. Marwa's research interests lie in the field of affective computing, social signal processing, and automating machine understanding of Emotional Body Language. Aspects of her research draw on computer vision, machine learning, human-computer interaction, and psychology. Marwa holds a B.S. and an M.S. in Computer Science from the American University in Cairo, Egypt.
        </div>
</div>

