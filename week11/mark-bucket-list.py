import sys
t = open("uploads.txt")
names = {}
people = []

def translate(x): # here we translate our mark in values
	if x == "correct":
		return 1
	else:
		return 0

for line in t:
	line = line.replace("\n","").replace(".py.",".py/")
	details = line.split("/")
	name = details[2]
	exercise = details[3]
	mark = translate(details[4])
	if name not in names:
		names[name] = {}
		people.append(name)
	if exercise.startswith("bl-"):
		names[name][exercise] = mark

for person in people: # in this loop we print the total of marks for each student
	total = 0
	results = names[person].values()
	for result in results:
		total += result
	print person, total