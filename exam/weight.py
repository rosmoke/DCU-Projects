class Weight(object):

	OUNCES_PER_POUND = 16

	def __init__(self, pounds=0,ounces=0):
		self.ounces = ounces
		self.pounds = pounds

	def to_ounces(self):
		ounces = self.ouncesounces +=self.pounds * self.OUNCES_PER_POUND
		return(ounces)

	def __eq__(self, other):
		return(self.to_ounces() == other.to_ounces())

	def __gt__(self, other):
		return(self.to_ounces() > other.to_ounces())

	def __ge__(self, other):
		return(self.to_ounces() >= other.to_ounces())

	def __add__(self, other):
		return(from_ounces(self.to_ounces() + other.to_ounces()))

	def __iadd__(self, other):
		z = self + other
		self.pounds = z.pounds
		self.ounces = z.ounces
		return(self)

	@classmethod
	def from_ounces(cls, total_ounces):
		pounds, ounces = divmod(total_ounces, cls.OUNCES_PER_POUND)
		return(cls(pounds,ounces))