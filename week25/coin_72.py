import random
class Coin(object):
	def __init__(self,sideup="Heads"):
		self.sideup = sideup
	def flip(self):
		options = ["Heads", "Tails"]
		self.sideup = random.choice(options)
	def getstate(self):
		print(self.sideup)
	def __str__(self):
		return("Current state : {}".format(self.sideup))