import sys
class House(object):
   def __init__(self, address, value, bedrooms, garden):
      self.address = address
      self.value = int(value)
      self.bedrooms = bedrooms
      self.garden = garden

   def getValueRange(self):
      if self.value < 200000:
         return 0
      if 200000 < self.value and self.value < 349999:
         return 1
      if 350000 < self.value and self.value < 499999:
         return 2
      if self.value >= 500000:
         return 3

   def isComparableValue(self, other):
      return(bool(self.getValueRange() == other.getValueRange()))

   def __str__(self):
      return(self.address, self.value, self.bedrooms, self.garden)

lines = sys.stdin.read().splitlines()

names = []
details = lines[0].split(",")
a = House(details[0],details[1],details[2],details[3])
names.append(details[0])

details = lines[1].split(",")
b = House(details[0],details[1],details[2],details[3])
names.append(details[0])

print(a.isComparableValue(b))