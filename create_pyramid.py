# Take input from the user for number of rows in the pyramid
row = int(input('Enter the value of row: '))

# Initialize a counter to keep track of the total number of stars printed
count_star = count_space = 0

# Outer loop to handle the number of rows
for i in range(row):
    # Inner loop to print spaces before stars
    # (row - i - 1) spaces to center-align the pyramid
    for j in range(row - i - 1):
        print(' ', end=' ')
        count_space += 1
    
    # Inner loop to print stars
    # Number of stars in each row = 2*i + 1
    for j in range(2 * i + 1):
        print('*', end=' ')
        count_star += 1  # Increment star count for each star printed
    
    # Move to the next line after printing each row
    print()

# Print the total number of stars printed
print('Total number of stars:', count_star)
print('Total number of space:', count_space)
