import random
import json
import nltk
from textblob import TextBlob
import openai
import pickle

from gpt3 import GPT 
from gpt3 import Example


nltk.download('brown')
openai.api_key = "sk-bevCcAUQKr16OtmKeFgN93C0uSOGMHQH9Q50ohAs"

gpt = pickle.load(open( "../models/gpt3_model.p", "rb" ))

# prompt1 = '["trump", "impeachment", "capitol", "america", "funny"]'
# prompt2 = '["game of thrones", "trump", "funny"]'
# prompt3 = '["epic fortnite gamer", "apex legends", "ban for racism", "funny"]'
# prompt4 = '["meme", "bruh moment", "artificial intelligence", "funny"]'
prompt5 = '["insurrectionist", "dab on the haters", "lemons", "funny"]'


# output1 = gpt.submit_request(prompt1)
# output2 = gpt.submit_request(prompt2)
# output3 = gpt.submit_request(prompt3)
# output4 = gpt.submit_request(prompt4)
output5 = gpt.submit_request(prompt5)


# print(output1.choices[0].text)
# print(output2.choices[0].text)
# print(output3.choices[0].text)
# print(output4.choices[0].text)
print(output5.choices[0].text)