# Prompt Refusal

The creators of large language models impose restrictions on some of the types of requests one might make of them.  LLMs commonly refuse to give advice on committing crimes, producing adult content, or responding with any details about a variety of sensitive subjects.  As with any content filtering system, you have false positives and false negatives.

Today's interview with Max Reuter and William Schulze discusses their paper [I'm Afraid I Can't Do That: Predicting Prompt Refusal in Black-Box Generative Language Models](https://dataskeptic.com/blog/episodes/2023/prompt-refusal).  In this work, they explore what types of prompts get refused and build a machine learning classifier adept at predicting if a particular prompt will be refused or not.

They started by explaining what prompt refusal is. They shared the kind of prompts that are typically refused and why. They also discussed how these models possibly determine the type to refuse. Additionally, they addressed the issue of using closed algorithms to train the ethical aspects of LLMs. Max shared ways that researchers can help solve specific limitations of LLMs. In their research, they focused on building a prompt refusal classifier.

Max talked about the datasets they used to train their classification model and the required feature engineering. They also shared the accuracy of the model and some sources of irreducible error for the task.

Max and William discussed some valuable insights they could extract from the functioning of LLMs' responses. They also shared the possible room for improvements in their work. Concluding they discussed where future research for them is headed.

Follow both guests on Twitter: [@MaxReuter__](https://twitter.com/MaxReuter__) [@wbschulze](https://twitter.com/wbschulze)


