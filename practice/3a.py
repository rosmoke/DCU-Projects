a = [4,10,1,7]
i = 0
while i < len(a):
	if a[i] % 2 != 0:
		a[i] = 0
	i = i + 1
print a