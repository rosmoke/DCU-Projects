def swap_keys_values(d):
	new_d = {}
	for k,v in d.items():
		new_d[v] = k
	return(new_d)

def main():
	d = {"one":"1","two":"2"}
	print(swap_keys_values(d))

if __name__ == "__main__":
	main()