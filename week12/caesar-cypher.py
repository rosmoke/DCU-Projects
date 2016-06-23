import sys
v = sys.argv[1]
t = raw_input()

def encrypt(alpha):
	alpha = "abcdefghijklmnopqrstuvwxyz"
	word = ""
	i = 0
	while i < len(t):
		j = 0
		while j < len(alpha):
			if t[i] == alpha[j]:
				if j > len(alpha)-4:
					word = word + alpha[j-23]
				else:
					word = word + alpha[j+int(v)]
			elif t[i] == alpha[j].upper():
				if j > len(alpha)-4:
					word = word + alpha[j-23].upper()
				else:
					word = word + alpha[j+int(v)].upper()
			j = j + 1
		if t[i].isalpha() == False:
			word = word + t[i]
		i = i + 1
	return word

print encrypt(t)