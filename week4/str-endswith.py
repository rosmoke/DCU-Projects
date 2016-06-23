import sys
s = sys.argv[1]
suffix = sys.argv[2]

if s[len(s)-len(suffix):] == suffix:
	print "True"
else:
	print "False"