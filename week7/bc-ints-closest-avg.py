i = 0
ints = []
integer = raw_input()
total = 0.0

while integer != "end":
    total = total + int(integer)
    ints.append(integer)
    integer = raw_input()
    i = i + 1
if i > 1:
    total = total / i

n = 0
while n < len(ints):
	if abs(total-int(ints[n-1])) < abs(total-int(ints[n])):
		t = ints[n-1]
	else:
		t = ints[n]
	n = n + 1
print ints,total,t