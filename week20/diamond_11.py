import sys
number = int(sys.argv[1])

x = "* "
i = 1
while i <= number:
	print((number-i) * " " + x * i)
	i = i + 1
i = number-1
while i > 0:
	print((number-i) * " " + x * i)
	i = i - 1