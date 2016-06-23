import sys
s = sys.argv[1]
prefix = sys.argv[2]

if s[0:len(prefix)] == prefix:
	print "True"
else:
	print "False"