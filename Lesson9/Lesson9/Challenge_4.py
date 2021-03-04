# Mohamad Moussaoui
# Challenge 4
import random
PLANETS = ["AHCH-TO", "MUSTAFAR", "TATOOINE", "HOTH", "BESPIN", "NABOO", "ENDOR"]


class Player(object):
    def __init__(self, name, loc):
        self.name = name
        self.loc = loc
    def __str__(self):
        rep = ""
        rep += "Player Name: " + self.name
        rep += "\nCurrent Location: " + self.loc 
        return rep
    def spacetravel(self):

        print(f"These are the nearby planets:")
        for i in PLANETS:
            print(i)

class Planet(object):
    def __init__(self, planet):
        self.loc = loc
        self.loc2 = loc2
    
    
    def changeloc():
        print(PLANETS)
        thisisgood = True
        while thisisgood:
            loc2 = input(f"Other than {loc}, pick a planet to explore.").upper()

            if loc2 == loc:
                print("You're already on that planet.")

            elif loc2 not in PLANETS:
                print("That is not an available planet.")
            
            if loc2 in PLANETS:
                print(f"Traveling to {loc2}...")
                thisisgood = False
                loc = loc2

    




def main():
    # Location.printlocs()
    name = input("\nWho is going on an adventure across the galaxy?: ")
    

    print(jedi)

    Planet.changeloc()
    Planet.changeloc()
    Planet.changeloc()
    print("Your ship is out of fuel. Until next time.")


main()

input("\n\nPress the enter key to exit.")
