class Point(object):
	def __init__(self, x = 0, y = 0):
		self.x = x
		self.y = y
	def distance(self,second):
		self.second = second
		return(abs(self.second - second))
	def __str__(self):
		return("({}, {})".format(self.x,self.y))

class Segment(Point):
	def __init__(self, first, second):
		self.first = first
		self.second = second
	def midpoint(self):
		x1 = int(str(self.first).split(",")[0][1:])
		y1 = int(str(self.first).split(",")[1][:-1])
		x2 = int(str(self.second).split(",")[0][1:])
		y2 = int(str(self.second).split(",")[1][:-1])
		x = (x1 + x2) / 2
		y = (y1 + y2) / 2
		return(x, y)

class Circle(Point):
	def __init__(self, j, k):
		self.j = j
		self.k = k
	def overlaps(self, circle):
		return(str(self.first), self.k)
