seen = []

line = raw_input()
while line != "end":
   i = 0
   while i < len(seen) and line != seen[i]:
      i += 1
   found = i < len(seen)

   if not found:
      print line
      seen.append(line)

   line = raw_input()