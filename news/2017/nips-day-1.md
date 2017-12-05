## NIPS Day 1

<img src="src-nips-day-1/badge.jpg" />

## Reprogramming the Human Genome Using AI, Brendan Frey

"Without artificial intelligence medicine is going to completely fail"

65% lifetime risk of genetic disease

8M births per year with serious genetic defect
$5 M lifetime cost per baby

Pharma is broken.  EvaluatePharma

"How to convert the genome into actionable information"

PROMOTER
EXON - print statement
INRON - removed, control logic, how to assemble the gene

"Biology is too complex for any one research or group of researchers to understand"

### Learning Protein-DNA Binding
240k sequences
200 protiens
Will it bind?
CNN
The ML isn't hard
What is the right cost function for producing a NN which is useful in practice?

Using NN for predictions about mutations.  Change one input and predict how much that mutation will change protein binding. !!!!!

Known disease-causing mutations are frequently predicted, but not always
New predictions are made

They build a CNN which tries to predict the changes to binding given a mutation.  They trained on some training data, and then introduced new examples the system never saw before by inputing examples of mutated genes.

Often, the predicts made align with known disease causing mutations - a very nice validation

But it also makes some predictions that aren’t known to be disease causing

This is an even better chance to go out and do validation, since a new prediction not known to medicine is being mae


### Deep Genomics

Genomics profiling tools.  

Spinal muscular atrothy - trial was terminated early because drug was so affective, it was deemed unethical to not give it to the placebo group.

Spinraza - A digital medicine.  You can download it.  Specified and synthesized digitally.  Mutation causes an Exon to be skipped and not included in a protein.

Deep Genomics wants to use ML to accellerate early exploratory work in developing a drug.

Sometimes the mutation makes the protien go wrong but the fix is not to change but to introduce another protein.  Mechanism of a disease and mechanism of action may not be the inverse of one another.

Their ML tool put Spinraza in 3rd place as predicted likelihood of success.  Boldly said other two might be better.  Important part is how many need to be tested.

Cloud Labratory - Upload a python script which specifies the experimental protocol.  Robots then conduct the experiment.


### Project Saturn

Using AI to search over 69 billion compounds
1000 compound verified in human cells
3 therapies in clinical trials in the next 3 years

Great question for information theorist - genome can be stored in 2x size of all nips PDF procedings.  Can genetics fully specify?  Branden correctly mentioned compression.  Environmental factors.




