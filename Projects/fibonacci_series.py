# Define a recursive function to calculate Fibonacci numbers
def fibonacci(n):
    # Base case: Fibonacci of 0 is 0
    if n <= 0:
        return 0
    # Base case: Fibonacci of 1 is 1
    elif n == 1:
        return 1
    # Recursive case: F(n) = F(n-1) + F(n-2)
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Ask the user for the number of terms to print
n = int(input('Enter how many terms you want to print of the Fibonacci Sequence: '))

# Loop through and print the Fibonacci sequence up to n terms
for i in range(n):
    print(fibonacci(i), end=' ')
