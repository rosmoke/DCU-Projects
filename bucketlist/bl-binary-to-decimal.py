import sys
binary = sys.argv[1]
i = len(binary) # here we set the counter to how many numbers we have
power = 0
result = 0

while i > 0: # here we set the counter to do something i times
	result += int(binary[i-1]) * 2 ** power # we convert each number to decimal
	i = i - 1
	power = power + 1 # now we increase the power for every number we have
print result