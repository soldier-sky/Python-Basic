class Player:
    """
    Basics of class and method in python.
    Understanding syntax of classmethod and static method decorator
    """

    NumOfPlayer = 0                  # Class Attribute
    def __init__(self, name, age=18):
        self.name = name             # Object attribute
        self.age = age               # Object attribute
        Player.NumOfPlayer += 1


    def run(self):
        """Method to run the given player"""
        print(f"running player {self.name} with age {self.age}")
        return True


    def player_count(self):
        """ Returns the total count of players"""
        return self.NumOfPlayer        # This syntax too work.


    @classmethod
    def adding_things(cls, num1, num2):
        """ Dummy method to demonstrate class method"""
        return num1+num2


    @classmethod
    def parameterized_constuctor(cls, num1, num2):
        """ example of create parameterized constructor in python"""
        return cls("Dummy", num1+num2)

    @staticmethod
    def adding_things2(num1, num2):
        """ Dummy method to demonstrate static method. Do not have access to cls attributes"""
        return num1+num2

p1 = Player("Sunil", 32)
p1.run()
p2 = Player("Ayaan", 3)
p2.run()
print(p1.name)

print("Number of players ", p1.player_count())
p3 = Player.parameterized_constuctor(3,5)
print("Player 3's age ", p3.age)

print(Player.adding_things2(10,33))   # can be called directly
print(p2.adding_things(10,30))        # can be called via object
