def maximum(*a):
	if len(a[0]) == 1:
		return(a[0][0])
	a[0].pop(a[0].index(min(a[0])))
	return(maximum(a[0]))