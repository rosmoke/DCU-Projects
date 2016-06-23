mark = 70

if mark < 40:
	result = "fail"
elif mark >= 40 and mark < 50:
	result = "third"
elif mark  >= 50 and mark < 70:
	result = "second"
else:
	result = "first"

print "A mark of", mark, "is classified as a", result
