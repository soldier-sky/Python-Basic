class Player:
    """
    Basics of class and method in python
    """

    NumOfPlayer = 0                  # Class Attribute
    def __init__(self, name):
        self.name = name             # Object attribute
        Player.NumOfPlayer += 1


    def run(self):
        """Method to run the given player"""
        print(f"running {self.name}")
        return True


    def player_count(self):
        """ Returns the total count of players"""
        return self.NumOfPlayer        # This syntax too work.

p1 = Player("Sunil")
p1.run()
p2 = Player("Ayaan")
p2.run()
print(p1.name)

print("Number of players ", p1.player_count())
