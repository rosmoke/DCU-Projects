import sys

h1 = 'POS'
h2 = 'CLUB'
h3 = 'P'
h4 = 'W'
h5 = 'D'
h6 = 'L'
h7 = 'GF'
h8 = 'GA'
h9 = 'GD'
h10 = 'PTS'

print('{:>3s} {:20s} {:>2s} {:>3s} {:>3s} {:>3s} {:>3s} {:>3s} {:>3s} {:>3s}'.format(h1, h2, h3, h4, h5, h6, h7, h8, h9, h10))

for line in sys.stdin:
	line = line.split()
	i = 1
	b = []
	b.append(line[0])
	done = False
	while i < len(line):
		if line[i].isdigit() and not done:
			b.append(" ".join(line[1:i]))
			done = True
		if done:
			b.append(line[i])
		i = i + 1
	line = b
	print('{:>3s} {:20s} {:>2s} {:>3s} {:>3s} {:>3s} {:>3s} {:>3s} {:>3s} {:>3s}'.format(line[0], line[1], line[2], line[3], line[4], line[5], line[6], line[7], line[8], line[9]))

