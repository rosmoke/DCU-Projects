service = 1000
job = raw_input()
servers = []
i = 0

while job != "end":
	if i == 0:
		servers = [int(job)+service]
		start_time = int(job)
	done = True
	for x in servers:
		if x < int(job) and done:
			x = start_time+service
			done = False
		elif done and i > 0:
			servers.append(int(job)+service)
			done = False
	job = raw_input()
	i = i + 1
print len(servers)
