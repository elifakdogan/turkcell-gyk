from checking_account import CheckingAccount
from saving_account import SavingAccount

account1 = CheckingAccount("Elif Akdoğan",12345,1000)
account2 = SavingAccount("Elif Akdoğan",123456,5000)

account1.deposit(500)
account1.withdraw(300)
account1.show_balance()

account2.calculate_interest()
account2.withdraw(1000)
account2.show_balance()