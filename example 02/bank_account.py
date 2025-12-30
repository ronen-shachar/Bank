# הוספנו properties אל ה-class
# שים לב שלמרות שאלו שני מופעים שונים (בהרצה תראה כתובות זהות)
# ערכי הproperties שלהם זהים

class BankAccount:
    def __init__(self):
        self.account_id: str = 'An example initial Id'
        self.first_name: str = 'Moshe'
        self.last_name: str = 'Cohen'
        self.balance: float = 0.0

bank_account1 = BankAccount()
bank_account2 = BankAccount()

print("**** bank_account1")
print( bank_account1 )
print( bank_account1.__dict__ )

print("**** bank_account2")
print( bank_account2 )
print( bank_account2.__dict__ )
