# כעת נוסיף methods
# נוסיף בדיקה כי חשבון לא יורד למינוס וכי מפקידים מומשכים סכומים חיוביים
class BankAccount:
    def __init__(self, id: str, f_name: str, l_name: str):
        self.account_id: str = id
        self.first_name: str = f_name
        self.last_name: str = l_name
        self.balance: float = 0.0

    def deposit(self, amount: float):
        if amount >= 0:
            self.balance += amount
        else:
            print("ERROR: Cant deposit negative amount.")

    def withdraw(self, amount: float):
        if amount >= 0:
            if amount <= self.balance:
                self.balance -= amount
            else:
                print("ERROR: Overdraft.")
        else:
            print("ERROR: Cant withdraw negative amount.")


bank_account1 = BankAccount('1245', 'Moshe', 'Cohen')
bank_account2 = BankAccount('8982', 'David', 'Lev')

print("**** bank_account1")
print( bank_account1 )
print( 'Beginning', bank_account1.__dict__ )

bank_account1.deposit(100)
print( 'After deposit 100', bank_account1.__dict__ )

bank_account1.deposit(11)
print( 'After deposit 11', bank_account1.__dict__ )

bank_account1.withdraw(100)
print( 'After withdraw 100', bank_account1.__dict__ )

bank_account1.withdraw(100)
print( 'After withdraw 100. Expecting ERROR and no change in balance', bank_account1.__dict__ )
