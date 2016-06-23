import sys
from operator import itemgetter
lines = sys.stdin.read().splitlines()
hole_par = lines[0].split()
hole_index = lines[1].split()
d = {}

def handicap_calc():
	handicap = int(line.split()[-19:-18][0])
	hole_handicap = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
	i = 0
	while i < handicap:
		if i < 18:
			hole_handicap[i] += 1
		if i == 17:
			i = -1
			handicap = handicap - 18
		i = i + 1
	return(hole_handicap)

for line in lines[2:]:
	score = 0
	name = " ".join(line.split()[:-19])
	handicap = line.split()[-19:-18][0]
	strokes = line.split()[-18:]
	for x in range(18):
		try:
			if strokes[x].isdigit() == False:
				points = 2
			elif strokes[x].isdigit():
				net = int(strokes[x]) - handicap_calc()[int(hole_index[x])-1]
				points = net - int(hole_par[x])
			if points < 1:
				score += abs(points) + 2
			elif points == 1:
				score += 1
			else:
				score += 0
		except ValueError:
			continue
	d[name] = score

def myown(k):
	return(len(k[0]))
def sort_c():
	for k,v in sorted(d.items(), key=myown, reverse=True):
		return(len(k))
		break
for k,v in sorted(d.items(), key=itemgetter(1), reverse=True):
	print("{:>{}} : {:>2}".format(k, sort_c(), v))