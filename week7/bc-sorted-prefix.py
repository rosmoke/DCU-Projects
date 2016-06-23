lines = []

line = raw_input()
while line != "end":
   lines.append(line)
   line = raw_input()

if 0 < len(lines):
   print lines[0]
   i = 1
   while i < len(lines) and lines[i-1] <= lines[i]:
      print lines[i]
      i = i + 1
