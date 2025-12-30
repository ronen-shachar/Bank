# override method כעת נוסיף
# שימו לב כי בחשבון VIP ניתן לרדת לאוברדראפט
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


class VIPBankAccount(BankAccount):

    def withdraw(self, amount: float):
        if amount > 0:
            self.balance -= amount
        else:
            print("ERROR: Amount must be positive")


bank_account1 = BankAccount('1245', 'Moshe', 'Cohen')
vip_bank_account2 = VIPBankAccount('8982', 'David', 'Lev')

print("**** bank_account1")
print( bank_account1 )
print( 'Beginning: ', bank_account1.balance )

bank_account1.deposit(100)
print( 'After deposit 100: ', bank_account1.balance )

bank_account1.withdraw(200)
print( 'After withdraw 200. Expecting ERROR and no change in balance: ', bank_account1.balance )

## Now VIP account
print()
print("**** vip_bank_account2")
print( vip_bank_account2 )
print( 'Beginning: ', vip_bank_account2.balance )

vip_bank_account2.deposit(100)
print( 'After deposit 100:', vip_bank_account2.balance )

vip_bank_account2.withdraw(200)
print( 'After withdraw 200. No error for VIP:', vip_bank_account2.balance )
