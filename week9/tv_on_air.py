import time
import sys
lines = sys.stdin.readlines()
i = 0

def get_time():
	t = time.strftime("%H:%M")
	return t

def get_minutes(s):
	s = s.split(":")
	time_hours = int(s[0]) * 60
	time_minutes = int(s[1])
	total_minutes = time_minutes + time_hours
	return total_minutes

def current_time():
	t = get_time()
	t = get_minutes(t)
	return t

while i < len(lines):
	line = lines[i]
	details = line.split()
	line = " ".join(details)
	name = line[12:]
	start_time = line[:5]
	end_time = line[6:12]
	start = get_minutes(start_time)
	end = get_minutes(end_time)
	if start <= current_time() < end:
		print start_time, name
	i = i + 1