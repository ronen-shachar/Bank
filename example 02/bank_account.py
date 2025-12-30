# המופע יווצר כעת עם פרמטרים כפי שאנחנו נחליט

class BankAccount:
    def __init__(self, id, f_name, l_name):
        self.account_id: str = id
        self.first_name: str = f_name
        self.last_name: str = l_name
        self.balance: float = 0.0

bank_account1 = BankAccount('1245', 'Moshe', 'Cohen')
bank_account2 = BankAccount('8982', 'David', 'Lev')

print("**** bank_account1")
print( bank_account1 )
print( bank_account1.__dict__ )

print("**** bank_account2")
print( bank_account2 )
print( bank_account2.__dict__ )
