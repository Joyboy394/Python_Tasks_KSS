class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be positive.")
            return
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return
        if amount > self.balance:
            print("Insufficient balance.")
            return
        self.balance -= amount
        print(f"Withdrew {amount}. New balance: {self.balance}")

    def display_balance(self):
        print(f"Account Number: {self.account_number}, Balance: {self.balance}")


account1 = BankAccount(1001, 5000)

account1.display_balance()
account1.deposit(2000)
account1.withdraw(1000)
account1.withdraw(10000)
account1.display_balance()
