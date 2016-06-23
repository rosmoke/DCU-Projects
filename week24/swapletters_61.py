import sys
word = sys.argv[1]
#swap adjacent letters
word = "".join([word[i:i+2][::-1] for i in range(0,len(word),2)])










print(word)