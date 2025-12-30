# יצירת class ללא תכונות (properties)
# שימו לב כי כתובות המופעים (instances) שונות

class BankAccount:
    pass

bank_account1 = BankAccount()
bank_account2 = BankAccount()

print("**** bank_account1")
print( bank_account1 )
print( bank_account1.__dict__ )

print("**** bank_account2")
print( bank_account2 )
print( bank_account2.__dict__ )
