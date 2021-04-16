from tkinter import *

class Application(Frame):
    def __init__(self, master):
        """ Initialize Frame. """
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):

        Label(self,
            text = "Chipotle Menu",
            font = ("Times New Roman", 20)
            ).grid(row = 0, column = 0, columnspan = 4, sticky = N)

        Label(self,
              text="This Order is for: ",
              font = ("Times New Roman", 15)
              ).grid(row=1, column=0, sticky=W)
        self.person_ent = Entry(self)
        self.person_ent.grid(row=1, column=1, sticky=W)

        # create variable for single, body part
        
        

        Label(self,
              text="\nMeals:",
              font=("Times New Roman", 15)
              ).grid(row=3, column=0, columnspan=4, sticky=W)

        self.meal_type = StringVar()
        self.meal_type.set(None)

        meal_types = ["Burrito", "Burrito Bowl", "Tacos", "Salad"]
        row = 4
        for meal in meal_types:
            Radiobutton(self,
                        text=meal,
                        variable=self.meal_type,
                        value=meal
                        ).grid(row=row, column=0, sticky=W)
            row += 1   

        Label(self,
              text="\nProtein/Veggie:",
              font=("Times New Roman", 15)
              ).grid(row=8, column=0, sticky=W)

       

        self.chicken = DoubleVar()
        self.chicken.set(0)

        Radiobutton(self,
                    text="Chicken ($7.35)",
                    variable=self.chicken,
                    value=7.35
                    ).grid(row=9, column=0, sticky=W)

        self.steak = DoubleVar()
        self.steak.set(0)

        Radiobutton(self,
                    text="Steak ($8.35)",
                    variable=self.steak,
                    value=8.35
                    ).grid(row=10, column=0, sticky=W)

        self.veggie = DoubleVar()
        self.veggie.set(0)

        Radiobutton(self,
                    text="Veggie ($7.35)",
                    variable=self.veggie,
                    value=7.35
                    ).grid(row=11, column=0, sticky=W)

        self.rice = StringVar()
        self.rice.set(None)

        Label(self,
              text="\nRice:",
              font=("Times New Roman", 15)
              ).grid(row=12, column=0, sticky=W)

        rice_types = ["White Rice", "Brown Rice", "No Rice"]
        row = 13
        for rice in rice_types:
            Radiobutton(self,
                        text=rice,
                        variable=self.rice,
                        value=rice
                        ).grid(row=row, column=0, sticky=W)
            row += 1

        Label(self,
              text="\nToppings:",
              font=("Times New Roman", 15)
              ).grid(row=16, column=0, sticky=W)
                    
        self.guac = BooleanVar()
        Checkbutton(self,
                    text="Guacamole ($2.25)",
                    variable=self.guac
                    ).grid(row=17, column=0, sticky=W)

        # create joyous check button
        self.tomato = BooleanVar()
        Checkbutton(self,
                    text="Tomato Salsa",
                    variable=self.tomato
                    ).grid(row=18, column=0, sticky=W)

        # create electric check button
        self.corn = BooleanVar()
        Checkbutton(self,
                    text="Chili-Corn Salsa",
                    variable=self.corn
                    ).grid(row=19, column=0, sticky=W)

        self.s_cream = BooleanVar()
        Checkbutton(self,
                    text="Sour Cream",
                    variable=self.s_cream
                    ).grid(row=20, column=0, sticky=W)
                    
        self.lett = BooleanVar()
        Checkbutton(self,
                    text="Lettuce",
                    variable=self.lett
                    ).grid(row=21, column=0, sticky=W)


        self.cheese = BooleanVar()
        Checkbutton(self,
                    text="Cheese",
                    variable=self.cheese
                    ).grid(row=22, column=0, sticky=W)
        
        self.g_sal = BooleanVar()
        Checkbutton(self,
                    text="Green Chili Salsa",
                    variable=self.g_sal
                    ).grid(row=23, column=0, sticky=W)

        self.r_sal = BooleanVar()
        Checkbutton(self,
                    text="Red Chili Salsa",
                    variable=self.r_sal
                    ).grid(row=24, column=0, sticky=W)

        Label(self,
              text="\nSides:",
              font=("Times New Roman", 15)
              ).grid(row=25, column=0, sticky=W)

        self.chips = BooleanVar()
        Checkbutton(self,
                    text="Chips ($1.50)",
                    variable=self.chips
                    ).grid(row=26, column=0, sticky=W)

        self.guac_side = BooleanVar()
        Checkbutton(self,
                    text="Side of Guacamole ($2.25)",
                    variable=self.guac_side
                    ).grid(row=27, column=0, sticky=W)

        self.drink = BooleanVar()
        Checkbutton(self,
                    text="Fountain Drink ($2.40)",
                    variable=self.drink
                    ).grid(row=28, column=0, sticky=W)
    
        Button(self,
               text = "Place Order",
               command = self.receipt
               ).grid(row = 29, column = 0, sticky = W)

        self.receipt_txt = Text(self, width = 40, height = 10, wrap = WORD)
        self.receipt_txt.grid(row = 30, column = 0, columnspan = 4)

    def receipt(self):
        price = 0
        """ Fill text box with new receipt based on user input. """
        # get values from the GUI
        person = self.person_ent.get()

        if self.guac.get():
            price += 2.25
        if self.guac_side.get():
            price += 2.25
        if self.drink.get():
            price += 2.40
        if self.chips.get():
            price += 1.50
        if self.chicken.get():
            price += 7.35
        if self.steak.get():
            price += 8.35
        if self.veggie.get():
            price += 7.35
        # if self.is_joyous.get():
        #     adjectives += "joyous, "
        # if self.is_electric.get():
        #     adjectives += "electric, "
        # body_part = self.body_part.get()
        # create the receipt
        price_string = "{:02.2f}".format(price)

       

        receipt = "Hello " + person + "! Thank you for choosing Chipotle!\n"
        receipt += "The price of your meal is $" + price_string + ".\n"
        
        # display the receipt                                
        self.receipt_txt.delete(0.0, END)
        self.receipt_txt.insert(0.0, receipt)
    # # def final_pay
root = Tk()
root.title("Order Up!")
app = Application(root)
root.mainloop()


#tip!!!!!!!!!!!!!!!!