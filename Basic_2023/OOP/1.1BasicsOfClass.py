# example to understand public and private in Python class

class Base:
    def __init__(self, b):
        self.b = b
        self._pri = b         # notation to denote private attribute
    

    def foo(self):
        print(f"inside base class: {self.b},{self._pri}")


bobj = Base(10)
#bobj.foo()
#print(bobj._pri)

#----------------------------------------------------------

class User():
    def sign_in(self):
        print("signed in: User")
    def attack():
        print("Dummy attack")

class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f"attacking with ower of {self.power}")

class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        #User.attack()       #calling base class method while overriding
        print(f"attacking with arrows: {self.num_arrows}")

wizard1 = Wizard("Dr.Strange", 100)
wizard1.attack()

archer1 = Archer("Hawkeye", 70)
archer1.attack()

for character in [wizard1, archer1]:
    character.attack()