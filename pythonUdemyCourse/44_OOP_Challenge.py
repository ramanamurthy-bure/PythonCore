class BankAccount():
    def __init__(self,accnt_owner,accnt_balance=0):
        self.accnt_owner = accnt_owner
        self.accnt_balance = accnt_balance

    def deposit(self,deposit_amount):
        self.accnt_balance = self.accnt_balance + deposit_amount

    def withdraw(self,withdraw_amount):
        if withdraw_amount >= self.accnt_balance:
            print("In sufficient balance")
        else:
            print("Withdrawl Accepted")
            self.accnt_balance = self.accnt_balance - withdraw_amount

    def __str__(self):
        return f"Owner:{self.accnt_owner}  \nAvailable account balance: {self.accnt_balance}"

my_accnt = BankAccount('Ramana',50000)
print(my_accnt.accnt_owner)
print(my_accnt.accnt_balance)
my_accnt.deposit(20000)
print(my_accnt.accnt_balance)
my_accnt.withdraw(4)
print(my_accnt.accnt_balance)
print(my_accnt)


