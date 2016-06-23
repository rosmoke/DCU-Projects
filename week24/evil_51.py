import sys

def presence_check(c,word):
	if c in word.lower() and word.lower().count(c) == 1:
		return(word.lower().find(c))
	else:
		return(0)

characters = list("evil")
for word in sys.stdin.readlines():
	positions = []
	for c in characters:
		positions.append(presence_check(c,word))
	if positions[0] < positions[1] < positions[2] < positions[3]:
		print(word[:-1])