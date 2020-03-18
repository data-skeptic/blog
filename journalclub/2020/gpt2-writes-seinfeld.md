# GPT-2 writing comedy sitcom?

Hi! This is a first experiment to see if a state-of-the-art language model such as [GPT-2](https://github.com/openai/gpt-2) can learn to write comedy sitcom in the course of one night.  I thought we might as well let the [transformer](https://jalammar.github.io/illustrated-transformer/) learn from the best and start it off with the finest material.  [**Seinfeld**](https://www.imdb.com/title/tt0098904/) is my all time favorite comedy show on TV, that's what I'll go with!  


## The training (fine-tuning) data

I scraped all the Seinfeld scripts from http://www.seinology.com a couple years ago - this site actually doesn’t exist anymore.  Each episode is one text file, I concatenated them with '<|endoftext|>' added to the end of each episode and stripped out excess `\t` and `\n` characters. Pretty minimal cleaning. This generated ~4.5MB of text.

**Data hosted [here](https://raw.githubusercontent.com/LanGuo/seinfeldNLP/master/all_scripts.txt).**

## Getting started – installation in a Python virtual environment
The GPT-2 fine-tuning and text generation was made super straightforward by the good folks at [Hugging Face](https://github.com/huggingface).  We'll start by cloning their transformers [repo](https://github.com/huggingface/transformers) into a fresh virtual environment and installing other dependencies.

```
python3 -m venv huggingface

source huggingface/bin/activate

mkdir src

cd src/

git clone https://github.com/huggingface/transformers

cd transformers

pip install .

pip install -r ./examples/requirements.txt

pip install torch torchvision
```

## Fine tuning

Oh by the way, did I mention I only have one GPU (GeForce GTX 1050) on my laptop with 2GB memory?  This is not nearly enough for training such a big model. So I resorted to using CPU for training.

If I run training with `--per_gpu_train_batch_size=4`, which is the default, I needed more RAM than the 15.5GB+8GB swap current available.  One option is to increase the swap to 16GB.  Thanks to [this post](https://bogdancornianu.com/change-swap-size-in-ubuntu/) for the commands below.
```
$ sudo swapoff -a

$ sudo dd if=/dev/zero of=/swapfile bs=1G count=16

16+0 records in

16+0 records out

17179869184 bytes (17 GB, 16 GiB) copied, 14.0243 s, 1.2 GB/s

$ sudo mkswap /swapfile

Setting up swapspace version 1, size = 16 GiB (17179865088 bytes)

no label, UUID=e17a7090-cbe5-4d44-9e44-b5df679b9ea7

$ sudo swapon /swapfile

$ grep SwapTotal /proc/meminfo

SwapTotal: 16777212 kB
```
Another option, which I ended up doing, is to train with `--per_gpu_train_batch_size=1 --gradient_accumulation_steps=4`, this works on 15.5GB of RAM.


```
(huggingface) (base) ~/virtual_envs/huggingface/src/transformers/examples master $ python run_lm_finetuning.py \ 
--no_cuda \
--output_dir=output \
--model_type=gpt2 \
--model_name_or_path=gpt2 \
--do_train \
--train_data_file=./all_scripts.txt \
--per_gpu_train_batch_size=1 \
--gradient_accumulation_steps=4
```
I used pretty much all default parameters for training, and did not do evaluation.  Here are the list of parameters:


```
Training/evaluation parameters Namespace(adam_epsilon=1e-08, block_size=1024, cache_dir='', config_name='', device=device(type='cpu'), do_eval=False, do_lower_case=False, do_train=True, eval_all_checkpoints=False, eval_data_file=None, evaluate_during_training=False, fp16=False, fp16_opt_level='O1', gradient_accumulation_steps=4, learning_rate=5e-05, local_rank=-1, logging_steps=50, max_grad_norm=1.0, max_steps=-1, mlm=False, mlm_probability=0.15, model_name_or_path='gpt2', model_type='gpt2', n_gpu=1, no_cuda=True, num_train_epochs=1.0, output_dir='output', overwrite_cache=False, overwrite_output_dir=False, per_gpu_eval_batch_size=4, per_gpu_train_batch_size=1, save_steps=50, save_total_limit=None, seed=42, server_ip='', server_port='', tokenizer_name='', train_data_file='./all_scripts.txt', warmup_steps=0, weight_decay=0.0)
```
This whole training (fine-tuning) took about 3 hours on my Intel(R) Core(TM) i7-7700HQ CPU @ 2.80GHz.  Running the fine-tuning script generates an `output` directory, with the specified checkpoints (in the default setting, every 50 steps) saved.  You will need this directory to load back the fine-tuned model and tokenizer configuration and weights.


## Text generation 

Now we have trained GPT-2 on Seinfeld scripts!  Can it generate some text that looks like a sitcom script and (dare we hope) is funny?  Let's find out:
```
(huggingface) (base) ~/virtual_envs/huggingface/src/transformers/examples master $ python run_generation.py --model_type=gpt2 --model_name_or_path=output/ --length=200 –repetition_penalty=1 --no_cuda
```
Notice one of the parameter is the directory storing the fine-tuned model (`output`).  Here I did not set `--repetition_penalty` and use the default (1.0), prompted with some text, the output can get very repetitive and doesn't do anything interesting:
```
Model prompt >>> Elaine: Jerry! George! You guys, listen!

Elaine: Jerry! George! You guys, listen! I'm gonna be here for a while. 
JERRY: (to Elaine) I'm sorry. ELAINE: (to Jerry) I'm sorry. JERRY: (to Elaine) I'm sorry. ELAINE: (to Jerry) I'm sorry. JERRY: (to Elaine) I'm sorry. ELAINE: (to Jerry) I'm sorry. JERRY: (to Elaine) I'm sorry. ELAINE: (to Jerry) I'm sorry. JERRY: (to Elaine) I'm sorry. ELAINE: (to Jerry) I'm sorry. JERRY: (to Elaine) I'm sorry. ELAINE: (to Jerry) I'm sorry. JERRY: (to Elaine)!
```
Let's try to increase the length of generated text, as well as increase the repetition penalty (this changes the model behavior from always picking the predicted output with the highest likelihood to choosing somewhat randomly from the top N).  This generation unfortunately also needs to be run on CPU (with `--no_cuda`) since GPU quickly ran out of the 2GB memory.
```
$ python run_generation.py --model_type=gpt2 --model_name_or_path=output/ --length=200 –repetition_penalty=5 --no_cuda
```
It came up with something like this with the same prompt:
```
Model prompt >>> Elaine: Jerry! George! You guys listen!

Elaine: Jerry! George! You guys listen! 
JERRY (to Elaine): Hey, I'm sorry. It's a little late for me to go out with you today but it was nice meeting ya again and we're gonna have some fun tonight...I'll see y'all later on in the day.." "Oh yeah? What are they doing here?" Kramer enters from his apartment wearing an orange jacket that he has been carrying since last night - this is what looks like something made of rubber gloves or plastic bags. He walks into another room where there isn't much else going around except one thing at least :) The door opens behind him, revealing himself as Mr Puddy Ross Jr., who sits down next Toppleman & Co.'s office building overlooking Broadway Street between Eighth Avenue Sandler Boulevard E-6A/B&C Blvd.(Jerry can hear them talking.) They've got their own offices right across street; so if!
```
Hey, more interesting!


## Some interesting model behavior

### Difficulty in generating text following a scene description
Could this be due to the limited scene description available in the training data (mostly in dialogue-form), and the unique nature of a scene never before seen?
For example, it did not have much to say here:
```
Model prompt >>> Kramer walks into the bar and headed towards the pool table

Kramer walks into the bar and headed towards the pool table. 
"Hey, Kramer!
```
Notice the generated text stopped way before reaching the maximum length set (500). And here:
```
Model prompt >>> Kramer walks into the bar

Kramer walks into the bar, and Kramer is there. KRAMER: Hey!
```
It just does not think Kramer belongs in a bar!! And apparently, neither does Jerry:
```
Model prompt >>> Jerry walks into a bar

Jerry walks into a bar, and the waitress is there. JERRY: Hey Jerry!
```

### Making the prompt super general increases the generated text length?
Here I used a super short and general prompt, and the model got quite talkative!
```
Model prompt >>> Jerry: George!

Jerry: George! 
GEORGE (to the crowd): Hey, hey. I'm gonna go get some coffee and a little something to eat tonight? You know what's better than that?! It'll be great!! Oh yeah...I got this one for you today..(he leaves)..and it was so good!!! So much fun watching your favorite show on TV....you're not even kidding me.....soooooo cool......it really is an amazing experience!!!!!!!!! Jerry : What are ya doing here?? Where do we start??? We gotta have dinner with Elaine right now.......she has no idea how she can make such incredible food out of nothing but her own imagination.........but then again maybe they don't want us there anymore because he doesn' think about them like Kramer does when his parents die.........................(George enters.)........Oh my God........that guy who made those pancakes in front Of The World That Wasn 'em all over him....He just couldn-t stop laughing at himself as if someone had said "Hey look man" or whatever else people say around these parts." He laughs back tearsful laughter from everyone except myself. And after seeing everything happen,the whole thing went down very quickly...then suddenly everybody started talking loudly --they were yelling loud enough--They yelled louder too -And by time somebody came up behind their backs screaming "...You wanna see more?" They screamed harder still."So why did anyone come forward? Because nobody wanted anything done against anybody other Than Himself! Why didn’s anyone tell Mr Seinfeld “Mr Larry David"? Well guess where would've been our next move anyway since Mrs Ollie left home last night................Well wait till tomorrow morning before going anywhere......We will find another place soon..........<|endoftext|>Episode 85 – A Very Merry Christmas

A few weeks ago while working through work assignments during lunch break,... Free View In iTunes #1 Episode 83 This week Steve joins Andy & Julia along side host John Krasinski (@Kraigsberg). Today Tony talks w/ Jimmy Fallon regarding being fired due *not* having sex; getting married early into life without consenting adults involved); making friends outside marriage via dating sites etc.; meeting new women using fake names instead thereof ; trying different methods including taking off clothes whilst walking alone together under heavy traffic lights which led many men away ); finding love within hours upon arrival inside prison cell only once per day until finally returning safely afterwards ) How long should each episode take!
```
It even knows to insert some scene description, such as  "(George enters.)", episode description "Episode 85 – A Very Merry Christmas" (a made-up episode name!), and even something that looks like promotional content (an interview?) at the end there. Pretty amazing!

## Wrap up
I hope this has been a fun read to you, certainly has been an entertaining learning experience for me.  I'll probably be doing more experiments with this, if you have any comments or suggestions for things I can try, please leave a comment or get [in touch](https://github.com/LanGuo/seinfeldNLP/) with me!
<!--stackedit_data:
eyJoaXN0b3J5IjpbMjM4NTA1Nzg3LDk5MDIwOTI5MywxMjg1Nj
M2NDE2LC03OTc5NTcwNTQsLTU4MTM5NjQ0NSwtMzc4MjE1MTEw
LDE2OTgyNjQ3MzEsMjA2NTQ1NDUwNl19
-->