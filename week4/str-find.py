import sys
haystack = sys.argv[1]
needle = sys.argv[2]
i = 0
v = "-1"

while i < len(haystack):
	if haystack[i:i+len(needle)] == needle:
		v = "3"
	i = i + 1
print v