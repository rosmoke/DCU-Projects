import sys
import re

f = sys.stdin.read()

p = re.compile("\d+/\d+/\d+")
dates1 = p.findall(f)
print(dates1)

p = re.compile("\d+-\d+-\d+")
dates2 = p.findall(f)
print(dates2)

p = re.compile("\d+[-/]\d+[-/]\d+")
dates3 = p.findall(f)
print(dates3)

p = re.compile("01[\s-]\d{7}")
ph = p.findall(f)
print(ph)

p = re.compile("(?:\w+\.)*\w+\@\w+\.\w+(?:\.\w+)*")
email = p.findall(f)
print(email)

p = re.compile("\d{1,2}\s\w{3}\s\d{2,4}")
date4 = p.findall(f)
print(date4)