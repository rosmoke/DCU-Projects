n = raw_input()
list = []

def slurp_lines(n):
	while n != "end":
		list.append(n)
		n = raw_input()
	return list

def slurp_ints(n):
	while n != "end":
		list.append(int(n))
		n = raw_input()
	return list

def print_list(n):
	slurp_lines(n)
	for x in list:
		print x

def main():
	#print slurp_lines(n)
	print_list(n)

if __name__ == "__main__":
	main()