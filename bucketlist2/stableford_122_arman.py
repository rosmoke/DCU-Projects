import sys
import math
import re

HS = {}
Players = {}

ScoreToPar = {
	"-4" : 6,
	"-3" : 5,
	"-2" : 4,
	"-1" : 3,
	"0" : 2,
	"1" : 1,
	"2" : 0,
}

for line in sys.stdin:
	try:
		details = line.split()
		par = all(int(x) <= 5 for x in details)
		if par:
			Par = details
		else:
			Index = details
	except ValueError:
		word = "".join(details[0:2])
		new_word = (re.sub(r'\W+', '', word))
		if new_word.isalpha():
			HS[" ".join(details[0:2])] = (details[2], details[3:])
		else:
			HS[details[0]] = (details[1], details[2:])

#print (Par)
#print (Index)

i = 0
for (k, v) in HS.items():
	try:
		value = math.floor(int(v[0])/18)
		remainder = [x for x in range(1, int(v[0])%18+1)]
		total = 0
		for c in v[1]:
			try:
				if int(Index[i]) in remainder:
					score = (int(c) - int(Par[i]) - value - 1)
					if score < 1:
						total += abs(score) + 2
					elif score == 1:
						total += 1
					else:
						total += 0
				else:
					score = (int(c) - int(Par[i]) - value)
					if score < 1:
						total += abs(score) + 2
					elif score == 1:
						total += 1
					else:
						total += 0
				i = i + 1
			except ValueError:
				pass
				i = i + 1
		i = 0

		Players[k] = total
	except ValueError:
		pass

for (k, v) in  sorted(Players.items(), key=lambda x: (-x[1], x[0])):
	max = 0
	if len(k) > max:
		max = int(len(k))

for (k, v) in  sorted(Players.items(), key=lambda x: (-x[1], x[0])):
	print ('{:>{}} : {:2d}'.format(k, max, v))



