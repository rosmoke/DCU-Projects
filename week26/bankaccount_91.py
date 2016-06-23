i = 0
class BankAccount(object):
	def __init__(self, surname, forename, balance, account_number=0):
		global i
		self.forename = forename
		self.surname = surname
		self.balance = balance
		self.next_account_number = 16555232 + i
		self.account_number = self.next_account_number
		i = i + 1
		
	def lodge(self, amount):
		self.balance += amount
	def __str__(self):
		pass
class CurrentAccount(BankAccount):
	account_type = "current"
	def withdraw(self, amount):
		overdraft = -1000
		if self.balance - amount < overdraft:
			print("Insufficient funds available")
		else:
			self.balance -= amount
	def __str__(self):
		return("Name: {0} {1}\nAccount number: {2}\nBalance: {3:.2f}\nAccount type: {4}".format(self.surname, self.forename, self.account_number, self.balance, self.account_type))
class SavingsAccount(BankAccount):
	account_type = "savings"
	def apply_interest(self):
		interest_rate = 1.01
		self.balance *= interest_rate
	def withdraw(self, amount):
		if (self.balance - amount) < 0:
			print("Insufficient funds available")
		else:
			self.balance -= amount
	def __str__(self):
		return("Name: {0} {1}\nAccount number: {2}\nBalance: {3:.2f}\nAccount type: {4}".format(self.surname, self.forename, self.account_number, self.balance, self.account_type))