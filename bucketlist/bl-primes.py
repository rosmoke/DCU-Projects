import sys
a = sys.argv[1]
i = 2.00

while i < int(a): 		
	prime = True			#we assume all are primes and test that
	for x in range(2,10):
		if i / x - (int(i)/x) == 0 and i != x:
			prime = False
	if prime:
		print int(i)
	i = i + 1