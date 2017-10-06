## Data Science Tools and Other Announcements from Ignite

In this episode, Microsoft's Corporate Vice President for Cloud Artificial Intelligence, Joseph Sirosh, joins host Kyle Polich to share some of the Microsoft's latest and most exciting innovations in AI development platforms. Last month, Microsoft launched a set of three powerful new capabilities in Azure Machine Learning for advanced developers to exploit big data, GPUs, data wrangling and container-based model deployment. 

The first new feature, the AML Workbench, is a cross-platform client that integrates AI-powered data wrangling into the client itself, which allows the user to transform data with the power of AI. The second new feature is the AML Experimentation service on the cloud that enables data scientists to track and manage their big data experiments on Spark and GPUs, etc. using all the power in the cloud. And the third announcement is the AML Model Management service to host, version, manage and monitor machine learning models.

Joseph discusses the three features in some detail with Kyle, but for a deep dive into each one, you can visit his blog [here](https://azure.microsoft.com/en-us/blog/diving-deep-into-what-s-new-with-azure-machine-learning/).

The AML Workbench is a client application that runs on Windows and Mac and serves as a control panel for your development lifecycle. Building on the latest research in program synthesis (PROSE) and data cleaning,  Microsoft created a data wrangling technology that can drastically reduce the time that data scientists have to spend in coding and transforming data for machine learning. The way program synthesis works are, you give an input, the kind of data you want to wrangle, and the output you want to transform to, so you control the before and after. And then, the program synthesis technique will generate a program for that data transformation automatically for the user, and the program can be run on all of the data and verify that it works. If there are examples where it doesn't work, the user can give more character examples, and it will re-generate a new program that fits it better. 

The AML Experimentation Service allows machine learning experimentation at any scale, leveraging the cloud. ML experiments can run on a local machine, inside of a Docker container locally or on Azure. Through the service, experiments can even scale-out on top of Apache Spark on Azure HDInsight clusters.  The Experimentation Service can support a variety of open source deep learning frameworks, such the Microsoft Cognitive Toolkit, Tensorflow, Caffe2, PyTorch and Chainer. Leveraging the Azure Batch AI Training service, each deep learning experiment can utilize hundreds of GPU virtual machines. The new service can track, store and manage models, configuration, parameter, and data using Git repositories. These features enable users to record the run history on all the experiments run, which allows them to compare and contrast model runs, and review performance under different parameters.

The AML Model Management Service allows data scientists and developers to deploy and manage their trained models locally to or to large-scale cluster deployments in the cloud. Models can be containerized in Docker and implemented on network edge devices, allowing models to score closer to the event and in real-time. Once in production, models can be monitored for performance using Azure Application Insights and then proactively retrained if data drift or other circumstances begin to degrade performance. 

These three new features together offer end-to-end tools for AI development. A recording of Joseph's session at Microsoft Ignite 2017 is available [here](https://www.youtube.com/watch?v=MUqo-lsAKgQ&feature=youtu.be). 

Other announcements from Ignite 2017 mentioned in the show:

- Excel integration, using which organizations can create custom models using AML and deploy them as cloud hosted functions in Excel, allowing ML/AI to integrate more naturally into your spreadsheets.

- Visual Studio Code Tools for AI, for easily building models with deep learning frameworks including Microsoft Cognitive Toolkit (CNTK), TensorFlow, Theano, Keras, Chainer, and Caffe2. This tool integrates the AML Experimentation service to execute jobs locally and in the cloud and deploy a web service with the AML Model Management.

- The first version of SQL Server 2017 that can run on Windows Server, Linux, and Docker. SQL Server 2017 enables advanced in-database machine learning and supports scalable Python and R-based analytics. The user can now train the most sophisticated models efficiently with data inside SQL Server, without having to move data. 

- The new release of Microsoft Machine Learning Server,
Azure CosmosDB database service and serverless Azure Functions that enables developers to write a few lines of code that can tie machine learning into Internet of Things (IoT) sensors, database changes, and more.

- Deep Learning Virtial Machine (DLVM), a configured variant of the Data Science VM to help users jump-start deep learning on Azure GPU VMs. Since DLVM uses the same underlying VM images as the Data Science VM, it comes with the same set of data science tools and deep learning frameworks as the base VM.

- Finally, a rich set of AI Solutions for Enterprises, designed to tackle high value, complex enterprise scenarios, helping companies speed up their digital transformation.

## Links and Resources:

[Joseph’s blog on AI announcements at Ignite](https://azure.microsoft.com/en-us/blog/tools-for-the-ai-driven-digital-transformation/)

[Microsoft AI Platform](https://www.google.com/url?hl=en&q=http://azure.com/ai&source=gmail&ust=1507326032660000&usg=AFQjCNFjp9L4liYt8Io9oQjEpczWOPT3rA)

[Introduction to Azure Machine Learning](https://docs.microsoft.com/en-us/azure/machine-learning/preview/overview-what-is-azure-ml)

Quick Start Tutorials for [Data Preparation](https://docs.microsoft.com/en-us/azure/machine-learning/preview/tutorial-classifying-iris-part-1), [Build a model](https://docs.microsoft.com/en-us/azure/machine-learning/preview/tutorial-classifying-iris-part-2), [Deploy a model](https://docs.microsoft.com/en-us/azure/machine-learning/preview/tutorial-classifying-iris-part-3), [Advanced Data Preparation](https://docs.microsoft.com/en-us/azure/machine-learning/preview/tutorial-bikeshare-dataprep)

### Sponsored by Springboard
Check out Springboard's [Data Science Career Track Bootcamp](https://sbdata.co/datascareer)

<br/><br/><br/>

<div class="row">
	<div class="col-xs-12 col-sm-3">
		<img alt="Joseph Sirosh" src="src-data-science-tools-and-other-announcements-from-ignite/joseph-sirosh.jpg" />
		<br/>
		<p><i>Joseph Sirosh</i></p>
	</div>
	<div class="col-xs-12 col-sm-9">
		Joseph Sirosh is the Corporate Vice President for the Data Group at Microsoft, where he leads the company’s database, big data, and machine learning products. Joseph holds a PhD in Computer Science from the University of Texas at Austin and a B.Tech. in Computer Science & Engineering from the Indian Institute of Technology Chennai. He is very passionate about machine learning and its applications. One of his missions at Microsoft is to democratize ML technology and make it accessible to everybody.
	</div>
</div>
