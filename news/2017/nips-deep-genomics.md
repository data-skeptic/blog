## Reprogramming the Human Genome Using AI

The second day of NIPS kicked off with this presentation from Brendan Frey.  In the first minute, he put forward the bold claim "without artificial intelligence medicine is going to completely fail".  The presentation was support for that idea.

He shared a few noteworthy statistics such as people having 65% lifetime risk of genetic disease.  You are more likely than not to face an issue in your lifetime.  There are major costs around treatment, and prevention would be better and more cost effective, naturally.

Its safe to assume that the "low hanging fruit" of preventing and curing diseases has long been picked by the medical community.  It's doubtful simple solutions like vitamin C to prevent scurvy are going to be discovered.  The trends in drug discovery are increasingly costly and increasingly slow.  A better strategy would be warmly welcome and Frey believes that strategy is leveraging machine learning.

Frey further claims that "biology is too complex for any one research or group of researchers to understand".  This being true, it seems machine learning *must* play a strong role in the future of medicine.

### Learning Protein-DNA Binding
An existing system build by Frey's company Deep Genomics trained a model for making protein-DNA binding predictions.  The training data consisted of a 240k sequences of DNA and 200 proteins.  The objective was to predict whether or not the protein would bind to the DNA.  I don't know much about genomics, but I can appreciate this problem purely from a learning perspective.  There is a clear input dataset and an objective function.  There are good questions to be asked about what sort of cost function we use and what diagnostics to use for evaluating our model.  

There are also good questions about whether or not the sequence/protein data contains sufficient information for these prediction to be possible.  The heartbeat data tracked by my fitness band does not have sufficient information content to predict whether or not I'm going to pay my phone bill on time.  My wireless provider should have little or no interest in that dataset.  From what I can tell, however, the mechanics of binding do seem to be mostly covered in this dataset.  There may be environmental interactions or other unknown interactions that play a role, but probably not an active role.

Their technique is a fairly typical convolutional neural network.  Yet their work doesn't stop at the prediction stage.  Once their model is trained, if we assume the model is a good description of the mechanism of binding, then we can use that same model to make inferences.  This is done by feeding the network new data with deliberate mutations introduced.  The model is then asked to predict the impact those mutations would have on the binding.

This is a very novel example of validation for the model.  There are some well studied disease-causing mutations that are known to medical science.  Frey didn't comment on this, but given their rarity, I presume some of these diseases were not represented in the training data.  He reports that their system did reliably well at predicting risk in cases of well established disease causing mutations.  The degree to which this is true constitutes a huge win for the model.  It means their model has learned a general representation of the of the mechanism, rather than learned to simply recognize cases it saw enough examples of.  If this result generalizes and replicates well, it could provide a roadmark for what mutations should be studied further due to perceived potential for harm.

In some ways, this is an incredible chance to go out and do validation.  Their model claims to not only be consistent with available genomics knowledge, but also makes verifiable predictions about how certain mutations that aren't well studied might affect the binding process.




