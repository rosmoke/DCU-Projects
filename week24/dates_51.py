import sys
import datetime
for line in sys.stdin:
	line = datetime.datetime.strptime(line[:-1], "%d %B %Y").strftime("%d/%m/%y")
	line_start = line[:-3].replace("/0","/").lstrip("0")
	line_end = line[5:]
	print(line_start + line_end)