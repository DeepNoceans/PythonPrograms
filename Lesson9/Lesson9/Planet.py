#Planet objects with attributes

#Create a Planet class with attributes name, radius, mass & distance. A constructor
#   and str method should be included. In addition, include the methods getVolume,
# 	getSurfaceArea, and getDensity. 

class Planet(object):
    def __init__ (self, name, radius, mass, distance):
        self.name = name
        self.radius = radius
        self.mass = mass
        self.distance = distance
    
    def __str__ (self):
        rep = ""
        rep += f"\nName: {self.name}kg"
        rep += f"\nRadius: {self.radius}km"
        rep += f"\nMass: {self.mass}"
        rep += f"\nDistance: {self.distance}km"
        return rep

    def getVolume(radius):
        print("This is volume.")

    def getSurfaceArea(radius):
        print("This is surface area")

    def getDensity(mass):
        print("This is denstiy")

 

