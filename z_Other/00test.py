class Robot(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        rep = ""
        rep += "Name =", self.name
        rep += "\nColor =", self.color
    
    def change_color(self):
        colors = ["Blue", "Red", "Green"]
        self.color = random.choice(colors)

class VacuumRobot(Robot):
    def __init__(self, name, color, battery_percent):
        super().__init__(name)
        self.color = color
        self.battery_percent = battery_percent 

    def __str__(self):
        rep = super().__str__(), + "\nBattery Percentage:", battery_percent

vrob1 = VacuumRobot("Clean_Bob", "Black", 100)

print(vrob1)
