import sys

def get_minutes(s):
	s = s.split(":")
	time_hours = int(s[0]) * 60
	time_minutes = int(s[1])
	total_minutes = time_minutes + time_hours
	return total_minutes

def main():
	print get_minutes("01:05")

if __name__ == "__main__":
	main()