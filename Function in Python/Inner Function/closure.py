# Outer function takes 'exponent' as argument
def power_function(exponent):
    # Inner function uses 'exponent' from outer scope
    def power(base):
        return base ** exponent  # Calculates base raised to exponent
    return power  # Returns the inner function

# Creating 'square' function by fixing exponent = 2
square = power_function(2)

# Creating 'cube' function by fixing exponent = 3
cube = power_function(3)

# Value to test
x = 5

# Calling both functions
print('square of the', x, ':', square(x))  # 5^2 = 25
print('cube of the', x, ':', cube(x))      # 5^3 = 125
