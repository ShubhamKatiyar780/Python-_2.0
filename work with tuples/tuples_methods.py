# Create a Tuple
# Using parentheses
my_tuple = (1, 2, 3)
# Without parentheses (Python allows it in many cases)
another_tuple = 4, 5, 6
# A single-element tuple must have a comma
single_element = (10,)


# Tuple Operations
t1 = (1, 2)
t2 = (3, 4)
# Concatenation
print(t1 + t2)  # Output: (1, 2, 3, 4)
# Repetition
print(t1 * 2)   # Output: (1, 2, 1, 2)


#  Using * for Variable-Length Unpacking
a, *b = (1, 2, 3, 4, 5)
print(a)   
print(b)


# Tuple Unpacking with * in Function Arguments
def add(*args):
    return sum(args)
print(add(1, 2, 3, 4))

# Accessing Values in Tuples
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple[1:4])


# Creating a Tuple From dict
my_dict = {'apple': 1, 'banana': 2, 'cherry': 3}
my_tuple = tuple(my_dict.items())
print(my_tuple)


# max(), min()
my_tuple = tuple((1, 2, 3))
print(max(my_tuple))
print(min(my_tuple))


# sum()
print(sum(my_tuple))


# sorted() -->   It returns a new sorted list containing the elements of the tuple
my_tuple = tuple((3, 2, 1))
sorted_tuple = tuple(sorted(my_tuple))
print(sorted_tuple)


