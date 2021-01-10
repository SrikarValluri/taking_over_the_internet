import json
import nltk
from textblob import TextBlob
# import openai


nltk.download('brown')
openai.api_key = "sk-bevCcAUQKr16OtmKeFgN93C0uSOGMHQH9Q50ohAs"

from gpt import GPT
from gpt import Example

token_limit = 0

gpt = GPT(engine='davinci', temperature=0.5, max_tokens=token_limit)


with open('../data/sample_text.txt') as text_file:
    for line in text_file:
        blob = TextBlob(line)
        gpt.add_example(Example(blob, line))

pickle.dump(gpt, open( "../models/gpt3_model.p", "wb" ))