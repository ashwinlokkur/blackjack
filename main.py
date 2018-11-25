from player import Player
from deck import Deck
from dealer import Dealer
import pickle 


FILE_NAME = "players.dat"

players = []
deck = None
player = None
dealer = None

def get_old_players():
    global players
    infile = open(FILE_NAME, "rb")
    l = ''
    try:
        l = pickle.load(infile)
    except EOFError:
        players = []
        return
    while True:
        try:
            players.append(l)
            l = pickle.load(infile)
        except EOFError:
            break
    
def write_new_players(player_name, player_balance):
    outfile = open(FILE_NAME, "ab")
    p = {}
    p['name'] = player_name
    p['balance'] = player_balance
    pickle.dump(p, outfile)
    outfile.close()

def search_player(name):
    for p in players:
        if name == p['name']:
            return p
    return None

def start_round():
    global player
    global dealer

    player.new_hand()
    dealer.new_hand()

    player.gets_card(deck.deal(2))
    dealer.gets_hole_card(deck.deal(1))
    dealer.gets_card(deck.deal(1))

def display_table(dealer_hole_display = False):
    print("---------------")
    print("Player Cards")
    print("---------------")
    # player.display_cards()
    player.display_cards()
    print("\n---------------")
    print("Dealer Cards")
    print("---------------")
    # dealer.display_cards(dealer_hole_display)
    dealer.display_cards(dealer_hole_display)
    print("---------------")

def player_turn():
    global player
    display_table()

    while(True):
        player.calc_card_value()

        if len(player.get_card_value()) == 2 and player.get_card_value()[0] > 21:
            player.remove_value(player.get_card_value()[0])
        elif len(player.get_card_value()) == 2 and player.get_card_value()[1] > 21:
            player.remove_value(player.get_card_value()[1])

        if len(player.get_card_value()) == 1 and player.get_card_value()[0] > 21:
            return ("BUST", player.get_card_value())
        elif len(player.get_card_value()) == 2 and 21 in player.get_card_value():
            return ("BLACKJACK", player.get_card_value())
        
        ch = input("Hit or Stand? Press H or S: ")

        if ch.upper() == 'H':
            player.gets_card(deck.deal(1))
            player.calc_card_value()
        elif ch.upper() == 'S':
            return ("STAND", player.get_card_value())
        else:
            print("Invalid input. Please retry")
            continue
            
        display_table()
        
    return None

def dealer_turn():
    global dealer
    display_table(dealer_hole_display = True)
    while(True):

        dealer.calc_card_value()

        if len(dealer.get_card_value()) == 1 and dealer.get_card_value()[0] > 21:
            return("BUST",dealer.get_card_value())
        elif dealer.get_card_value() > player.get_card_value():
            return ("STAND", dealer.get_card_value())
        elif len(dealer.get_card_value()) == 1 and dealer.get_card_value()[0] < 17:
            pass
        elif len(dealer.get_card_value()) == 1 and dealer.get_card_value()[0] >= 17 and dealer.get_card_value()[0] < 21 :
            return ("STAND", dealer.get_card_value())
        elif 21 in dealer.get_card_value():
            return ("BLACKJACK", dealer.get_card_value())
        
        if len(dealer.get_card_value()) > 1 :
            for c in dealer.get_card_value():
                if c > 21:
                    dealer.remove_value(c)

        dealer.gets_card(deck.deal(1))
        dealer.calc_card_value()
            
        
        display_table(dealer_hole_display = True)
        
def check_win(p, d):
    if p[0] == "STAND" and d[0] == "STAND":
        if p[1] > d[1]:
            print("PLAYER WON")
        elif p[1] < d[1]:
            print("DEALER WON")
        else:
            print("DRAW")

def start_game():
    global deck
    global player
    global dealer
    deck = Deck()
    while(True):
        deck.shuffle()
        start_round()

        p = player_turn()
        
        if p[0] == "BUST":
            print("DEALER WON!")
            continue
        elif p[0] == "BLACKJACK":
            print("PLAYER WON!")
            continue
        d = dealer_turn()
        
        if d[0] == "BUST":
            print("PLAYER WON!")
            continue
        elif d[0] == "BLACKJACK":
            print("DEALER WON!")
            continue
    
        check_win(p, d)    
        
    
def main():
    global player
    global dealer

    name = input("Enter your name: ")
    get_old_players()
    player_found = search_player(name)

    player = None

    if player_found is not None:
        print("Welcome back, "+name)
        print("You have a balance of "+str(player_found['balance']))
        player = Player(player_found['name'],player_found['balance'])
    else:
        temp = {}
        b = int(input("Balance: "))
        temp['name'] = name
        temp['balance'] = b
        players.append(temp)
        player = Player(name,b)
    
    dealer = Dealer()

    start_game()   
    write_new_players(name, player.get_balance())
main()