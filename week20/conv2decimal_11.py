import sys

number = sys.argv[1]
base = int(sys.argv[2])
sum = 0

if base != 10:
	i = 0
	j = 0
	while i < len(number):
		x = int(number[len(number)-i-1])
		sum += x * (base ** j)
		j = j * 2
		i = i + 1
		if j == 0:
			j += 1
	print(sum)
else:
	print(int(number))