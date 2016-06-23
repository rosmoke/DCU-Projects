import timeit
import sys
import random
numbers = sys.argv[1:]
drawings = 1000000

#generate 1 mil random sets of six
def generate_set():
	a = []
	random.seed(42)
	for six in range(drawings):
		six = random.sample(range(1,48), 6)
		a.append(six)
	return(a)

def lotto():
	d = {}
	for x in generate_set():
		count = 0
		for y in numbers:
			if int(y) in x:
				count += 1
		if count >= 3 and count not in d:
			d[count] = 1
		elif count >= 3:
			d[count] = d[count] + 1
	for z in range(3,7):
		if z not in d:
			d[z] = 0
	return(d)

for match,times in lotto().items():
	if times == 0:
		presence = "?"
	else:
		presence = round(drawings / times)
	print("Match {}'s : {:>5} ({} to 1)".format(match,times,presence))
#print(timeit.timeit("generate_set()", setup="from __main__ import generate_set", number=1))