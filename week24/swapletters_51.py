import sys
word = "".join([sys.argv[1][i:i+2][::-1] for i in range(0, len(word), 2)])
print(word)