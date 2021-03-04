# Blackjack
# From 1 to 7 players compete against a dealer

import cards, games, random    

class BJ_Card(cards.Card):
    """ A Blackjack Card. """
    ACE_VALUE = 1

    @property
    def value(self):
        if self.is_face_up:
            v = BJ_Card.RANKS.index(self.rank) + 1
            if v > 10:
                v = 10
        else:
            v = None
        return v

class BJ_Deck(cards.Deck):
    """ A Blackjack Deck. """
    def populate(self):
        for suit in BJ_Card.SUITS: 
            for rank in BJ_Card.RANKS: 
                self.cards.append(BJ_Card(rank, suit))


# class Hand(object):
#  """ A hand of playing cards. """

#  def __init__(self):
        
class BJ_Hand(cards.Hand):
    """ A Blackjack Hand. """
    def __init__(self, name, wallet, result):
        super(BJ_Hand, self).__init__()
        self.name = name
        self.wallet = wallet
        self.result = result

    def __str__(self):
        rep = self.name + ":\t" + super(BJ_Hand, self).__str__()  
        if self.total:
            rep += "(" + str(self.total) + ")"        
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

        # determine if hand contains an Ace
        contains_ace = False
        for card in self.cards:
            if card.value == BJ_Card.ACE_VALUE:
                contains_ace = True
                
        # if hand contains Ace and total is low enough, treat Ace as 11
        if contains_ace and t <= 11:
            # add only 10 since we've already added 1 for the Ace
            t += 10   
                
        return t
    def is_busted(self):
        return self.total > 21
    def ran_out(self):
        return "F"
    def bankrupt(self):
        self.player.wallet = 0
class BJ_Player(BJ_Hand):
    """ A Blackjack Player. """


    def is_hitting(self):
        response = games.ask_yes_no("\n" + self.name + ", do you want a hit? (Y/N): ")
        return response == "y"



    def bust(self):
        print(self.name, "busts.")
        self.result = "Pending"
        self.lose()

    def lose(self):
        print(self.name, "loses. You lost your share of the prize pool!")
        self.result = "L"
    def win(self):
        print(self.name, "wins! Let it rain $$$!")

        self.result = "W"

    def push(self, result):
        print(self.name, "pushes. The bet is shared!")
        self.result = "W"
        
class BJ_Dealer(BJ_Hand):
    """ A Blackjack Dealer. """
    def is_hitting(self):
        return self.total < 17

    def bust(self):
        print(self.name, "busts.")

    def flip_first_card(self):
        first_card = self.cards[0]
        first_card.flip()


class BJ_Game(object):
    """ A Blackjack Game. """
    def __init__(self, names):      
        self.players = []
        for name in names:
            player = BJ_Player(name, 2000, "None")
            self.players.append(player)
        self.name = name
        self.dealer = BJ_Dealer("Dealer", 999999999, "None")

        self.dealer.bet_amount = ((random.randint(100, 2000))//100)*100
        #self.dealer.wallet = 2000
        for self.player in self.players:
            self.player.wallet = 2000


        self.deck = BJ_Deck()
        self.deck.populate()
        self.deck.shuffle()
    def total_initiate(self):
        rep = 0
        rep += self.dealer.bet_amount
        return rep

    def DigIn(self):
        print(f"\nThe Dealer is betting ${self.dealer.bet_amount}!")
        self.total_bets = self.total_initiate()

        for self.player in self.players:
            y = True
            while y == True:
                try:
                    self.bet_amount = int(input(f"{self.player.name}, how much money you wanna bet?: $"))
                except ValueError:
                    print("\nTry again!\n")
                else:
                    if self.bet_amount < 1 or self.bet_amount > self.player.wallet:
                        print("\nYou cannot bet such a quantity! Try again.\n")
                
                    else:
                        print(f"{self.player.name} is betting ${self.bet_amount}!")
                        self.player.wallet -= self.bet_amount


                        self.total_bets += self.bet_amount
                        print(f"{self.player.name} has ${self.player.wallet} left.\n")

                        y = False
        # for player in self.players:

        #     self.player.wallet -= self.bet_amount


        print(f"Total prize pool is a grand total of ${self.total_bets}!\n\n")
    def payout(self):
        for self.player in self.players:
            print(self.name, self.player.result)

   
    @property
    def still_playing(self):
        sp = []
        for player in self.players:
            if not player.is_busted() and not player.bankrupt():
                sp.append(player)
        return sp

    def __additional_cards(self, player):
        while not player.is_busted() and player.is_hitting():
            self.deck.deal([player])
            print(player)
            if player.is_busted():
                print(self.player.result)
                self.player.result = "Pending"
                player.bust()
           
    def play(self):
        winners = 0
        # deal initial 2 cards to everyone
        print(f"\nThe Dealer has: ${self.dealer.wallet}")
        for self.player in self.players:
            print(f"{self.player.name} has: ${self.player.wallet}")

        self.DigIn() 

        self.deck.deal(self.players + [self.dealer], per_hand = 2)
        self.dealer.flip_first_card()    # hide dealer's first card
        for player in self.players:
            print(player)
            self.player.result = "Pending"
        print(self.dealer)

        # deal additional cards to players
        for player in self.players:
            self.__additional_cards(player)

        self.dealer.flip_first_card()    # reveal dealer's first 

        if not self.still_playing:
            # since all players have busted, just show the dealer's hand
            print(self.dealer)
        else:
            # deal additional cards to dealer
            print(self.dealer)
            self.__additional_cards(self.dealer)

            if self.dealer.is_busted():
                # everyone still playing wins
                for player in self.still_playing:
                    player.win()
            else:
                # compare each player still playing to dealer
                for player in self.still_playing:
                    if player.total > self.dealer.total:
                        player.win()
                    elif player.total < self.dealer.total:
                        player.lose()
                    else:
                        player.push()
            # for self.player in self.players:
            #     if self.player.wallet == 0:
            #         self.players -= self.player
            #         print(self.players)
            winners = 0
            for self.player in self.players:
                if self.player.result == "W":
                    winners += 1

            for self.player in self.players:
                if self.player.result == "W":
                    self.player.wallet += (self.total_bets // winners)

            for self.player in self.players:
                if self.player.wallet <= 0:
                    self.player.result = "F"

      
        # remove everyone's cards
        for player in self.players:
            player.clear()
        self.dealer.clear()
        

def main():
    print("\n\n\t\tWelcome to Blackjack!\n")
    print("""
    The dealer is super rich. They put in money\ninto the prize pool but don't take any out.\n
    Players start with $2000.
    """)
    names = []
    thisisgood = 1

    while thisisgood != 0:
        try:
            number = games.ask_number("How many players? (1 - 7): ", low = 1,  high = 8) 

        except ValueError:
            print("\nThat is not a valid number of players!\n")
        else: 
            thisisgood = 0
    for i in range(number):
        name = input("Enter player name: ")
        names.append(name)
    # print("\nEvery player starts with $2000.\n")
    
    game = BJ_Game(names)

    again = None
    while again != "n":
        game.play()
        again = games.ask_yes_no("\nDo you want to play again?: ")


main()
input("\n\nPress the enter key to exit.")
