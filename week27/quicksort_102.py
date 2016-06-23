def quicksort(A, p, r, h=None):
	if h == None:
		q = j = p
		h = 1
	if j < r:
		var = A[j]
		A[j] = A[q]
		A[q] = var
		q +=1
	j +=1
	if j == r:
		var = A[j]
		A[j] = A[r]
		A[r] = var
		return(A)
	return(quicksort(A,p,r, h))