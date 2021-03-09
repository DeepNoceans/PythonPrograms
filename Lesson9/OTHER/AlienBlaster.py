#Mohamad Moussaoui

#Alien Blaster
#Demonstrates object interaction


class Player(object):
    """ A player in a shooter game. """

    def blast(self, enemy):
        print("The player blasts an enemy.\n")
        enemy.die()


class Alien(object):
    """ An alien in a shooter game. """

    def die(self):
        print(
            "The alien gasps and says, 'Oh, this is it. This is the  big one. \nYes, it's getting dark now. Tell my 1.6 million larvae  that I loved them... \nGood-bye, cruel universe.'"
        )


# main
print("\n\nDeath of an alien\n")

hero = Player()
invader = Alien()

hero.blast(invader)

#'invader' is argument for 'enemy' in the 'blast' function


input("\n\nPress the enter key to exit.") 

