import sys
import re

lines = sys.stdin.read().splitlines()
p = int(sys.argv[1])
counter = 0


def find_rows(text):
    return [[cell for cell in row] for row in text]

def find_diagonals(text):
    diagonals = [[] for col in text[0]]
    for row in text:
        for col_index, cell in enumerate(row):
            diagonals[col_index].append(cell)
    return diagonals

def match():
	match = ""
	for i in range(p):
		match = match + "x"
	return("[^x]"+match+"[^x]")

def count(l):
	global counter	
	m = re.compile(match())
	x = m.findall("l" + l + "l")
	#print(x)
	if len(x) > 0:
		counter += 1

def horizontal(lines):
	l = 0
	while l < len(lines):
	# Check columns
		count(lines[l])
		l += 1
	return

def join(diagonals):
	joined = []
	for diagonal in diagonals:
		joined.append("".join(diagonal))
	return(joined)

def forward_diagonals(text):
    fill = ['Y']*(len(text[0])+1)
    fill_text = []
    for row_index, row in enumerate(find_rows(text)):
        fill_text.append(fill[row_index:] + row + fill[:row_index+1] )
    diagonals = find_diagonals(fill_text)[2:-1]
    for col in diagonals:
        while 'Y' in col:
            col.remove('Y')
    return(join(diagonals))

def reverse_diagonals(text):
    fill = ['Y']*(len(text[0])+1)
    fill_text = []
    for row_index, row in enumerate(find_rows(text)):
        fill_text.append( fill[:row_index+1] + row + fill[row_index:] )
    diagonals = find_diagonals(fill_text)[1:-2]
    for col in diagonals:
        while 'Y' in col:
            col.remove('Y')
    return(join(diagonals))

def vertical(text):
	i = 0
	vertical_lines = []
	while i < len(text[0]):
		line = ""
		j = 0
		while j < len(lines):
			line = line + lines[j][i]
			j = j + 1
		vertical_lines.append(line)
		i = i + 1
	return(vertical_lines)

horizontal(vertical(lines))
horizontal(lines)
horizontal(forward_diagonals(lines))
horizontal(reverse_diagonals(lines))
print(counter)