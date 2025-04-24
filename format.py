# full syntax str.format(*args, **kwargs)
'''Where:
str = a string that contains one or more placeholders ({})
*args = positional arguments
**kwargs = keyword arguments (named values)'''

# 1. Positional arguments (*args)

# You can pass values without names.
print("{} {}".format("Shubham", 25))
# Output: Shubham 25
# You can also use index to reorder:
print("{1} is {0} years old".format(25, "Shubham"))
# Output: Shubham is 25 years old

# 2. Keyword arguments (**kwargs)
# Pass values with names and refer to them using {name}:
print("{name} is {age} years old".format(name="Shubham", age=25))
# Output: Shubham is 25 years old

# 3. Formatting options inside {}
# You can use colons (:) to format:
price = 49.9999
print("Price: {:.2f}".format(price))  # 2 decimal places
# Output: Price: 50.00

num = 5
print("Binary: {:b}, Hex: {:x}".format(num, num))
# Output: Binary: 101, Hex: 5