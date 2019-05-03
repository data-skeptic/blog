## The Transformer

I didn't like the last episode

I overemphasized context and remembering on attention.
i did taht to focus on the mechanism of deep learning
attention is more about linking

image attention is a bit mask

Attention distribution
In context of reading
In context of writing
	bread crumb - differentiable, convex combination
	ML is not just trying stuff.  Its asking why DIDN'T my solution work
	Also cost prohibitive
	I do some of this but not a huge amount, you as CFO don't know it

Topic is the transformer

Remember embeddings?
king minus queen
Fails on "bank" - water or institution?

RIDDLES
* Consumes electricity
* A place of commerce
* Food has a strong presence there
* People can enter this place from the street
* On a given day, few people are consistently there

* Consumes electricity
* A place of commerce
* Food has a weak presence
* Only certain people can go to this place
* On a given day, most people are the same

* DOES NOT Consumes electricity
* Can be found near Central Park in NYC

As the decoder starts decoding, it uses the encoding that is of the entire sentence AND the previous step to disambiguate or "pick" the best representation





stack of encoders
stack of decoders that all read each other and the encoding
self-attention
encoder-decoder attention



It applies a self-attention mechanism which directly models relationships between all words in a sentence, regardless of their respective position. 

More specifically, to compute the next representation for a given word - “bank” for example - the Transformer compares it to every other word in the sentence.





Story begins with the idea of RNN
LSTM
Neuro Turing Machines




Thank listener for details about 7 slots of memory



The Transformer – a model that uses attention to boost the speed with which these models can be trained

The biggest benefit, however, comes from how The Transformer lends itself to parallelization

The Transformer was proposed in the paper Attention is All You Need. A TensorFlow implementation of it is available as a part of the Tensor2Tensor package

encoder
decoder

layers of encoders
encoder = self-attention and feed forward
same feed forward network in each encoder layer

The decoder has both those layers, but between them is an attention layer that helps the decoder focus on relevant parts of the input sentence (similar what attention does in seq2seq models).


encoder recieves a list of vectors
not cencatenates, run separately


”The animal didn't cross the street because it was too tired”

What does “it” in this sentence refer to? Is it referring to the street or to the animal? It’s a simple question to a human, but not as simple to an algorithm.

http://jalammar.github.io/images/t/transformer_self-attention_visualization.png


