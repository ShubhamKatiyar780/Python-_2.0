# Take input from the user
input_str = input('Enter a string: ')

# Initialize an empty list to store words
result = []

# Temporary string to build individual words
temp = ''

# Iterate through each character in the input string
for i in input_str:
    # If the character is not a space, add it to the current word
    if i != ' ':
        temp += i
    else:
        # If a space is encountered, add the current word to result and reset temp
        result.append(temp)
        temp = ''

# Append the last word after the loop ends
result.append(temp)

# Print the list of words
print(result)
