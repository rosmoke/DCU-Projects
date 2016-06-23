cypher = {
	"a": "b",
	"b": "c",
	"c": "a"
}

def encode(cypher,s):
	a = []
	i = 0
	while i < len(s):
		a.append(s[i])
		if a[i] in cypher:
			a[i] = cypher[a[i]]
		i = i + 1
	a = "".join(a)
	return a
print encode(cypher,"cab")