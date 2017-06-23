## Doctor AI

When faced with medical issues, would you want to be seen by a human or a machine? In this episode, Data Skeptic host Kyle Polich interviews guest Edward Choi, co-author of the study titled “Doctor AI: Predicting Clinical Events via Recurrent Neural Network.” Edward presents his team’s efforts in developing a temporal model that can learn from human doctors based on their collective knowledge, i.e. the large amount of Electronic Health Record (EHR) data. 

In the United States, large amounts of Electronic Health Record (EHR) data have been collected over millions of patients over multiple years. EHR data represent the rich longitudinal experiences of physicians and patients, which include information regarding diagnosis, medication prescription and procedures. Although physicians have access to the massive amounts of patient historical data, they neither have the time nor the tools to analyze them all. Yet evidence-based clinical decisions should rely on such information that is specific to the patient and provider needs. By leveraging rich longitudinal EHR data, Edward and his colleagues developed “Doctor AI” --a generic predictive model that covers all medical conditions and medication uses.

Using patient HER data, Edward’s research team developed a successful application of Recurrent Neural Networks (RNN) to predict the diagnosis and medical code that will be issued in the next visit, as well as the time of the next visit. They used RNNs to capture the longitudinal EHR patterns. 

The initialization of the RNN involved using skip-gram embeddings. More specifically, the input data included: a patient’s medical (ICD-9) diagnosis, medications, and procedure codes, which were time-stamped with the patient’s previous visit. (Note: the procedure code from the previous visit was used to predict the next visit’s procedure code) Below is the general architecture of the model. The diagram shows how they applied RNNs to solve the problem of forecasting of next visits’ time and procedure codes assigned for each visit:

https://github.com/GokuMohandas/casual-digressions/blob/master/notes/images/docai/rnn.png

The proposed neural network architecture receives input at each timestamp t<sub>i</sub> as the concatenation of the multi-hot input vector x <sub>i</sub> of the multi-label categories and the duration d<sub>i</sub> since the last event. So, x <sub>i</sub> is fed into the model to output y<sub>i+1</sub> and d<sub>i+1</sub> from the RNN, where y<sub>i+1</sub> are diagnosis and medication classes for the next visit and d<sub>i+1</sub> is the time until the next visit, which is labeled as: d<sub>i+1</sub> = t<sub>i+1</sub> – t<sub>i</sub>

The medical and diagnosis multi-hot input vector is the input, which can be as large as 40, 000. Thus, the input goes through a second layer of embedding to become a lower dimensional vector, which was then passed through RNN (which was implemented with GRU in this particular study). The second input is d<sub>i</sub>, which is the duration since the last visit. They then feed this second input, d<sub>i</sub>, into the network to predict the multi-hot vector for the medication and diagnosis codes of the next visit using a softmax classifier. To predict the period of time until next visit, they use the ReLU activation function. 

https://github.com/GokuMohandas/casual-digressions/blob/master/notes/images/docai/final_layer.png

As mentioned earlier, the multi-hot vectors x<sub>i</sub> of almost 40,000 dimensions were first projected to a lower dimensional space, then put into the GRU. Edward employed two approaches for embedding the medication and diagnosis codes. The first approach (1) was to train the embeddings with the RNN end-to-end. The second approach (2) was to pre-train the medication and diagnosis codes with a skip-gram method use these embeddings as the initialization, then refine the embedding weights for the RNN as they then train the model end-to-end.  The first and second approach were formulated as the following:

https://github.com/GokuMohandas/casual-digressions/blob/master/notes/images/docai/embed.png

where [·, ·] is the concatenation operation used for appending the time duration to the multi-hot vector h<sup>(1)</sup> to make it an input vector to the GRU.

In the end, Edward found that the second option (2) consistently out-performed the first option (1). 

By training with a skip-gram method, the skip-gram method in Word2Vec meant using each word and predicting the context words for before and after. For Doctor AI, they used a particular disease or medication/diagnosis code to predict the previous and future medication/diagnosis codes in order to pre-train and learn embeddings. They used GRU because it performed similar to LSTM but much less complex. Pre-training the medical diagnosis embedding weights (W<sub>emb</sub>) with a skip-gram method consistently out performed random embedding initialization.

Unlike traditional classification models where a single target is of interest, the Doctor AI model can assess the entire history of patients and make continuous and multi-label predictions based longitudinal time stamped EHR data. The primary goal of this study was to use longitudinal patient visit records to predict the physician diagnosis and medication order of
the next visit. The model’s performance was evaluated on real-world EHR data from over 260,000 patients and 14,805 physicians over 8 years. Accordingly, Edward shows that Doctor AI can perform differential diagnosis with similar accuracy to physicians. In this study, Doctor AI achieved up to 79% recall@30, significantly higher than several baselines. 

Conclusion: RNNs can be used to predict future medical events and the timing of these events. They demonstrate the generalizability of Doctor AI by applying the resulting models on data from a completely different medication institution achieving comparable performance. Hence, information can be transferred between models. In other words, an RNN trained on data from one hospital can be used to improve predictions for another hospital with insufficient patient records.

Links to include:

https://arxiv.org/pdf/1511.05942.pdf

https://github.com/mp2893/doctorai

http://mucmd.org/

http://mp2893.com/docs/jamia2016.pdf

http://mp2893.com/


Other papers from Edward mentioned in the show:

https://papers.nips.cc/paper/6321-retain-an-interpretable-predictive-model-for-healthcare-using-reverse-time-attention-mechanism

https://arxiv.org/abs/1611.07012

Remove rasberry pi reference?


<div class="row">
	<div class="col-xs-12 col-sm-3">
		<img alt="Edward Choi, Doctor AI coauthor" src="src-doctor-ai/edward-choi.png" />
		<br/>
		<p><i>Edward Choi</i></p>
	</div>
	<div class="col-xs-12 col-sm-9">
		Edward Choi received his M.S degree in Computer Science and Engineering from the Korea Advanced Institute of Science and Technology in 2009 and his B.S. degree in Computer Science and Engineering from Seoul National University in 2007. He is currently pursuing a PhD in Computer Science at Georgia Tech, under the supervision of Professor Jimeng Sun. Edward's main research interests include predictive modeling, temporal modeling, and healthcare analytics, specifically using representation learning and interpretable deep learning for predictive healthcare. Over the past years, he has held research internships at Sutter Health, DeepMind, and more recently, Google Research.  When he's not in the lab, Edward is a dilettante pianist, a low-budget traveler, a self-approved philosopher, and most of all, a gamer at heart.
	</div>
</div>
