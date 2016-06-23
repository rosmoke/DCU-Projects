import sys
from collections import Counter

dictionary = ["the","of","and","to","a","in","that","is","was","he","for","it","with","as","his","on","be","at","by","i","this","had","not","are","but","from","or","have","an","they","which","one","you","were","her","all","she","there","would","their","we","him","been","has","when","who","will","more","no","if","out","so","said","what","up","its","about","into","than","them","can","only","other","new","some","could","time","these","two","may","then","do","first","any","my","now","such","like","our","over","man","me","even","most","made","after","also","did","many","before","must","through","back","years","where","much","your","way","well","down","should","because","each","just","those","people","mr","how","too","little","state","good","very","make","world","still","own","see","men","work","long","get","here","between","both","life","being","under","never","day","same","another","know","while","last","might","us","great","old","year","off","come","since","against","go","came","right","used","take","three"]
text = sys.stdin.read()
encoded = [word for word in (" ".join(text.splitlines()).split()) if word.isalpha() or word.isdigit()]
alphabet = list("abcdefghijklmnopqrstuvwxyz0123456789")

def match(word_encoded,i):
	letters = list(word_encoded)
	word = []
	[word.append(alphabet[alphabet.index(letter.lower()) + i - len(alphabet)]) if alphabet.index(letter.lower()) + i >= len(alphabet) else word.append(alphabet[alphabet.index(letter.lower()) + i]) for letter in letters]	
	return("".join(word).upper())

occurences = []
[occurences.append(i) for word_dict in dictionary for i in range(35) if match(word_dict,i) in encoded]
if len(Counter(occurences).most_common(1)) > 0:
	shift_value = Counter(occurences).most_common(1)[0][0]
else:
	shift_value = 0

def translate(letter,shift):
	return(alphabet[alphabet.index(letter.lower()) - shift].upper())

new_text = []
for c in text:
	if c.isalpha() or c.isdigit():
		letter = translate(c,shift_value)
		new_text.append(letter)
	else:
		new_text.append(c)
sys.stdout.write("".join(new_text))