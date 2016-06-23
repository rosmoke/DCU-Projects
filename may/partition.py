def partition(A, p, r):
	q = j = p
	while j < r:
		if A[j] <= A[r]:
			A[q], A[j] = A[j], A[q]
			q += 1
		j += 1
	A[q], A[r] = A[r], A[q]
	return q
A = [10, 20, 59, 83, 18, 47, 44, 96, 16, 38]
print(A, "initial")
partition(A, 0, len(A)-1)