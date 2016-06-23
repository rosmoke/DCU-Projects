a = [1,2,3,1,2,3]

def swap(a, i, j):
	tmp = a[i]
	a[i] = a[j]
	a[j] = tmp
	return a

def find_smallest_position(a,i):
	a = a[i:]
	k = 0
	j = 0
	tmp = a[0]
	while k < len(a):
		if a[k] < tmp:
			tmp = a[k]
			j = k
		k = k + 1
	return j + i

def main():
	print swap(a,3,4)
	print find_smallest_position(a,4)

if __name__ == "__main__":
	main()