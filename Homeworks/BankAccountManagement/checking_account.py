from account import Account

class CheckingAccount(Account):
    def __init__ (self, owner, account_number, balance=0.0):
        super().__init__(owner, account_number, balance)
    