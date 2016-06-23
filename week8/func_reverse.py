list = [1, 2, 3, 10, 24, 20, 40]
def reverse(list):	#we replace each letter one by one starting from middle
	i = len(list)/2 - 1
	if len(list) % 2 == 0:
		j = len(list)/2
	else:
		j = len(list)/2 + 1
	while i >= 0:
		tmp = list[i]
		list[i] = list[j]
		list[j] = tmp
		j = j + 1
		i = i - 1
	return list

def main():
	print reverse(list)

if __name__ == "__main__":
	main()