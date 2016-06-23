import sys
haystack = sys.argv[1]
needle = sys.argv[2]
i = 0
c = 0

while i < len(haystack) - (len(needle) - 1):
	if haystack[i:i+len(needle)] == needle:
		c = c + 1
	i = i + 1
print c