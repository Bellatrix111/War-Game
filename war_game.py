import random 

class Card:
    def __init__(self, suit, rankvalue, rankname):
        self.suit = suit
        self.rankvalue = rankvalue
        self.rankname = rankname

    def __lt__(self, other):
        return self.rankvalue < other.rankvalue
    
    def __gt__(self, other):
        return self.rankvalue > other.rankvalue
    
    def __eq__(self, other):
        return self.rankvalue == other.rankvalue
    
    def __str__(self):
        return self.rankname + " of " + self.suit