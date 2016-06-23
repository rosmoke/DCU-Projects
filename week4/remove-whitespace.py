s = raw_input()

i = 0
while i < len(s) and s[i].isdigit():
   i += 1

print s[i:]