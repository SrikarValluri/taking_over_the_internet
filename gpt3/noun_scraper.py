import random
import json
import nltk
from textblob import TextBlob
import openai
import pickle

nltk.download('brown')


def nounsFromLine(line, humor_level):
    blob = TextBlob(line)
    input_data = blob.noun_phrases
    output_data = []
    for element in input_data:
        willItBeChosen = random.randint(0,1)
        if willItBeChosen:
            output_data.append(element)
    output_data.append(str(humor_level))

    return output_data

def iterator(filename, humor_level):
    with open(filename) as text_file:
        output_data = []
        for line in text_file:
            output_data.append((nounsFromLine(line, humor_level), line.strip()))
    
    return output_data




# output_data = iterator("../data/random_relevant_words.txt")
# for element in output_data:
#     print(element)

