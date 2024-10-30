class BankAccount:
    def __init__(self, account_balance):
        self.account_balance = account_balance

    def deposit(self, amount):
        if amount > 0:
            self.account_balance += amount
            return self.account_balance
        else:
            print("Amount must be a positive number")

    def withdraw(self, amount):
        if self.account_balance >= amount:
            self.account_balance -= amount
            return True
        else:
            return False
    def display_balance(self):
        print(f"Your current balance is {self.account_balance}")


