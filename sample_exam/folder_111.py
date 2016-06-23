class File(object):
	FILE_PERMISSIONS = "rwx"
	def __init__(self, name, owner, size=0, permissions="null"):
		self.name = name
		self.owner = owner
		self.permissions = permissions
		self.get_size = size
	def has_access(self,name, permission):
		if name == self.owner:
			return("Access granted")
		if permission in self.permissions:
			return("Access granted")
		else:
			return("Access denied")
	def enable_permission(self, name, permission):
		if name != self.owner:
			print("Access denied")
			return()
		if self.permissions == "null":
			self.permissions = ""
		if permission in self.permissions or permission not in self.FILE_PERMISSIONS:
			return()
		self.permissions = "".join(sorted(self.permissions + permission))
	def get_permissions(self):
		return(self.permissions)
	def get_size(self):
		return self.size
	def disable_permission(self, name, permission):
		if name != self.owner:
			print("Access denied")
			return()
		if permission not in self.permissions or permission not in self.FILE_PERMISSIONS:
			return()
		if self.permissions == "null":
			self.permissions = ""
		self.permissions = self.permissions.replace(permission,"")
	def __str__(self):
		if self.permissions == "":
			self.permissions = "null"
		return("File: {}\nOwner: {}\nPermissions: {}\nSize: {} bytes".format(self.name, self.owner, self.permissions, self.get_size))

class Folder(object):

	def __init__(self):
		self.d = {}

	def add_file(self,f):
		if f.name in self.d:
			print('File already exists')
		self.d[f.name] =  f

	def del_file(self,user,name):
		if name not in self.d:
			print('No such file')
			return
		if self.d[name].owner != user:#Go to d lookup file name,check if user is owner, if they arnt do nothing
			print('Access denied')
			return
		else:
			del self.d[name]

	def get_size(self):
		return sum([f.get_size() for f in self.d.values()])

	def __str__(self):
		heading = 'Folder contents'
		uline = '=' * len(heading)
		slist = [heading,uline]
		for k in sorted(self.d.keys()):
			slist.append(self.d[k].__str__())
		slist.append('Folder size: {} bytes'.format(self.get_size()))
		return '\n'.join(slist)