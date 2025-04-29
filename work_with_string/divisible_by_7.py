# Function to check divisibility of a number by 7 using a shortcut method
def isdivisible7(num):
    # Step 1: Get the last digit and multiply it by 2
    a = (int(num[-1])) * 2

    # Step 2: Get the length of the number (number of digits)
    b = len(num)

    # Step 3: Get the number excluding the last digit
    c = int(num[:(b-1)])

    # Step 4: Subtract twice the last digit from the rest of the number
    # If the result is divisible by 7, then the original number is divisible by 7
    if abs(c - a) % 7 == 0:
        return 1   # Divisible by 7
    else:
        return 0   # Not divisible by 7
    
print(isdivisible7('49'))   # Output: 1 ✅ (49 is divisible by 7)
print(isdivisible7('203'))  # Output: 1 ✅ (203 is divisible by 7)
print(isdivisible7('18'))   # Output: 0 ❌ (18 is not divisible by 7)