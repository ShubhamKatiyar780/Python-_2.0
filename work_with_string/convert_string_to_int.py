# Function to manually convert a string number to an integer
def int_converter(str):
    result = 0  # Initialize the final result

    # Check if the number is negative
    if str[0] == '-':
        start_index = 1            # Start from index 1 to skip '-'
        check_negative = True      # Flag to mark the number as negative
    else:
        start_index = 0            # Start from index 0 for positive numbers
        check_negative = False     # Number is positive

    # Loop through each digit from left to right
    for i in range(start_index, len(str)):
        place_value = 10**(len(str) - (i + 1))       # Calculate the place value of the digit (e.g., 1000s, 100s, 10s, etc.)
        digit_value = ord(str[i]) - ord('0')         # Convert character to integer using ASCII
        result += place_value * digit_value          # Add to result based on place value

    # If the original number was negative, return the negative result
    if check_negative:
        return -1 * result
    else:
        return result

# Take input from user
str = input('Enter a number: ')

# Print the type before and after conversion
print(type(str))                    # <class 'str'>
print(type(int_converter(str)))     # <class 'int'>
