import random
import itertools
from card import Card
class Deck:

    __suits = ("Diamonds", "Spades", "Clubs", "Hearts")
    __ranks = (2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", "Ace")
    __values = {2:2, 3:3, 4:4, 5:5, 6:6, 7:7,8:8, 9:9, 10:10, "Jack":10, "Queen":10, "King":10, "Ace":11}
    __cards = []
    __cards_in_deck = 0
    
    def __init__(self):
        self.__cards = list(itertools.product(self.__suits,self.__ranks))
        self.__cards_in_deck = len(self.__cards)
        for c in range(self.__cards_in_deck):
            cardObj = Card(self.__cards[c][0], self.__cards[c][1], self.__values[self.__cards[c][1]]) 
            self.__cards[c] = cardObj
        
    def shuffle(self):
        random.shuffle(self.__cards)

    def deal(self, n):
        ret = []
        for i in range(0, n):
            ret.append(self.__cards.pop())
        return ret

    def __str__(self):
        ret = ""
        for c in self.__cards:
            ret = ret + str(c) + "\n"
        return ret     
    
    def reset(self):
        self.__init__()
    
