from account import Account

class SavingAccount(Account):
    def __init__(self, owner, account_number, balance=0.0, interest_rate=0.05):
        super().__init__(owner, account_number, balance)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        interest = self._Account__balance * self.interest_rate
        print(f"Hesaplanan faiz oranı: {interest} ₺")

    def withdraw(self, amount):    
        penalty = amount * 0.02
        total_amount = amount + penalty
        if 0 < total_amount <= self._Account__balance:
            self._Account__balance -= total_amount
            print(f"{self.owner} isimli müşterinin {self.account_number} numaralı hesabından {penalty} ₺ ceza ile {amount} ₺ para çekildi. Kalan bakiye: {self._Account__balance}")
        else:
            print("Yetersiz!")