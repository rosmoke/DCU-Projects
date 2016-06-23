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

def count(a,q):
	tmp = bsearch(a,q)
	count = 0
	while q == a[tmp] and tmp > q:
		count = count + 1
		tmp = tmp + 1
	return count
print count([2,3,6,6,7,8],8)