import sys
hands = 0

d_words = {
	0:"nothing",
	1:"one pair",
	2:"two pairs",
	3:"three of a kind",
	4:"a straight",
	5:"a flush",
	6:"a full house",
	7:"four of a kind",
	8:"a straight flush",
	9:"a royal flush"}

d = {}
for line in sys.stdin.read().splitlines():
	rank = int(line.split(",")[-1])
	if rank not in d:
		d[rank] = 0
	d[rank] = d[rank] + 1
	hands += 1

for x in range(0,10):
	print("The probability of {} is {:.4f}%".format(d_words[x],(d[x]/hands) * 100))