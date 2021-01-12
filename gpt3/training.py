import random
import json
import nltk
from textblob import TextBlob
import openai
import pickle

nltk.download('brown')
openai.api_key = "sk-bevCcAUQKr16OtmKeFgN93C0uSOGMHQH9Q50ohAs"

from gpt3 import GPT
from gpt3 import Example

token_limit = 100

gpt_model = GPT(engine='davinci', temperature=0.5, max_tokens=token_limit)


with open('../data/sample_text.txt') as text_file:
    i = 0
    for line in text_file:
        blob = TextBlob(line)
        num_of_words = random.randint(1,4)
        input_data = blob.noun_phrases[0:num_of_words]
        input_data.append("funny")
        input_data = str(input_data)

        gpt_model.add_example(Example(input_data, line))
        pickle.dump(gpt_model, open( "../models/gpt3_model.p", "wb" ))
        print("This is the " + str(i) + " iteration.")
        i += 1

