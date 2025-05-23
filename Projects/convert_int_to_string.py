# Take input from the user
number = int(input('Enter a number: '))

# Initialize an empty string to store the reversed digits
result = ''

# Loop to extract digits from the number one by one (from right to left)
while number != 0:
    char = number % 10              # Get the last digit
    result = str(char) + result     # Add digit to the beginning of the result string
    number = number // 10           # Remove the last digit from the number

# Display the type of the original number (after processing, number will be 0)
print('Type of the original number (after processing):', type(number))

# Display the type of the result after converting digits to string
print('Type of the result after conversion:', type(result))
