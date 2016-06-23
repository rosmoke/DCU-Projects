def convert(x):
	if x % 2 != 0:
		x = 0
	return x

print map(convert, [4,10,1,7])