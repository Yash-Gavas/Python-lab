class SavingAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.balance += amount
        print(f"Deposited: {amount}")

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount
        print(f"Withdrew: {amount}")

    def display_balance(self):
        print(f"Balance: {self.balance}")

# Creating an instance of SavingAccount with an initial balance of 100
account = SavingAccount(100)

# Displaying the initial balance
account.display_balance()

# Getting user input for deposit
try:
    deposit_amount = float(input("Enter amount to deposit: "))
    account.deposit(deposit_amount)
except ValueError as e:
    print(e)

# Getting user input for withdrawal
try:
    withdraw_amount = float(input("Enter amount to withdraw: "))
    account.withdraw(withdraw_amount)
except ValueError as e:
    print(e)

# Displaying the balance after deposit and withdrawal
account.display_balance()
