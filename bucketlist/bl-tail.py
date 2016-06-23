import sys
n = int(sys.argv[1])
line = raw_input()
text = []
while line != "end": # stop when we detect "end" input
	text.append(line) # here we store each line of text in an list
	line = raw_input()
for i in text[len(text)-n:]: # do something for the last n lines
	print i # print the desired lines