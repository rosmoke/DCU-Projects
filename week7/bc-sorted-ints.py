lines = []
line = raw_input()
while line != "end":
   lines.append(line)
   line = raw_input()
i = 1
while i < len(lines) and lines[i-1] <= lines[i]:
   i+=1
if i < len(lines):
   print "not sorted"
else:
   print "sorted"
