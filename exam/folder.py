class Folder(object):
	# d is a dictionary that maps from file names to file objects
	def __init__(self):
		self.d = {}

	def add_file(self, f):
		if f.name in self.d:
			print('File already exists')
			return
		self.d[f.name] = f

	def del_file(self, user, name):
		if name not in self.d:
			print('No such file')
			return
		if self.d[name].owner != user:
			print('Access denied')
			return
		del self.d[name]

	def get_size(self):
		return(sum([f.get_size() for f in self.d.values()]))

	def __str__(self):
		heading = 'Folder contents'
		uline = '-' * len(heading)
		slist = [heading, uline]
		for k in self.d.keys():
			slist.append(self.d.[k].__str__())
		slist.append('Folder size: {} bytes'.format(self.get_size()))
		return('\n'.join(slist))