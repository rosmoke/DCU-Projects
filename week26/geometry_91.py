import math
class Point(object):
	def __init__(self, x, y):
		self.x = x
		self.y = y
	def distance(self, other):
		return((math.sqrt((other.x - self.x) ** 2 + (other.y - self.y) ** 2)), [self.x,self.y])

class Shape(object):
	def __init__(self, points):
		self.points = points
	def sides(self):
		side1 = self.points[0].distance(self.points[1])[0]
		side2 = self.points[1].distance(self.points[2])[0]
		if len(self.points) == 3:
			side3 = self.points[2].distance(self.points[0])[0]
			return([side1,side2,side3])
		else:
			side3 = self.points[2].distance(self.points[3])[0]
			side4 = self.points[3].distance(self.points[0])[0]
			return([side1,side2,side3,side4])
	def perimeter(self):
		return(sum(Shape.sides(self)))

class Triangle(Shape):
	def area(self):
		ax = self.points[0].distance(self.points[1])[1][0]
		ay = self.points[0].distance(self.points[1])[1][1]
		bx = self.points[1].distance(self.points[1])[1][0]
		by = self.points[1].distance(self.points[1])[1][1]
		cx = self.points[2].distance(self.points[1])[1][0]
		cy = self.points[2].distance(self.points[1])[1][1]
		return(abs((ax*(by-cy)+bx*(cy-ay)+cx*(ay-by))/2))
class Square(Shape):
	def area(self):
		return(Shape.sides(self)[0] ** 2)



