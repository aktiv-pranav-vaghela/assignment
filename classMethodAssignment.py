class BankAccount:
    def __init__(self, account_number, holder_name, initial_balance=0.0):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                print(f"Withdrew {amount}. New balance: {self.balance}")
            else:
                print("Insufficient balance.")
        else:
            print("Withdrawal amount must be positive.")

    def display_balance(self):
        print(f"Account Number: {self.account_number}")
        print(f"Account Holder: {self.holder_name}")
        print(f"Current Balance: {self.balance}")

class SavingsAccount(BankAccount):
    def __init__(self, account_number, holder_name, initial_balance=0.0, interest_rate=0.01):
        super().__init__(account_number, holder_name, initial_balance)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        return self.balance * self.interest_rate

    def apply_interest(self):
        interest = self.calculate_interest()
        self.balance += interest
        print(f"Interest of {interest} applied. New balance: {self.balance}")


class CurrentAccount(BankAccount):
    def __init__(self, account_number, holder_name, initial_balance=0.0, overdraft_limit=0.0):
        super().__init__(account_number, holder_name, initial_balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount > 0:
            if self.balance + self.overdraft_limit >= amount:
                self.balance -= amount
                print(f"Withdrew {amount}. New balance: {self.balance}")
            else:
                print("Withdrawal exceeds overdraft limit.")
        else:
            print("Withdrawal amount must be positive.")


Person1 = SavingsAccount(4000031028,"Pranav",2000,0.06)
print("The name of the Bank account holder is:",Person1.holder_name)
print(f"The account number of the Bank account holder named {Person1.holder_name} is:",Person1.account_number)
print(f"The initial balance of the Bank account holder named {Person1.holder_name} is:",Person1.balance)
Person1.deposit(4000)
Person1.withdraw(1000)
Person1.display_balance()

print("Calculated interest is :",Person1.calculate_interest())
Person1.apply_interest()

Person2 = CurrentAccount(5000031028,"Tejas",100000,500000)
print("The name of the Bank account holder is:",Person2.holder_name)
print(f"The account number of the Bank account holder named {Person2.holder_name} is:",Person2.account_number)
print(f"The initial balance of the Bank account holder named {Person2.holder_name} is:",Person2.balance)
Person2.deposit(4000)
Person2.withdraw(1000)
Person2.display_balance()
Person2.withdraw(400000)