class File(object):
	
	FILE_PERMISSIONS = "rwx"

	def __init__(self, filename, owner, size=0, permissions=""):
		self.filename = filename
		self.owner = owner
		self.size = size
		self.permissions = permissions

	def get_permissions(self):
		if not self.permissions:
			return("null")
		return("".join(sorted(self.permissions)))

	def has_access(self, name, permission):
		if self.owner == name or permission in self.permissions:
			return("Access granted")
		else:
			return("Access denied")

	def enable_permission(self, name, permission):
		if permission not in File.FILE_PERMISSIONS or permission in self.permissions:
			return
		if self.owner == name:
			self.permissions = self.permissions + permission
			return
		else:
			print("Access denied")

	def disable_permission(self, name, permission):
		if self.owner == name and permission in self.permissions:
			self.permissions = self.permissions.replace(permission, "")
			return
		else:
			return

	def __str__(self):
		return("File: {}\nOwner: {}\nPermissions: {}\nSize: {} bytes".format(self.filename, self.owner, self.get_permissions(), self.size))