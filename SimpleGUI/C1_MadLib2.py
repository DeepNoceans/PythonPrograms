# Mad Lib 2

# Write your own version of the MadLib program
# using a different arrangement of widgets as well as
# a different story line.

from tkinter import *


class Application(Frame):
    """ GUI application that creates a story based on user input. """

    def __init__(self, master):
        """ Initialize Frame. """
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()
        
        self.config(bg="#f2eecb")


    def create_widgets(self):
        """ Create widgets to get story information and to display story. """
        # create instruction label
        Label(self,
              text="A Brave Knight for a Selfish King",
              font=("Segoe Script", 15),
              bg="#f2eecb"
              ).grid(row=0, column=0, columnspan=5, sticky=W)


        # create a label and text entry for the name of a person
        Label(self,
              text="Knight's Name: ",
              font=("Times New Roman", 10, "bold"),

              bg="#f2eecb"
              ).grid(row=1, column=0, sticky=W)
        self.person_ent = Entry(self)
        self.person_ent.grid(row=1, column=1, sticky=W)

        # create a label and text entry for a plural noun
        Label(self,
              text="An evil animal: ",
              font=("Times New Roman", 10, "bold"),

              bg="#f2eecb"
              ).grid(row=2, column=0, sticky=W)
        self.noun_ent = Entry(self)
        self.noun_ent.grid(row=2, column=1, sticky=W)

        # create a label and text entry for a verb
        Label(self,
              text="Action Verb: ",
              font=("Times New Roman", 10, "bold"),

              bg="#f2eecb"
              ).grid(row=3, column=0, sticky=W)
        self.verb_ent = Entry(self)
        self.verb_ent.grid(row=3, column=1, sticky=W)

        # create a label for adjectives check buttons
        Label(self,
              text="Adjective(s):",
              font=("Times New Roman", 10, "bold"),

              bg="#f2eecb"
              ).grid(row=4, column=0, sticky=W)

        # create strong check button
        self.is_strong = BooleanVar()
        Checkbutton(self,
                    text="strong",
                    font=("Times New Roman", 10, "bold"),

                    variable=self.is_strong,
                    bg="#f2eecb"
                    ).grid(row=4, column=1, sticky=W)

        self.is_chivalrous = BooleanVar()
        Checkbutton(self,
                    text="chivalrous",
                    font=("Times New Roman", 10, "bold"),

                    variable=self.is_chivalrous,
                    bg="#f2eecb"
                    ).grid(row=5, column=1, sticky=W)

        # create superior check button
        self.is_superior = BooleanVar()
        Checkbutton(self,
                    text="superior",
                    font=("Times New Roman", 10, "bold"),

                    variable=self.is_superior,
                    bg="#f2eecb"
                    ).grid(row=6, column=1, sticky=W)

        # create confident check button
        self.is_confident = BooleanVar()
        Checkbutton(self,
                    text="confident",
                    font=("Times New Roman", 10, "bold"),

                    variable=self.is_confident,
                    bg="#f2eecb"
                    ).grid(row=7, column=1, sticky=W)

        # create a label for body parts radio buttons
        Label(self,
              text="Weapon:",
              font=("Times New Roman", 10, "bold"),

              bg="#f2eecb"
              ).grid(row=9, column=0, sticky=W)

        # create variable for single, body part
        self.weapon = StringVar()
        self.weapon.set(None)

        # create body part radio buttons
        weapons = ["sword", "spear", "chainsaw"]
        row = 9
        for part in weapons:
            Radiobutton(self,
                        text=part,
                        font=("Times New Roman", 10, "bold"),

                        variable=self.weapon,
                        value=part,
                        bg="#f2eecb"
                        ).grid(row=row, column=1, sticky=W)
            row += 1

        # create a submit button
        Button(self,
               text="Click for story",
               font=("Times New Roman", 10, "bold"),
               command=self.tell_story,
               bg="#cfb53b"
               ).grid(row=11, column=0, sticky=S)

        self.story_txt = Text(self, width=20, height=37, wrap=WORD)
        self.story_txt.grid(row=1,column=4,rowspan=11)

   

    def tell_story(self):
        """ Fill text box with new story based on user input. """
        # get values from the GUI
        person = self.person_ent.get()
        noun = self.noun_ent.get()
        verb = self.verb_ent.get()
        adjectives = ""
        if self.is_strong.get():
            adjectives += "strong, "
        if self.is_chivalrous.get():
            adjectives += "chivalrous, "
        if self.is_superior.get():
            adjectives += "superior, "
        if self.is_confident.get():
            adjectives += "confident, "
        weapon = self.weapon.get()

        # create the story
        story = person
        story += " the brave knight"
        story += " had nearly given up a life-long quest for the king to find and eradicate the evil "
        story += noun.title()
        story += " that trampled the king's flowers. However, one day, the "
        story += noun
        story += " ran into "
        story += person + ". "
        story += "A surprised, "
        story += adjectives
        story += "yet worried feeling overwhelmed the brave knight. "
        story += "After all this time, they had found the king's biggest enemies. "
        story += person + "'s "
        story += weapon + " gleamed in the sun as they approached the " + noun
        story += "And then, the "
        story += noun
        story += " were eradicated by "
        story += person + " in honor of the king. "
        story += "The moral of the story? Be careful when you "
        story += verb
        story += " with the king, for you may get on his bad side.\nLong live the king!"

        # display the story
        self.story_txt.delete(0.0, END)
        self.story_txt.insert(0.0, story)


# main
root = Tk()
root.title("Mad Lib 2")

app = Application(root)
root.mainloop()
