from quicksort_102 import quicksort
import random

def main():
	A = random.sample(range(-99, 100), 10)

	print("unsorted: {}".format(A))
	print(quicksort(A, 0, len(A)-1))

if __name__ == "__main__":
	main()