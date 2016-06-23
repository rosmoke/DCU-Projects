import sys
import math
stack = []


def add(x,y):
	return x + y
def sub(x,y):
	return x - y
def mul(x,y):
	return x * y
def div(x,y):
	return x / y
def power(x,y):
	return x ** y

def neg(x):
	return -x
def squ(x):
	return x * x
def sqr(x):
	return math.sqrt(x)
def log(x):
	return math.log(x)

# start dictionary
binary = {
	"+": add,
	"-": sub,
	"*": mul,
	"/": div,
	"**": power,
}
unary = {
	"n": neg,
	"s": squ,
	"r": sqr,
	"l": log,
}
# end dictionary


def main():
	lines = "l"
	while lines:
		lines = sys.stdin.readline()
		tokens = lines.split()
		for token in tokens:
			if token in binary:
				x = stack.pop()
				y = stack.pop()
				stack.append(binary[token](x,y))
			elif token in unary:
				x = stack.pop()
				stack.append(unary[token](x))
			else:
				stack.append(int(token))
		print stack
if __name__ == "__main__":
	main()