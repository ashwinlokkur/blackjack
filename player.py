class Player:
    __name = None
    __balance = None
    __cards = None
    __cards_value = None
    __ace_present = None

    def __init__(self, name, balance):
        self.__name = name
        self.__balance = balance
        self.__cards = []
    
    def __str__(self):
        return self.__name + " has a balance  of  " + str(self.__balance)
    
    def bet(self, money):
        if money < self.__balance:
            return
        else:
            self.__balance -= money
    
    def won(self, money):
         self.__balance -+ money

    def gets_card(self, cards):
        for c in cards:
            self.__cards.append(c)
            if c.get_rank() == "Ace":
                self.__ace_present = True
    
    # def display_cards(self):
    #     for c in self.__cards:
    #         print(c)

    def get_balance(self):
        return self.__balance

    def calc_card_value(self):
        self.__cards_value = [0]
        for c in self.__cards:
            self.__cards_value[0] += c.get_value()
        
        if self.__ace_present:
            self.__cards_value = [self.__cards_value[0], self.__cards_value[0] - 10]

    def get_card_value(self):
        return self.__cards_value

    def remove_value(self, n):
        self.__cards_value.remove(n)
    
    def new_hand(self):
        self.__cards = []
        self.__ace_present = False
    
    def get_cards(self):
        return self.__cards
    
    def visualize_cards(self):
        lines = [[],[],[],[],[],[],[]]
        for c in self.__cards:
            rank = c.get_rank()
            suit_symbol = c.get_suit_symbol()
            space = ' '
            if rank == 10:
                space = ''
            elif type(rank) is str:
                rank = rank[0]
            lines[0].append('┌─────────┐')
            lines[1].append('│{}{}       │'.format(rank, space))
            lines[2].append('│         │')
            lines[3].append('│    {}    │'.format(suit_symbol))
            lines[4].append('│         │')
            lines[5].append('│       {}{}│'.format(space, rank))
            lines[6].append('└─────────┘')
        return lines
    
    def display_cards(self):
        lines = self.visualize_cards()    
        for i in lines:
            for j in i:
                print(j, end='')
            print()