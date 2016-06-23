def bsearch(a,q):
	low = 0
	high = len(a)
	while low < high:
		mid = (low + high) / 2
		if q > a[mid]:
			low = mid + 1
		else:
			high = mid
	return low
def contains(a,q):
	position = bsearch(a,q)
	if position < len(a) and a[position] == q:
		return True
	else:
		return False
#print contains([2,3,6,6,7,8], 21)
