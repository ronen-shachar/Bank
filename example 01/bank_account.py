class BankAccount:
    def __init__(self):
        self.account_id: str = 'An example initial Id'
        self.first_name: str = 'Moshe'
        self.last_name: str = 'Cohen'
        self.balance: float = 0.0

bank_account1 = BankAccount()
print( bank_account1.__dict__ )