i = 0
integer = raw_input()
total = 0.0
while integer != "end":
   total = total + int(integer)
   integer = raw_input()
   i = i + 1
if i > 1:
   print total / i
else:
   print total
