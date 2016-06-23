import sys
runners = []
for line in sys.stdin.read().splitlines():
	tokens = line.split(" ")
	runner = []
	for token in tokens[1:]:
		try:
			time = int(token[:-3]) * 60 + int(token[-2:])
		except ValueError:
			time = -1
		runner.append(time)
	if -1 not in runner:
		best = runner[1]
		for time in runner:
			if time < best:
				best = time
	runners.append((tokens[0],best))
time = runners[0][1]
best = runners[0][0]
for k,v in runners:
	if v < time:
		time = v
		best = k
hours = str(int(time/60))
minutes = str(time%60)
if minutes < "10":
	minutes = "0" + minutes
print(best, ":", hours + ":" + minutes)