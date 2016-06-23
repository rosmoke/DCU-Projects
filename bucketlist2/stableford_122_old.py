import sys

lines = sys.stdin.read().splitlines()

par = lines[0].split()
hole_index = lines[1].split()
strokes = lines[5].split()[-18:]


#dictionary of par for each index hole




for line in lines[2:]:
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

	for i in range(18):
		hole_index[i] = hole_handicap[hole_index[i]]
		print(hole_index[i])





	handicap = int(line.split()[-19:-18][0])

	name = " ".join(line.split()[:-19])
	line = line.split()[-18:]
	score = 0
	for x in range(18):
		strokes = line[x]
		try:
			if line[x].isdigit() == False:
				points = 2
			elif strokes.isdigit():
				net = int(strokes) - hole_handicap[x]
				points = net - int(par[x])
				#points = int(strokes) - hole_handicap[x] - d[x+1]
			if points < 1:
				score += abs(points) + 2
			elif points == 1:
				score += 1
			else:
				score += 0
			#print("Strokes: ", strokes, "Score: ",score, "Hole Handicap: ", hole_handicap[x],"Par: ", par[x])
		except ValueError:
			continue
	hole_index = lines[1].split()
	#print(name, score,handicap)