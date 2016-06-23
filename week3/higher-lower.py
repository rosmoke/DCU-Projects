value = input()
times = 0
previous = value


while times < 5:
	cur = input()
	if cur < previous:
		print "lower"
	elif cur > previous:
		print "higher"
	else:
		print "equal"
	previous = cur
	times = times + 1