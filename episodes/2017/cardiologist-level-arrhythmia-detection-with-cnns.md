## Cardiologist Level Arrhythmia Detection with CNNs

Our guest Pranav Rajpurkar and his co-authors recently published [Cardiologist-Level Arrhythmia Detection with Convolutional Neural Networks](https://arxiv.org/pdf/1707.01836.pdf), a paper in which they demonstrate the use of Convolutional Neural Networks which outperform board certified cardiologists in detecting a wide range of heart arrhythmias from ECG data. In this episode, Pranav, a graduate student in Stanford's Machine Learning Group, discusses the methods applied in the study and how this automated approach could prove valuable in everyday medical treatment and revolutionize medicine.

Some arrhythmias may result in serious health complications including sudden cardiac arrest, but an intermittent signal can be difficult to detect. While patients with abnormal heartbeats can wear an ECG monitor for several weeks, a doctor might still find it difficult to distinguish between irregularities that may be benign and ones that could require treatment.

To tackle these detections, Pranav, a graduate student in Stanford's Machine Learning Group and his team developed and trained a deep-learning algorithm to classify twelve different types of irregular heartbeats (arrhythmias) in ECG data. The Stanford researchers partnered with [iRhythm Technologies](http://irhythmtech.com/), a company that makes portable ECG devices, for the study. The models they developed were inspired by models that have worked well in image classification.

The team collected ECG data from iRhythm’s Zio Patch, a single-lead, noninvasive and continuous monitoring device. For the training set, 30-second clips from roughly 30,000 unique patients with different forms of arrhythmia were individually annotated by a clinical ECG expert. Working with these annotated clips from iRhythm, Pranav and his research team were able to develop and train a 34-layer convolutional neural network (CNN) to detect arrhythmias in arbitrary length ECG time-series.

They then compared their model's performance to a committee of cardiologists on 336 undiagnosed records from 328 unique patients to test the accuracy of their algorithm. For the test set, three board-certified cardiologists formed a panel to reach a consensus about any arrhythmia present in the recordings, as a way to provide ground-truth annotation. There were three committees responsible for different splits of the test set. Additionally, six individual annotations from cardiologists outside the committees were collected for each ECG record in the test set. The researchers then compared the level of agreement of the algorithm of the three-person committee's opinion with the combined agreement of six independent cardiologists and found that the algorithm more closely aligned with the group of three cardiologists than an individual cardiologist's reading.

Pranav and his research team were able to show that the automated approach was adept at identifying complex patterns in images and audio. They suggest that the algorithm could especially help people who are at high risk and need to be monitored continuously. A device with the algorithm built into it could then alert emergency services in real-time when potentially deadly heartbeat patterns are detected. 

In the long run, the researchers hope to use this technology in rural areas and parts of the developing world, where many do not have access to cardiologists.

<div class="row">
        <div class="col-xs-12 col-sm-3">
                <img alt="Pranav Rajpurkar" src="src-cardiologist-level-arrhythmia-detection-with-cnns/pranav-rajpurkar.jpg" />
                <br/>
                <p><i>Pranav Rajpurkar</i></p>
        </div>
        <div class="col-xs-12 col-sm-9">
		Pranav Rajpurkar received his B.S. degree in computer science from Stanford University in 2015. Currently, he is a PhD candidate in Stanford’s Machine Learning Group. His research focuses on developing machine learning algorithms and applying AI solutions to high-impact problems.
        </div>
</div>

