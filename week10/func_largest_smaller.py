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

def largest_smaller(a,q):
	tmp = bsearch(a,q)
	return a[tmp-1]

#print largest_smaller([2,3,6,6,7,8], 4)