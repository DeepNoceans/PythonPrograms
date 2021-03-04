#Mohamad Moussaoui
#2/17/2021
#One-card War

import cards, games     

class BJ_Card(cards.Card):
    """ A Blackjack Card. """
    ACE_VALUE = 11

    @property
    def value(self):
        if self.is_face_up:
            v = BJ_Card.RANKS.index(self.rank) + 1
    
        return v
    def instructions():
        print("""
        Ace = 1





        """)
class BJ_Deck(cards.Deck):
    """ A Blackjack Deck. """
    def populate(self):
        for suit in BJ_Card.SUITS: 
            for rank in BJ_Card.RANKS: 
                self.cards.append(BJ_Card(rank, suit))
    

class BJ_Hand(cards.Hand):
    """ A Blackjack Hand. """
    def __init__(self, name):
        super(BJ_Hand, self).__init__()
        self.name = name

    def __str__(self):
        rep = self.name + ":\t" + super(BJ_Hand, self).__str__()  
               
        return rep
  
    @property     
    def total(self):
        # if a card in the hand has value of None, then total is None
        for card in self.cards:
            if not card.value:
                return None
        
        # add up card values, treat each Ace as 1
        t = 0
        for card in self.cards:
              t += card.value                
       
        return t

            

class BJ_Player(BJ_Hand):
    """ A Blackjack Player. """
    def is_hitting(self):
        print("\n")

    def lose(self):
        print(self.name, "loses, Dealer wins.")

    def win(self):
        print(self.name, "wins, Dealer loses.")

    def push(self):
        print(self.name, "and the Dealer tied!")


        
class BJ_Dealer(BJ_Hand):
    """ A Blackjack Dealer. """
    def is_hitting(self):
        return self.total < 17

 
    def flip_first_card(self):
        first_card = self.cards[0]
        first_card.flip()
        #Flip second card
        second_card = self.cards[1]
        second_card.flip()



class BJ_Game(object):
    """ A Blackjack Game. """
    def __init__(self, names):      
        self.players = []
        for name in names:
            player = BJ_Player(name)
            self.players.append(player)

        self.dealer = BJ_Dealer("Dealer")

        self.deck = BJ_Deck()
        self.deck.populate()
        self.deck.shuffle()

    @property
    def still_playing(self):
        sp = []
        for player in self.players:
            sp.append(player)
        return sp

    def __additional_cards(self, player):
        while player.is_hitting():
            self.deck.deal([player])
            print(player)

           
    def play(self):
        # deal initial 2 cards to everyone
        self.deck.deal(self.players + [self.dealer], per_hand = 1)
        #self.dealer.flip_first_card()    # hide dealer's first card
        for player in self.players:

            print(player)
        print(self.dealer)



        if player.total > self.dealer.total:
            player.win()
        elif player.total < self.dealer.total:
            player.lose()
        else:
            player.push()

      
        # remove everyone's cards
        for player in self.players:
            player.clear()
        self.dealer.clear()
        
def main():
    print("\n\n\t\tWelcome to War!\n")
    
    names = []
    #number = games.ask_number("How many players? (1 - 2): ", low = 1, high = 3)
    number = 1
    for i in range(number):
        name = input("Enter player name: ")
        names.append(name)
    print()
        
    game = BJ_Game(names)

    again = None
    round = 0
    while again != "n":
        round += 1
        print(f"-------\nRound {round}\n-------\n")
        game.play()
        again = games.ask_yes_no("\n\nDo you want to play again(Y/N)?: ")



main()
input("\n\nPress the enter key to exit.")
