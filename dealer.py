from player import Player
class Dealer(Player):

    __hidden_cards = []
    __balance = 0
    __cards_value_with_hidden = None
    __hidden_ace_present = None
    def __init__(self):
        Player.__init__(self, "Dealer", 0)    
    
    def gets_hole_card(self, card):
        for c in card:
            self.__hidden_cards.append(c)
            if c.get_rank() == "Ace":
                self.__hidden_ace_present = True
    
    def bet(self):
        pass

    def calc_card_value(self):
        Player.calc_card_value(self)
        self.__cards_value_with_hidden = Player.get_card_value(self)
        
        for c in self.__hidden_cards:
            if len(self.__cards_value_with_hidden) == 1:
                self.__cards_value_with_hidden[0] += c.get_value()
            elif len(self.__cards_value_with_hidden) >= 2:
                for v in range(len(self.__cards_value_with_hidden)):
                    self.__cards_value_with_hidden[v] += c.get_value()
        temp = []
        if self.__hidden_ace_present:
            for v in self.__cards_value_with_hidden:
                temp.append(v)
                temp.append(v-10)
    
    def get_card_value(self):
        return self.__cards_value_with_hidden

    def new_hand(self):
        Player.new_hand(self)
        self.__hidden_cards = []
        self.__hidden_ace_present = False
    
    def display_cards(self, display_hole_cards):
        lines = [[],[],[],[],[],[],[]]
        for c in self.__hidden_cards:
            if not display_hole_cards:
                lines = [['┌─────────┐'], ['│░░░░░░░░░│'], ['│░░░░░░░░░│'], ['│░░░░░░░░░│'], ['│░░░░░░░░░│'], ['│░░░░░░░░░│'], ['└─────────┘']]

            else:
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
            
            temp = Player.visualize_cards(self)
            for i in range(len(temp)):
                # lines[i].append(temp[i])
                for j in temp[i]:
                    lines[i].append(j)
            for i in lines:
                for j in i:
                    print(j, end='')
                print()
