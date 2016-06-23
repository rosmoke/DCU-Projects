class Customer(object):
	def __init__(self, name, balance, addr1, addr2, addr3):
		self.name = name
		self.balance = balance
		self.addr1 = addr1
		self.addr2 = addr2
		self.addr3 = addr3
		self.discount = 0
	def owes(self):
		total = self.balance - ((self.balance / 100) * self.discount)
		return(total)

	def __str__(self):
		return("{0}"'\n'"{1}"'\n'"{2}"'\n'"{3}"'\n'"Balance: {4:1.2f}"'\n'"Discount: {5}%"'\n'"Amount due: {6:1.2f}".format(self.name, self.addr1, self.addr2, self.addr3, self.balance, self.discount, self.owes()))

class ValuedCustomer(Customer):
	def __init__(self, name, balance, addr1, addr2, addr3):
		super().__init__(name, balance, addr1, addr2, addr3)
		self.discount = 10