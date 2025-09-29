class BankAccount:
    def __init__(self, account_number, balance=0):
        # private attributes using double underscore
        self.__account_number = account_number
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}. New balance: {self.__balance}")
        else:
            print("Deposit amount must be positive!")

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient balance! Withdrawal denied.")
        elif amount <= 0:
            print("Withdrawal amount must be positive!")
        else:
            self.__balance -= amount
            print(f"Withdrew {amount}. New balance: {self.__balance}")


    def get_balance(self):
        return self.__balance

account = BankAccount("123456789", 1000)

account.deposit(500)
account.withdraw(2000)
account.withdraw(300)
print(account.get_balance())
