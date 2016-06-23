dublin_goals = 2
dublin_points = 7

kerry_goals = 3
kerry_points = 5


dublin = dublin_goals * 3 + dublin_points
kerry = kerry_goals * 3 + kerry_points

if dublin > kerry:
	print "Dublin wins"
if kerry > dublin:
	print "Kerry wins"
if dublin == kerry:
	print "Draw"
