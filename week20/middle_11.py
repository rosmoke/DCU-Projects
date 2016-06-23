import sys
word = sys.argv[1]

def middle(x):
	if len(x) % 2 != 0:
		center = int(int(len(x)) / 2)
		return x[center]
	else:
		return "No middle character!"

print(middle(word))