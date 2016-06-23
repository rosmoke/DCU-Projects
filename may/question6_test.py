from question6 import BankAccount, CurrentAccount, SavingsAccount

a1 = CurrentAccount('Joe', balance=1000)
a2 = SavingsAccount('Zoe', balance=1000)
a1.withdraw(1100)
print('{:.2f}'.format(a1.balance))
a2.withdraw(1100)
a2.lodge(1000)
a2.apply_interest()
print('{:.2f}'.format(a2.balance))
print('{:d}'.format(a2.account_number))