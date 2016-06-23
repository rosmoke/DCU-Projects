from bankaccount_91 import CurrentAccount, SavingsAccount

def main():
   a1 = CurrentAccount('Joe', 'Murphy', 100)
   a2 = SavingsAccount('Mandy', 'Murray', 100)
   a3 = SavingsAccount('Jimmy', 'Smith', 200)

   # Print base classes
   print('Base classes...')
   print(a1.__class__.__bases__)
   print(a2.__class__.__bases__)
   # Print account details
   print('Account details...')
   print(a1)
   print(a2)
   print(a3)
   # Call some methods
   a1.lodge(50)
   a1.withdraw(100)
   a1.withdraw(100)
   a1.withdraw(1000)
   a2.withdraw(10)
   a2.withdraw(100)
   a2.lodge(20)
   a2.apply_interest()
   try:
       a1.apply_interest()
   except AttributeError:
       print('No such method')

   # Print account details
   print('Account details...')
   print(a1)
   print(a2)
#
if __name__ == '__main__':
    main()#