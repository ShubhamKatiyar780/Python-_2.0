# Take input from the user for the number of rows in the pyramid pattern
n = int(input('Enter a number: '))

# Outer loop for each row from 1 to n
for i in range(1, n + 1):
    
    # First inner loop: print numbers in ascending order from 1 to i
    for j in range(1, i + 1):
        print(j, end=' ')
    
    # 'else' here is attached to the 'for' loop, not a conditional
    # After the ascending part, print numbers in descending order
    # from (j - 1) down to 1 to complete the palindrome
    else:
        for k in range(j - 1, 0, -1):
            print(k, end=' ')
    
    # Move to the next line after printing each row
    print()
