import math
def overlap(x1=0,y1=0,r1=1,x2=0,y2=0,r2=1):
	distance = math.sqrt((y2-y1) ** 2 + (x2-x1) ** 2)
	if r1+r2 > distance:
		return(True)
	else:
		return(False)

