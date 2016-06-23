count = 0
def count_letters(word):
	global count
	if word == "":
		times = count
		count = 0
		return(times)
	word = word[:-1]
	count += 1
	return(count_letters(word))