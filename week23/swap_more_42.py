def swap_unique_keys_values(d):
	new_dict = {}
	for k,v in d.items():
		count = -1
		for nk,nv in d.items():
			if d[k] == d[nk]:
				count += 1
		if not count:
			new_dict[v] = k
	return(new_dict)

def main():
	my_dict = {'a' : 4, 'b' : 7, 'c' : 10, 'd' : 7}
	print(swap_unique_keys_values(my_dict))

if __name__ == "__main__":
	main()


#Another way of doing it using list comprehensive

#def swap_keys_values(d):
#	return dict([(v, k) for (k, v) in d.items()])

#def swap_unique(d):
#	return dict([(v, k) for (k, v) in d.items()
#		if list(d.values()).count(v) == 1])