ints = []
int = raw_input()


while int != "end":
   ints.append(int)
   int = raw_input()

if len(ints) > 0:
   maxx = ints[0]
else:
   maxx = 0 
i = 1
while i < len(ints):
   if ints[i-1] < ints[i]:
      maxx = ints[i]
   i = i + 1
print maxx
