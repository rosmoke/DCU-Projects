import sys
a = sys.stdin.readline()
a = a.split()
i = 0

while i < len(a):
	j = i
	lowest = j
	while j < len(a):
		if int(a[j]) < int(a[lowest]):
			lowest = j
		j = j + 1
	tmp = a[lowest]
	a[lowest] = a[i]
	a[i] = tmp
	i = i + 1
print a