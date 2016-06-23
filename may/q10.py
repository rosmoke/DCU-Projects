class Contact(object):
   def __init__(self, name, phone, email):
      self.name = name
      self.phone = phone
      self.email = email

   def __str__(self):
      return(self.name + " " + self.phone + " " + self.email)

class ContactList(Contact):
   def __init__(self):
      self.contactlist = {}

   def add(self, contact):
      if contact.name in self.contactlist:
         print("Contact already present")
         return
      self.contactlist[contact.name] = contact
      return

   def display(self, contact):
      if contact in self.contactlist:
         print(self.contactlist[contact])
         return
      print("No such contact")

   def remove(self, contact):
      if contact in self.contactlist:
         self.contactlist.pop(contact, None)
         return
      print("No such contact")

   def __str__(self):
      s = ""
      for contact in self.contactlist.values():
         s += str(contact)
         s += "\n"
      return(s)


# Program
# Initialise a contact list
cl = ContactList()
# Initialise some contacts
c1 = Contact(name='Max', phone='087 2233456',
 email='max@google.com')
c2 = Contact(name='Zoe', phone='085 1188555',
 email='zoe@yahoo.com')
c3 = Contact(name='Una', phone='086 2255448',
 email='una@eircom.net')
c4 = Contact(name='Lou', phone='087 4422456',
 email='lou@hotmail.com')
# Add contacts to contact list
cl.add(c1)
cl.add(c2)
cl.add(c3)
cl.add(c4)
cl.add(c4) # Produces the message "Contact already present"
# Lookup contacts
cl.display('Lou') # Prints Lou's details
cl.display('Moe') # Produces the message "No such contact"
# Remove contacts from contact list
cl.remove('Una') # Deletes the corresponding contact
cl.remove('Moe') # Produces the message "No such contact"
# Print contact list details. Contacts are printed in
# ascending alphabetical order. The total number of contacts
# is also printed.
print(cl)