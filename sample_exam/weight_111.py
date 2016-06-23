class Weight(object):
	#every weight has pounds , ounces
	# there are 16 ounces in 1 pound (so max 15 ounces)
	OUNCES_PER_POUND = 16

	def __init__(self, pounds=0, ounces=0):
		self.pounds = pounds
		self.ounces = ounces

	def total(weights):
		return((weights.ounces / Weight.OUNCES_PER_POUND) + weights.pounds)

	def __gt__(self, other):
		return(Weight.total(self) > Weight.total(other))

	def __eq__(self, other):
		return(Weight.total(self) == Weight.total(other))

	def __ge__(self, other):
		return(Weight.total(self) >= Weight.total(other))

	def __add__(self, other):
		total = [self.pounds + other.pounds, self.ounces + other.ounces]
		if total[1] >= 16:
			total[0] = total[0] + 1
			total[1] = total[1] - 16
		return(Weight(total[0], total[1]))

	def __mul__(self, n):
		self.pounds = self.pounds * n
		self.ounces = self.ounces * n
		return(self)
	def __rmul__(self, n):
		total_pounds = self.pounds * n
		total_ounces = self.ounces * n
		return(Weight(total_pounds,total_ounces))

	def __iadd__(self, other):
		z = self + other
		self.pounds = z.pounds
		self.ounces = z.ounces
		return(self)

	def __sub__(self, other):
		return(Weight((self.pounds-other.pounds),(self.ounces-other.ounces)))

	def __isub__(self,sub):
		z = self - sub
		self.pounds = z.pounds
		self.ounces = z.ounces
		return(self)

	def from_ounces(weight):
		pounds = int(weight / 16)
		ounces = weight - (pounds * 16)
		return(Weight(pounds,ounces))

	def __str__(self):
		return("{} pound(s) and {} ounce(s)".format(self.pounds, self.ounces))



