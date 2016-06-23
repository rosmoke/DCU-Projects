new_a = []
def reverse_list(a,m=None):
	global new_a
	if len(a) == 0:
		l = new_a
		new_a = []
		return(l)
	new_a.append(a.pop())
	return(reverse_list(a,m))