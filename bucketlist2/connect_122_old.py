import sys

lines = sys.stdin.read().splitlines()
p = int(sys.argv[1])
count = 0

def column(x, l):
	i = 0
	word = ""
	while i < len(l) and i <= p:
		if l[i].lower() == "x":
			word = word + l[i]
		else:
			break
		i = i + 1
	if word == "xxxx":
		return(True)

for line in lines:
	i = 0
	while i < len(line):
		if line[i].lower() == "x" and len(line[i:]) >= p:
			if column(line[i], line[i:]):
				count += 1
		i = i + 1 

print(count)

