pi = 3.141

def circumference(r):
	return 2 * pi * r
def area(r):
	return pi * r ** 2

def main():
	print circumference(5)
	print area(3)

if __name__ == "__main__":
	main()