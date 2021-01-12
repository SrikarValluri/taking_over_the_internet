import random
import json
import nltk
from textblob import TextBlob
import openai


gpt = pickle.load(gpt, open( "../models/gpt3_model.p", "rb" ))

prompt1 = ["trump", "impeachment", "capitol", "america", "funny"]
prompt2 = ["game of thrones", "trump", "funny"]
prompt3 = ["epic fortnite gamer", "apex legends", "ban for racism", "funny"]
prompt4 = ["meme", "bruh moment", "artificial intelligence", "funny"]

output1 = gpt.submit_request(prompt1)
output2 = gpt.submit_request(prompt2)
output3 = gpt.submit_request(prompt3)
output4 = gpt.submit_request(prompt4)

print(output1.choices[0].text)
print(output2.choices[0].text)
print(output3.choices[0].text)
print(output4.choices[0].text)