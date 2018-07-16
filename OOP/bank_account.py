class BankAccount:

    _acct_number = 400 #? This is a class attribute

    def __init__(self, _acct_name):
        self._acct_name = _acct_name
        BankAccount._acct_number += 1 #* Will increment the acct_number every instantiation
        self._acct_balance = 5000

    def deposit(self, cash_deposit):
        self._acct_balance += cash_deposit
        print(f"{self._acct_name} has deposited {cash_deposit} to his/her account")
        print(f"Balance: {self._acct_balance}")

    def withdraw(self, cash_withdraw):
        if self._acct_balance < cash_withdraw:
            print("Not Enough Balance!")
        else:
            self._acct_balance -= cash_withdraw
            print(f"{self._acct_name} has withdrawed {cash_withdraw} to his/her account")
            print(f"Remaining Balance: {self._acct_balance}")

    def get_balance(self):
        print(f"{self._acct_name} has P{self._acct_balance} left in his/her account")

    def get_info(self):
        print(f"Name: {self._acct_name}\nAccount No.: {self._acct_number}")

user1 = BankAccount("Jeg Ramos")
user1.get_balance()
user1.get_info()
user1.deposit(9500)
user1.get_balance()
user1.withdraw(500)
user1.get_info()

user2 = BankAccount("Carlo Ramos")
user2.get_balance()
user2.get_info()
user2.deposit(9500)
user2.get_balance()
user2.withdraw(80000)
user2.get_balance()
user2.get_info()