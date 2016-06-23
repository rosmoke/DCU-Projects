times = 0
negative = 0
positive = 0

while times < 5:
	i = input()
	if i < 0:
		negative += i
	else:
		positive += i
	times = times + 1
print negative, positive