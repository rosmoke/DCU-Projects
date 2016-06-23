line = raw_input()
text = []

while line != "end":
	text.append(line) # each encountered line is being saved in a list
	line = raw_input()

for line in text: # each line gets reversed
	i = 0
	phrase = ""
	letter = len(line)
	while i <= len(line):
		phrase += line[letter:letter + 1]
		i = i + 1
		letter = letter - 1
	print phrase # we print the line reversed