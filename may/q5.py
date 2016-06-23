import sys
import re

f = sys.stdin.read()

p = re.compile(r"(?:\b0[1-9]|[1-2][0-9]|3[0-1])/(?:0[1-9]|1[0-2])/\d\d")
m = p.findall(f)
print(m)