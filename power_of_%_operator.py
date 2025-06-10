# It works similarly to format(), but the syntax is a little different and inspired by the C language style.
# Basic Syntax: "format string" % (value1, value2, ...)


# Example 1: Single value
name = "Shubham"
print("Hello %s" % name)
# Output: Hello Shubham

# Example 2: Multiple values
name = "Shubham"
age = 25
print("My name is %s and I am %d years old." % (name, age))
# Output: My name is Shubham and I am 25 years old.

# Example 3: Float formatting
price = 49.9999
print("Price: %.2f" % price)
# Output: Price: 50.00

# Example 3: Octal formatting
num = 15
print("Octal: %o" % num)
# Output: Octal: 17