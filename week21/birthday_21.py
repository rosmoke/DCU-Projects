import sys
import calendar

day = int(sys.argv[1])
month = int(sys.argv[2])
year = int(sys.argv[3])
text = ["Monday's child is fair of face",
"Tuesday's child is full of grace",
"Wednesday's child is full of woe",
"Thursday's child has far to go",
"Friday's child is loving and giving",
"Saturday's child works hard for a living",
"Sunday's child is fair and wise and good in every way"]
start = "You were born on a"
a = []

for line in text:
	line = line.split()[0].split("'")[0]
	a.append(line)
weekday = calendar.weekday(year, month, day)
print(start, a[weekday] + " and " + text[weekday] + ".")