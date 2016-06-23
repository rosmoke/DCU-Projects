from collections import namedtuple
Student = namedtuple('Student', ['firstname', 'surname', 'id'])
def show_student(s):
	print("{:>0}{}".format("First name: ", s.firstname))
	print("{:>12}{}".format("Surname: ", s.surname))
	print("{:>12}{}".format("ID: ", s.id))