# Recursive function to calculate factorial of a number
def factorial(n):
    if n == 0:  # Base case: factorial of 0 is 1
        return 1
    else:
        return n * factorial(n-1)  # Recursive call

print(factorial(5))  # Output: 120 (5 * 4 * 3 * 2 * 1)


# Recursive function to calculate the nth Fibonacci number
def fibonacci(n):
    # Base cases
    if n == 0:
        return 0
    elif n == 1:
        return 1
    # Recursive case: sum of the two previous Fibonacci numbers
    else:
        return fibonacci(n-1) + fibonacci(n-2)
for i in range(11):
    print(fibonacci(i), end=' ')  # Output: 55 (11th Fibonacci number)
print()


# ----------------------- Types of Recursion -----------------------

# Tail Recursion: the recursive call is the last operation in the function
def tail_fact(n, acc=1):
    if n == 0:  # Base case: return the accumulated result
        return acc
    else:
        return tail_fact(n-1, acc * n)  # Recursive call with updated accumulator

# Non-Tail Recursion: the recursive call is followed by another operation (multiplication here)
def nontail_fact(n):
    if n == 0:  # Base case
        return 1
    else:
        return n * nontail_fact(n-1)  # Recursive call followed by multiplication

# Example usage
print(tail_fact(6))      # Output: 720 (Tail-recursive version of factorial)
print(nontail_fact(7))   # Output: 5040 (Non-tail-recursive version of factorial)
