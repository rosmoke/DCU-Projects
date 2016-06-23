import timeit
s = raw_input()

def reverse(s):
	s = "daniel"
	return s[::-1]

print reverse(s), timeit.timeit(reverse(s))