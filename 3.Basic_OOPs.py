# Basic python OOP

class Point:
	def __init__(self, x):
		self._x=x
		self._y=0
		self._z=0
		self.__p__=0   #private 
	def x(self):
		return self._x
	def y(self):
		return self._y
	def z(self):
		return self._z
	def set_p(self, val):
		self.__p__=val
	def get_p(self):
		return self.__p__

class Point2d(Point):
	def __init__(self, x, y):
		super().__init__(x)
		self._y=y
	def y(self):
		return self._y
	def print_p(self):
		print(f"value of p is {super().get_p()}")


p1=Point(3)
p2=Point2d(33,44)

print(f"p1.x: {p1.x()} and p1.y: {p1.y()}")
print(f"p2.x: {p2.x()} and p2.y: {p2.y()}")
p2.set_p(11)
p2.print_p()