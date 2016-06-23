import sys
from operator import itemgetter
title = sys.argv[1]
l = sys.stdin.read().splitlines()

tile_values = { 'a':1, 'b':3, 'c':3, 'd':2, 'e':1,
                'f':4, 'g':2, 'h':4, 'i':1, 'j':8,
                'k':5, 'l':1, 'm':3, 'n':1, 'o':1,
                'p':3, 'q':10, 'r':1, 's':1, 't':1,
                'u':1, 'v':4, 'w':4, 'x':8, 'y':4,
                'z':10 }

d1 = {}
board = []
for letter in title:
	if letter not in d1:
		d1[letter] = title.count(letter)
for word in l:
	d2 = {}
	for c in word:
		if c not in d2:
			d2[c] = word.count(c)
	score = 0
	for c in d2:
		if c in d1:
			times = min(d1[c],d2[c])
			score += tile_values[c] * times
	w = [word,score]
	board.append(w)
print("{}: {}".format(sorted(board, key = itemgetter(1), reverse = True)[0][0], sorted(board, key = itemgetter(1), reverse = True)[0][1]))