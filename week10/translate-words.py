import sys
t = sys.argv[1]
dictionary = open(t, "r")
text = sys.stdin.readlines()
fraze = []

for newline in dictionary.readlines():
	fraze.append(newline.split())

for line in text:
	line_list = line.split()
	i = 0
	while i < len(line_list):
		for fraza in fraze:
			if line_list[i] == fraza[0]:
				line_list[i] = fraza[1]
		i = i + 1
	print (" ").join(line_list)