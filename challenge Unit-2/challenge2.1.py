class BankAccount:
    def _init_(self, account_number, account_holder_name, initial_balance=0.0):
        self._account_number = account_number
        self._account_holder_name = account_holder_name
        self._account_balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self._account_balance += amount
            return f"Deposited ${amount}. New balance: ${self._account_balance}"
        else:
            return "Invalid deposit amount. Please enter a positive value."

    def withdraw(self, amount):
        if 0 < amount <= self._account_balance:
            self._account_balance -= amount
            return f"Withdrew ${amount}. New balance: ${self._account_balance}"
        elif amount > self._account_balance:
            return "Insufficient funds. Cannot withdraw that amount."
        else:
            return "Invalid withdrawal amount. Please enter a positive value."

    def display_balance(self):
        return f"Account balance for {self._account_holder_name}: ${self._account_balance}"

# Create an instance of the BankAccount class
account = BankAccount("123456", "John Doe", 1000.0)

# Test deposit and withdrawal functionality
print(account.display_balance())
print(account.deposit(500))
print(account.withdraw(200))
print(account.withdraw(1500))  # Should display an error message