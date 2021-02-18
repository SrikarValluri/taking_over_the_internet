import json
import sys
import getopt
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

class HeadlinePair(object):
    """
    A pair of headlines, each of type HeadlineNounPair. This pair 
    consists of a satirical headline and a real headline. 
    """
    def __init__(self, satirical, real):
        """ 
        initialize a pairing of a real headline and a satirical headline
        from their respective HeadlineNounPair objects.

        :param satirical: the satirical HeadlineNounPair
        :param real: the real HeadlineNounPair
        """
        self.satirical = satirical
        self.real = real
        self.overlap = list(set(satirical.nounlist)&set(real.nounlist))
        self.likeness = len(self.overlap)

def extractNouns(line):
    """
    Uses TextBlob to detect nouns in lines, returning them as a list.

    :param line: The line to extract nouns from
    """
    # this doesn't work very well.
    #return TextBlob(line).noun_phrases

    # this has been working better.
    words = line.split()
    for w in words:
        w = w.upper()
    return words


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
        self._pairs = []
        self.satiricalHLs = satiricalHLs
        self.realHLs = realHLs
        self.threshold = threshold
        self.reals = createHeadlineNounlistPairs(realHLs)
        self.satiricals = createHeadlineNounlistPairs(satiricalHLs)

    def rank(self):
        """
        Loop through every combination of real/satirical headline, creating lists of pairs. 
        These pairs are sorted by likeness, and all pairs above the specified threshold are 
        returned.
        """
        for sat in self.satiricals:
            for real in self.reals:
                _temp = HeadlinePair(sat, real)
                if(_temp.likeness > self.threshold):
                    self._pairs.append(_temp)
        self._pairs = sorted(self._pairs, key=lambda pair: pair.likeness, reverse=True)


def main(argv):
    """
    This method of input validation comes from tutorialspoint at
    https://www.tutorialspoint.com/python/python_command_line_arguments.htm
    """
    reals = ''
    satiricals = ''
    threshold = 0
    try:
       opts, args = getopt.getopt(argv, "hi:o:", ["real=", "satirical=", "threshold="])
    except getopt.GetoptError:
       print('article_sort -r <reals> -s <satirical> -t <threshold>')
       sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('article_sort -r <reals> -s <satirical> -t <threshold>')
            sys.exit()
        elif opt in ("-r", "--real"):
            reals = arg
        elif opt in ("-s", "--satirical"):
            satiricals = arg
        elif opt in ("-t", "--threshold"):
            threshold = int(arg)
    r = Ranking(satiricals, reals, threshold)
    r.rank()
    for p in r._pairs:
        print(p.overlap)
        print(p.likeness)
        print("---")

if __name__ == "__main__":
    main(sys.argv[1:])
