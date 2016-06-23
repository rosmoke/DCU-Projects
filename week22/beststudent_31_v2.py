import sys
f = sys.argv[1]
try:
	t = open(f, 'r')
	text = t.readlines()
	high_mark = 0
	high_name = ""
	for line in text:
		line = line.split()
		mark = line[0]
		name = line[1:]
		name = " ".join(name)
		if int(mark) > high_mark:
			high_mark = int(mark)
			high_name = name
	print("Best student: {}\nBest mark: {}".format(high_name, high_mark))
except FileNotFoundError:
	print('The file {:s} does not exist.'.format(f))
except ValueError:
	print('Invalid mark {} encountered. Exiting.'.format(mark))