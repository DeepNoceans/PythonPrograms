# Huston and Mohamad
# March 5, 2021
# This is a program to organize doctors with different salaries, professions, ages, and names
# You will be able to see Doctors' name, profession, age, and salary. You
class Doctor(object):

    #class attribute
    total = 0

    def __init__(self, name, salary, prof, age):
        """Huston and Mohamad, this is the constructor that initializes all the attributes"""
        self.__salary = salary
        self.name = name
        self.prof = prof
        self.age = age
        Doctor.total += 1

    def __str__(self):
        """Huston and Mohamad, prints out everything of objects"""
        rep = ""
        rep += "\nName: "
        rep += self.name
        rep += "\nSalary: "
        rep += str(self.__salary)
        rep += "\nMedical profession: "
        rep += self.prof
        rep += "\nAge: "
        rep += str(self.age)
        return rep

    def change_prof(self):
        """Huston and Mohamad, Doctor will change profession"""
        this_is_counter = True
        print(self.name, "is changing his profession.")
        print("""
        [1] Surgeon
        [2] Neurologist
        [3] Physician

        
        """)
        while this_is_counter == True:
            try:
                change_to = int(input("Which one will he change to?: "))
            except ValueError:
                print("try again")
            else:
                this_is_counter = False
                if change_to == 1:
                    self.prof = "Surgeon"
                elif change_to == 2:
                    self.prof = "Neurologist"
                elif change_to == 3:
                    self.prof = "Physician"
                else:
                    print("wrong input")

    @staticmethod
    def what_is_total():
        """Huston and Mohamad, prints out total number of doctors that have been instantiated"""
        print("\nTotal amount of Doctors that were instantiated:", Doctor.total)

    def __increase_salary(self):
        """Huston and Mohamad, access the salary and increasing by a 5% raise!"""
        new_sal = self.__salary * 1.05

        return new_sal

    def get_raise(self):
        """Huston and Mohamad, access a private method to increase salary of a doctor"""
        print("\nOk", self.name, "I will give you a pay raise")
        self.__salary = self.__increase_salary()
        self.print_sal()

    def print_sal(self):
        """Huston and Mohamad, print out a Doctor's salary"""
        print(self.name, ", your salary is now:", self.__salary)

    @property
    def salary(self):
        """Huston and Mohamad, property for completely changing Doctor's salary"""
        return self.__salary

    @salary.setter
    def brand_new_sal(self, different_sal):
        """Huston and Mohamad, this allows the boss to change the salary of doctor and prints it out"""
        print(f"\n{self.name}'s boss decided to completely change his salary.")
        self.__salary = different_sal


def main():
    """Huston and Mohamad, this is the main where all the action happens"""
    print("""
    ----------------------------------
    Welcome to the Paid Doctor Program
    ----------------------------------
    """)

    MD1 = Doctor("Dan", 90000.0, "Surgeon", 45)
    MD2 = Doctor("Bob", 80000.0, "Neurologist", 36)
    MD3 = Doctor("Joe", 60000.0, "Physician", 27)

    print(MD1)
    print(MD2)
    print(MD3)

    Doctor.what_is_total()

    MD1.get_raise()
    MD3.get_raise()

    MD2.brand_new_sal = 20000.0

    MD2.print_sal()

    input("\n\nPress the enter key to go to the next method...\n")

    MD2.change_prof()

    print(MD2)


main()


input("\n\nPress the enter key to exit.")
