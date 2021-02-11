import json
from textblob import TextBlob

"""
This module includes functionality to pair articles/headlines
based on common nouns used in the headlines. The intent is to be
able to match a satirical article with its factual counterpart, 
and to rank these pairs by relevance to each other. This allows
for bulk training of our AI.
"""

class HeadlineNounPair(object):
    """
    A HeadlineNounPair allows a given headline as a string to be
    associated with the list of nouns extracted from it. 
    """
    def __init__(self, headline, nounlist):
        """
        set up a pairing of a headline with its extracted nouns.
        
        :param headline: The headline string
        :param nounlist: The list of extracted nouns
        """
        self.headline = headline
        self.nounlist = nounlist

def extractNouns(line):
    """
    Uses TextBlob to detect nouns in lines, returning them as a list.

    :param line: The line to extract nouns from
    """
    return TextBlob(line).noun_phrases

def createHeadlineNounlistPairs(filename):
    """ 
    Create headline-nounlist pairs from each line in a file, to allow for the 
    comparison and sorting of the headlines based on the noun-phrase contents.

    :param filename: The name of the file containing the headlines. One headline per line please.
    """
    with open(filename) as text_file:
        pairs = []
        for line in text_file:
            _line = line.strip()
            pairs.append(HeadlineNounPair(_line, extractNouns(_line)))
        return pairs

class Ranking(object):
    """
    A Ranking contains data for processing the relevance between 
    sets of article headlines. It can produce json that represents
    the training pairs produced from the input headlines that are 
    above the threshold value of relevance given.
    """
    def __init__(self, satiricalHLs, realHLs, threshold):
        """
        Set up a Ranking.

        :param satiricalHLs: The filename of the satirical headlines input file. One headline per line please.
        :param realHLs: The filename of the real headlines. One headline per line please.
        :param threshold: An integer that represents the minimum numnber of shared nouns between a pair of headlines to be considered minimally relevant to each other. 
        """
        self.satirical = satiricalHLs
        self.realHLs = realHLs
        self.threshold = threshold
        