import sys
import statistics
a = []
for line in sys.stdin:
	a.append(int(line[:-1]))

def mean(a):
	return(sum(a) / len(a))

def mode(a):
	max = [0,0]
	for n in a:
		if a.count(n) > max[0]:
			max = [a.count(n),n]
	return(max)



print("Mean:", round(float(mean(a)), 1))
print("Mode:", float(mode(a)[1]))
print("Median:",float(statistics.median(a)))