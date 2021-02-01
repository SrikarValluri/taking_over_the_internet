import requests
from bs4 import BeautifulSoup
# import numpy as np
# import pandas as pd
# import time
import nltk
from newspaper import Article
from textblob import TextBlob


res = requests.get('https://www.theonion.com/')
print(type(res))

soup = BeautifulSoup(res.text, 'lxml')
print(type(soup))

link_list = []

for link in soup.find_all('a', href=True):
    # https://www.theonion.com/
    beginning = link['href'][:25]

    if(beginning == 'https://www.theonion.com/'):
        link_list.append(link['href'])


for link in link_list:
    article = Article(link)
    article.download()
    article.parse()
    article.nlp()
    print(article.text)