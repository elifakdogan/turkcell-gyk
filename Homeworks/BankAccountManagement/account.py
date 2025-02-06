class Account:
    def __init__(self, owner, account_number, balance=0.0):
        self.owner = owner
        self.account_number = account_number
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print (f"{self.owner} isimli müşterinin {self.account_number} numaralı hesabına {amount} ₺ para yatırıldı. Güncel bakiye : {self.__balance} ₺")
        else:
            print("Geçersiz tutar girişi!")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print (f"{self.owner} isimli müşterinin {self.account_number} numaralı hesabından {amount} ₺ para çekildi. Güncel bakiye : {self.__balance} ₺")
        else:
            print("Yetersiz bakiye veya geçersiz tutar girişi!")

    def show_balance(self):
        return f"Hesap Sahibi: {self.owner} - Hesap No: {self.account_number} - Bakiye: {self.__balance} ₺"