# Prompt Refusal

The creators of large language models impose restrictions on some of the types of requests one might make of them.  LLMs commonly refuse to give advice on 
committing crimes, producting adult content, or respond with any details about a variety of sensitive subjects.  As with any content filtering system, you 
have false positives and false negatives.

Today's interview with Max Reuter and William Schulze discusses their paper "I'm Afraid I Can't Do That: Predicting Prompt Refusal in Black-Box Generative 
Language Models".  In this work, they explore what types of prompts get refused and build a machine learning classifier adept at predicting if a 
particular prompt will be refused or not.
