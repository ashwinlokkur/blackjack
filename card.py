class Card:
    __rank = None
    __suit = None
    __value = None

    __suit_symbol = {"Spades" : '♠', "Diamonds" : '♦', "Hearts" : '♥', "Clubs" : '♣'}

    def __init__(self, suit, rank, value):
        self.__rank = rank
        self.__suit = suit
        self.__value = value

    def get_rank(self):
        return self.__rank 
    
    def get_suit(self):
        return self.__suit
    
    def get_value(self):
        return self.__value
    
    def set_value(self, value):
        self.__value = value
    
    def get_suit_symbol(self):
        return self.__suit_symbol[self.__suit]
    
    def __str__(self):
        return str(self.__rank) + " of " + self.__suit