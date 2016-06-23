import sys
import math

text = sys.stdin.read().splitlines()

def roots(line):
		try:
			tokens = line.split()
			a = int(tokens[0])
			b = int(tokens[1])
			c = int(tokens[2])
			r1 = (-b + math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
			r2 = (-b - math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
			return("r1 = {}, r2 = {}".format(r1,r2))
		except ValueError:
			return(None)

for line in text:
	print(roots(line))