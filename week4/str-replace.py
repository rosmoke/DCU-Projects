import sys
haystack = sys.argv[1]
needle = sys.argv[2]
replacement = sys.argv[3]
i = 0

while i < len(haystack) - (len(replacement)-1):
	if haystack[i:i+len(needle)] == needle:
		haystack = haystack[:i] + replacement + haystack[i+len(needle):]
		i = i + len(replacement)
	else:
		i = i + 1
print haystack