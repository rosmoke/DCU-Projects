class Employee(object):
	def __init__(self, name, number, salary = 0.00):
		self.salary = salary
		self.name = name
		self.number = number
	def wages(self):
		return(self.salary)
	def __str__(self):
		return("Name: {0}"'\n'"Number: {1}"'\n' "Wages: {2:1.2f}".format(self.name, self.number, float(self.wages())))

class Manager(Employee):
	def __init__(self, name, number, salary):
		super().__init__(name,number)
		self.salary = salary
	def wages(self):
		return(round(self.salary/52, 2))

class AssemblyWorker(Employee):
	def __init__(self,name, number, hourly_rate, hours):
		self.name = name
		self.number = number
		self.hourly_rate = hourly_rate
		self.hours = hours
	def wages(self):
		return("{0:1.2f}".format(self.hourly_rate * self.hours))