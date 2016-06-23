import sys
text = sys.argv[1:]

i = 0
tmp = len(text[i])
while i < len(text): # we check which one is the longest
	if len(text[i]) > tmp:
		tmp = len(text[i])
	i = i + 1
print "*" * (tmp+4)

for word in text:
	if len(word) <= tmp:
		spaces = tmp - len(word) + 1
		word = "* " + word + " " * spaces + "*"
		print word
print "*" * (tmp+4)