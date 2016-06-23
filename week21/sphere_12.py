import sys
import math

start_r = float(sys.argv[1])
increment_r = float(sys.argv[2])
end_r = float(sys.argv[3])

radius = "Radius (m)"
area = "Area (m^2)"
volume = "Volume (m^3)"
dash = "-"

print('{:>0} {:>15} {:>15}'.format(radius, area, volume))
print('{:>0} {:>15} {:>15}'.format(dash * 10, dash * 10, dash * 12))

i = start_r
while i <= end_r:
	area = 4 * math.pi * (i ** 2)
	volume = (4 / 3) * math.pi * (i ** 3)
	print('{0:10.1f} {1:15.2f} {2:15.2f}'.format(i, area, volume))
	i = i + increment_r
