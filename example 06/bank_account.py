# כעת נוסיף קלאס יורש נוסף
# שימו לב כי הוא אינו דורש שם בעל החשבון אלא מקבע אותו
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


class BusinessBankAccount(BankAccount):

    def __init__(self, account_id, company_name: str):
        super().__init__(id=account_id
                         , f_name='Business do not nerd f/l name'
                         , l_name='Business do not nerd f/l name')
        self.company_name = company_name


bank_account1 = BankAccount('1245', 'Moshe', 'Cohen')
business_bank_account2 = BusinessBankAccount('1000', 'Tesla')

print("**** bank_account1")
print( bank_account1 )
print( bank_account1.__dict__ )

## Now Business account
print()
print("**** business_bank_account2")
print( business_bank_account2 )
print( 'Pay attention to first and last name: ', business_bank_account2.__dict__ )
