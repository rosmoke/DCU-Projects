class File(object):
	FILE_PERMISSIONS = "rwx"
	def __init__(self, name, owner, size=0, permissions="null"):
		self.name = name
		self.owner = owner
		self.permissions = permissions
		self.size = size
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
		return("File: {}\nOwner: {}\nPermissions: {}\nSize: {} bytes".format(self.name, self.owner, self.permissions, self.size))