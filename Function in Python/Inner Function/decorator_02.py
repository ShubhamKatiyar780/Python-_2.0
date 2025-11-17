# Define decorator 1 - converts function's return value to uppercase
def decor1(function):
    def wrapper():
        return function().upper()  # Calls original function and converts result to uppercase
    return wrapper   # Returns the wrapper function

# Define decorator 2 - splits function's return value into a list of words
def decor2(function):
    def wrapper():
        return function().split()  # Calls original function and splits result by whitespace
    return wrapper  # Returns the wrapper function

# Apply decorators to get_name function
# Note: Decorators are applied from bottom to top (decor1 first, then decor2)
@decor2
@decor1
def get_name():
    # Gets user input for first and last name
    first_name = input('Enter your first name: ')
    last_name = input('Enter your last name: ')
    full_name = first_name + ' ' + last_name  # Combines names into full name string
    return full_name  # Returns the full name

# This commented line shows what the decorators are doing behind the scenes:
# a = decor2(decor1(get_name))
# print(a())

# Call the decorated function and print the result
print(get_name())