import sys
numbers = sys.stdin.read().splitlines()

def sumFac(n):
	total = 0
	for i in range(1,n):
		if n % i == 0:
			total += i
	return(total)
def isPerfect(n):
	if n == sumFac(n):
		return(True)
	else:
		return(False)
for number in numbers:
	print(isPerfect(int(number)))