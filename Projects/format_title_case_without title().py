# Take input from the user
input_str = input('Enter a string: ')

# Initialize an empty list to store processed words
result = []

# Split the input string into words using split()
for i in input_str.split():
    # Capitalize the first letter, make the rest lowercase
    result.append(i[0].upper() + i[1:].lower())

# Join the words back into a single string with spaces
print(' '.join(result))
