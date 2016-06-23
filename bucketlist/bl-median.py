t = raw_input()
a = []

while t != "end":
	a.append(t)		#here we build a list of integers
	t = raw_input()

def sort(a): # this function will sort our list
	b = []
	i = 0
	while i < len(a):
		curr = a[i]
		for j in range(i, len(a)): # we find the smallest number in our list
			if int(a[j]) < int(curr):
				curr = a[j]
		for k in range(i, len(a)):	# we remove that number from our list
			if curr == a[k]:
				a.pop(k)
				i = i - 1
				break	# if we have the same number more than once, we remove only once
		b.append(curr) # we add that number in our ordered list
		i = i + 1
	return b

b = sort(a)
median = len(b)/2
print b[median]

