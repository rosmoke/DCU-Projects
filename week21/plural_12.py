import sys
word = sys.argv[1]
a = ["a", "e", "i", "o", "u", "y"]
if word.endswith("ch") or word.endswith("sh") or word.endswith("x") or word.endswith("s") or word.endswith("z"):
	word = word + "es"
elif word.endswith("y") and word[len(word)-2] != "a" and word[len(word)-2] != "e" and word[len(word)-2] != "i" and word[len(word)-2] != "o" and word[len(word)-2] != "u" and word[len(word)-2] != "y" and len(word) > 2:
	word = word[:len(word)-1] + "ies"
elif word.endswith("f"):
	word = word[:len(word)-1] + "ves"
elif word.endswith("fe"):
	word = word[:len(word)-2] + "ves"
elif word.endswith("o"):
	word = word + "es"
else:
	word = word + "s"
print(word)