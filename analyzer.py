import nltk
from nltk.tokenize import TweetTokenizer

class Analyzer():
    """Implements sentiment analysis."""

    def __init__(self, positives, negatives):
        """Initialize Analyzer."""
        
        # initialize the lists as instance variables
        self.positives = []
        self.negatives = []
        
        # load positives text into positives list
        with  open("positive-words.txt", "r") as plist:
            self.positives = [word.strip() for word in plist if word.startswith((";", " "))== False]
                    
        # load negative text into negatives list
        with  open("negative-words.txt", "r") as nlist:
            self.negatives = [word.strip() for word in nlist if word.startswith((";", " ")) == False]

    def analyze(self, text):
        """Analyze text for sentiment, returning its score."""
        
        # initialize the score tracker
        score = 0
        
        # tokenize or spilt the tweet into ind. words
        tokenizer = nltk.tokenize.TweetTokenizer()
        tokens = tokenizer.tokenize(text)
        
        # iterate over each split up word or token
        for token in tokens:
            if token.lower() in self.positives:
                score += 1
            elif token.lower() in self.negatives:
                score -= 1
            else:
                score
        
        # return the total sentiment score for the given tweet
        return score
        