class MyException(Exception):
    def __init__(self, msg):
        print(msg)


class Bank:
    def __init__(self, balance = 0.0):
        # Initialize bank account with initial balance
        # Double underscore makes balance private (encapsulation)
        self.__balance = balance

    def get_balance(self):
        # Return formatted balance string with 2 decimal places
        return f"Balance: {self.__balance:.2f}"
    
    def deposit(self, amount):
        # Validate that deposit amount is not negative
        if amount < 0:
            raise MyException('amount cannot be negative')
        # Add amount to current balance
        self.__balance += amount
        
    
    def withdraw(self, amount):
        # Validate that withdrawal amount is not negative
        if amount < 0:
            raise MyException('amount cannot be negative')
        # Check if sufficient funds are available
        if self.__balance < amount:
            raise MyException('insufficient balance')
        # Subtract amount from current balance
        self.__balance -= amount


# Create a new bank customer with default balance (0.0)
customer1 = Bank()

# Display initial balance
print(customer1.get_balance())

# Attempt to deposit money with error handling
try:
    customer1.deposit(1500.99948121)
except MyException as e:
    pass
else:
    # Execute if deposit is successful
    print(f"Balance after deposit: {customer1.get_balance()}")

# Attempt to withdraw money with error handling
try:
    customer1.withdraw(500.50)
except MyException as e:
    pass
else:
    # Execute if withdrawal is successful
    print(f"Remaining Balance: {customer1.get_balance()}")