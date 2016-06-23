import sys
from operator import itemgetter
teams = [[line[:-10]] + line.split()[-5:] for line in sys.stdin.read().splitlines()]
a = {}
for team in teams:
	try:
		result = int(team[1]) + int(team[2]) + int(team[3]) + int(team[4]) + int(team[5])
	except ValueError:
		continue
	a[team[0]] = result
for k,v in sorted(a.items(), key=itemgetter(1), reverse=True):
	print(k + " " + str(v) + " points")