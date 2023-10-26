
class Robot:
    """Represent a robot, with a name."""

    # A class variable, counting the number of robots
    population=0

    def __init__(self,name):
        """Initialize the data."""
        self.name=name
        print("(Initializing {})".format(self.name))

        #When this person is created a robot, add to the population
        Robot.population +=1

    def die(self):
        """ I am dying"""
        print("{} is being destroyed".format(self.name))
        
        Robot.population -=1

        if Robot.population == 0:
            print("{} was the last one.".format(self.name))
        else:
            print("There are still {:d} robot working.".format(Robot.population))

    def say_hi(self):
        """Greetings by the robot.
        Yeah, they can do that."""
        print("Greetings, my master call me {}.".format(self.name))

    @classmethod
    def how_many(cls):
        """Prints the current population."""
        print("We have {:d} robot.".format(cls.population))

droid1 =Robot("R2-D2")
droid1.say_hi()

droid2= Robot("C-120")
droid2.say_hi()

Robot.how_many()

print("\n Robots can do some work here.\n")

print("Robots have finished thiere work. So let's destro them...\n")

droid1.die()
droid2.die()

Robot.how_many()

