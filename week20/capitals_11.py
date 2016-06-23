import sys

name = sys.argv[1]
if len(name) >= 2:
	print (name.capitalize()[:len(name)-1]+name[-1].upper())