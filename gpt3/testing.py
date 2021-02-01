import random
import json
import nltk
from textblob import TextBlob
import openai
import pickle

from gpt3 import GPT 
from gpt3 import Example

from noun_scraper import iterator

nltk.download('brown')
openai.api_key = "sk-bevCcAUQKr16OtmKeFgN93C0uSOGMHQH9Q50ohAs"

gpt = pickle.load(open( "../models/gpt3_model.p", "rb" ))

input_data_not_funny = iterator('../data/ap_headlines_test.txt', 'funny')

for example in input_data_not_funny:
    noun_input = str(example[0])
    output = gpt.submit_request(noun_input)
    print(noun_input, output.choices[0].text)


# prompt1 = '["belting highs", "voice crack","drug", "funny"]'
# prompt2 = '["beer", "pingpong", "cramps", "funny"]'
# prompt3 = '["homework", "ocean", "cakes", "funny"]'
# prompt4 = '["kids", "funny"]'
# prompt5 = '["dorm", "ripperoni", "funny"]'


# output1 = gpt.submit_request(prompt1)
# output2 = gpt.submit_request(prompt2)
# output3 = gpt.submit_request(prompt3)
# output4 = gpt.submit_request(prompt4)
# output5 = gpt.submit_request(prompt5)


# print(prompt1, output1.choices[0].text)
# print(prompt2, output2.choices[0].text)
# print(prompt3, output3.choices[0].text)
# print(prompt4, output4.choices[0].text)
# print(prompt5, output5.choices[0].text)