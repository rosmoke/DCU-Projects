import sys
first = sys.argv[1]
second = sys.argv[2]
j = 0

for c in first:
	presence = False
	i = 0
	for d in second:
		if c == d:
			presence = True
			second = second[:i] + second[i+1:]
			if presence:
				j = j + 1
		i = i + 1
if j == len(first):
	presence = True
else:
	presence = False
print(presence)