import sys
a = []

#each line is added to a
for line in sys.stdin:
	a.append(line[:-1])

# Print a list of all words that contain exactly 17 letters.
print(("Words containing 17 letters: {}").format([w for w in a if len(w) == 17]))
# Print a list of all words that contain more than 17 letters.
print(("Words containing 18+ letters: {}").format([w for w in a if len(w) > 17]))
# Print the shortest word that contains all vowels (‘aeiou’).
print(("Shortest word containing all vowels: {}").format(min([w for w in a if "a" in w and "e" in w and "i" in w and "o" in w and "u" in w], key=len)))
# Print all words that contain four a’s.
print(("Words with 4 a's: {}").format([w for w in a if w.count("a") == 4]))
# Print all words that contain two or more q’s.
print(("Words with 2+ q's: {}").format([w for w in a if w.count("q") >= 2]))
# Print all words that contain the sequence ‘cie’.
print(("Words containing cie: {}").format([w for w in a if "cie" in w]))
# Print all words that are anagrams of ‘angle’.
print(("Anagrams of angle: {}").format([w for w in a if sorted(list("angle")) == sorted(list(w)) and w != "angle"]))
# Print a count of all the words that end in ‘iary’.
print(("Words ending in iary: {}").format(len([w for w in a if w.endswith("iary")])))
# Print all words that contain q not immediately followed by u.
print(("Words with q but no u: {}").format([w for w in a if "q" in w and not "qu" in w]))
# Print the words that contain most e’s.
max_e = max([w.count("e") for w in a])
print(("Words with most e's: {}").format([w for w in a if w.count("e") == max_e]))



