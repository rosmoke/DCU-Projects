n = input()
base = input()
power = 9


while n < base ** (power - 1):
	power = power - 1
n = n - base ** (power - 1)
print 1
power = power - 1
while n <= base ** (power - 1):
	print 0
	power = power - 1
	print "This is the power: ", power, ", This is the number: ", n
print 1