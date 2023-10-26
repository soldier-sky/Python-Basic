# Example program to understand multiple inheritance in python

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

class HybridMutant(Wizard, Archer):
    """ Since we've inherited Wizard first and Archer later,
    in the absence of constructor, calling HybridMutant with 2 param 
    will invoke base class Wizard constructor/init function.
    To properly initialize base classes, use below approch
    """
    def __init__(self,name, power, arrows):
        Archer.__init__(self, name, arrows)
        Wizard.__init__(self, name, power)


wizard1 = Wizard("demon", 100)
archer1 = Archer("Robin Hood", 130)

hm1 = HybridMutant("Logan",180, 30)

hm1.attack()   # since inheratance chain have Wizard first and the Archer, Wizard.attack() is called
hm1.sign_in()
print(hm1.num_arrows)

# Understanding MRO - Method Resolution Order

class A:
    num = 11

class B(A):
    pass

class C(A):
    num = 110

class D(B,C):
    pass

d = D
print(d.num)       # 110: Since closest resolution order is Class C due to nature of multiple inheritance hierarchy
print(d.mro())     # [<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]
