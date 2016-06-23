import sys
f = sys.argv[1]
try:
	t = open(f, 'r')
	text = t.readlines()
	i = 0
	high = text[0][:2]
	while i < len(text):
		if high < text[i][0]:
			high = text[i]
		i = i + 1
	mark = high[:2]
	name = high[2:]
	print("Best student:{}Best mark: {}".format(name, mark))
	t.close()
except FileNotFoundError:
	print('The file {:s} does not exist.'.format(f))
