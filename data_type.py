# integer
print(1e308)  # pyhton can handle 1*10^308
print(1e309)  # pyhton can not handle 1*10^309 that by showing infinite
print(type(1308))

# Decimal/Float
print(1.7e308)  # pyhton can handle 1.7*10^308
print(1.6e309)  # pyhton can not handle 1.6*10^309 that by showing infinite
print(type(1.308))

# Boolean
print(True)
print(False)
print(type(True))

# String
print("I'm Shubham Katiyar")
print(type("Shubham"))

# Complex Number
print(5+6j)
print(type(1+3j))

# List = []
a = [1,5,'shubh', True, 1.852, 5+2j]
print(a)
print(type(a))

# Tuple = ()
b = (1,5,'shubh', True, 1.852, 5+2j)
print(b)
print(type(b))

# Sets = {}
c = {1,5,'shubh', True, 1.852, 5+2j}
print(c)
print(type(c))

# Dictionary = {'key': 'value'}
d = {'Name' : 'Shubham', 'Age' : 24, 'University' : 'LPU'}
print(d)
print(type(d))