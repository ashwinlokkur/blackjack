from Card import card
class Hand():
    __cards = None
    __cards_value = None
    __ace_present = None
    
    def __init__(self, ace_present = False):
        self.__ace_present = ace_present
        self.__cards = []
    def set_ace_present(self, ace_present):
        self.__ace_present = ace_present

    def get_card_value(self):
        for c in self.__cards:
            self.__cards_value += c.get_value()
        
        if self.__ace_present:
            self.__cards_value = [self.__cards_value, self.__cards_value - 10]

        return self.__cards_value
    
    def add_cards(self, cards):
        for c in cards:
            self.__cards.append(c)
            if c.get_rank == "Ace":
                self.__ace_present() = True