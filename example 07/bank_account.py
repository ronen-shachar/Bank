# כעת נוסיף קלאס נוסף Person

from person import Person

class BankAccount:
    def __init__(self, id: str, f_name: str, l_name: str):
        self.account_id: str = id
        self.person: Person = Person(f_name, l_name)
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
                         , f_name='Business do not need f/l name'
                         , l_name='Business do not need f/l name')
        self.company_name = company_name


bank_account1 = BankAccount('1245', 'Moshe', 'Cohen')
business_bank_account2 = BusinessBankAccount('1000', 'Tesla')
vip_bank_account2 = VIPBankAccount('8982', 'David', 'Lev')

print("**** bank_account1")
print( bank_account1 )
print( bank_account1.person.get_full_name() )

## Now Business account
print()
print("**** business_bank_account2")
print( business_bank_account2 )
print( business_bank_account2.person.get_full_name() )

## Now VIP account
print()
print("**** vip_bank_account2")
print( vip_bank_account2 )
print( vip_bank_account2.person.get_full_name() )
