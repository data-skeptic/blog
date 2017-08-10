## Project Common Voice

In this week’s episode, guest Andre Natal from Mozilla joins our host, Kyle Polich, to discuss a couple exciting new developments in open source speech recognition systems, which include [Project Common Voice](https://voice.mozilla.org/). 

In June 2017, Mozilla launched a new open source project, Common Voice, after quietly working on an open source, [TensorFlow-based DeepSpeech](https://github.com/mozilla/DeepSpeech) implementation. DeepSpeech is a deep learning-based voice recognition system that was designed by Baidu, which they describe in greater detail in their [research paper](https://arxiv.org/abs/1412.5567). DeepSpeech is a speech-to-text engine, and Mozilla hopes that, in the future, they can use Common Voice data to train their DeepSpeech engine.

These projects come at a time when the ratio of voice searches on mobile devices is growing at a faster rate than the type searches. While voice recognition systems and their use become more ubiquitous in the tech world, they are neither easy to build nor cheap to develop. In addition, voice recognition systems require a great deal of data to learn from, which is often proprietary and so not available to independents and small start-ups. For this reason, a team from Mozilla (makers of Firefox), has come forward with the crowdsource initiative, Project Common Voice, to collect voice samples from the public and have them validate the entries. 

The goal is to collect 10,000 hours of speech samples in various different accents, with various different noises, in order to make models and make them freely available to the public. Anyone can contribute to the project through submitting their voice samples through the [project website](https://voice.mozilla.org/), where users can volunteer to read words and/or sentences. Another way for volunteers to contribute is to spend a little time validating the sentences read by others, in order to help train this democratized voice recognition system. The more voice people donate and help out with validating samples, the better Common Voice will get. So far, according to Andre, almost all readings have been accurate, with no users purposely sabotaging the project.

These validated voice samples then get added to the server, which will then be freely available to independent developers who want to take the initiative and train speech-to-text systems for their projects. Project Common Voice uses [Kaldi](https://github.com/kaldi-asr/kaldi), an open source speech recognition toolkit to analyze voice commands.

The focus of Common Voice is on collecting as much accents and noises as possible so that the system works on spot. Currently, the data that is being used to teach computers to understand our voices are primarily biased towards a select group of languages, including English, Chinese, and Western European languages. Hence, the datasets being used to powers big tech apps don’t understand us all. Moreover, these datasets are often proprietary. 

Mozilla plans to make the models they develop open to the public by the end of the year, along with the full data sets of raw audio files and annotated samples, so that people can develop and train their own models.

##Links and Resources:

[Mozilla launches experimental voice search, file-sharing and note-taking tools for Firefox](https://techcrunch.com/2017/08/01/mozilla-launches-experimental-voice-search-file-sharing-and-note-taking-tools-for-firefox/)

[Voice Fill Test Pilot](https://github.com/mozilla/speech-proxy) of Mozilla's new speech recognition technology

[Kaldi](http://kaldi-asr.org/) - An open source speech recognition decoder.

<div class="row">
        <div class="col-xs-12 col-sm-3">
                <img alt="Andre Natal" src="src-project-common-voice/andre-natal.jpg" />
                <br/>
                <p><i>Andre Natal</i></p>
        </div>
        <div class="col-xs-12 col-sm-9">
		Andre Natal is a Speech Engineer at Mozilla with over 17 years of experience in the development, architecture, and management of software projects. He has extensive experience in software engineering, having worked in various industries, such as Internet, legal, government, media, Wall Street, microelectronics, and mobile. Andre is passionate about speech and audio technologies and has deployed a large number of awarded applications across different platforms, including mobile apps, IVR, and the IoT. He is particularly interested in building conversational agents, speech-enabled devices, and building voice-controlled VR/AR experiences. Andre holds a Bachelor’s degree in Information Systems from the Universidade Anhembi Morumbi in São Paulo, Brazil.
        </div>
</div>

