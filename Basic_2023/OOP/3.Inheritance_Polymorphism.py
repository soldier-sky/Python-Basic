# Example program to understand polymorphism i.e overloading

class User():
    def sign_in(self):
        print('logged in')
    

    def attack(self):
        print('do nothing')


class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power


    def attack(self):
        #User.attack(self)
        print(f"attacking with power of {self.power}")


class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows


    def attack(self):
        print(f"attacking with arrows {self.num_arrows}")


wizard1 = Wizard("demon", 100)
archer1 = Archer("Robin Hood", 130)

print(wizard1.sign_in())
archer1.attack()

print(isinstance(wizard1, User))
print(isinstance(wizard1, Archer))

characters = [wizard1, archer1]

# Polymorphism: Overloaded attack() method
for char in characters:
    char.attack()