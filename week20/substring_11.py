import sys
first = sys.argv[1]
second = sys.argv[2]

def substring(x,y):
	return y in x


if __name__ == "__main__":
	print(substring(first,second))