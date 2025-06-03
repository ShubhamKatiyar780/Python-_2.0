# Create a Dictionary
# create dictionary using { }
d1 = {1: 'Geeks', 2: 'For', 3: 'Geeks'}
print(d1)
# create dictionary using dict() constructor
d2 = dict(a = "Geeks", b = "for", c = "Geeks")
print(d2)
# Using for loop
keys = ['p', 'q', 'r']
values = [5, 10, 15]
d = {} 
for i in range(len(keys)):
    d[keys[i]] = values[i]
print(d)


# Accessing Dictionary Items
d = { "name": "Alice", 1: "Python", (1, 2): [1,2,4] }
# Access using key
print(d["name"])
# Access using get()
print(d.get("name"))
print(d)


# Adding and Updating
d = {1: 'Programming', 2: 'with', 3: 'Python'}
# Adding a new key-value pair
d["age"] = 22
# Updating an existing value
d[1] = "Python dict"
print(d)


# Removing Dictionary Items
d1 = {'name':'shubham', 'age':24, 'branch':'MCA', 'marks':[10, 20]}
# Using del to remove an item
del d1["age"]
print(d1)
# Using popitem to removes and returns the last key-value pair.
key, val = d1.popitem()
print(f"Key: {key}, Value: {val}")
# Clear all items from the dictionary
d1.clear()
print(d1)

# Using pop() to remove an item and return the value
my_dict = {'name': 'Shubham', 'age': 25, 'city': 'Kanpur'}
# Pop an existing key
value = my_dict.pop('age')
print(value)        # Output: 25
print(my_dict)      # Output: {'name': 'Shubham', 'city': 'Kanpur'}
# Pop a non-existing key with default
value = my_dict.pop('country', 'India')
print(value)        # Output: India
# Pop a non-existing key without default (will raise error)
#value = my_dict.pop('country')  # Raises KeyError


# Iterating
d = {'name': 'Shubham', 'age': 25, 'city': 'Kanpur'}
# Iterate over keys
for key in d:
    print(key)
# Iterate over values
for value in d.values():
    print(value)
# Iterate over key-value pairs
for key, value in d.items():
    print(f"{key}: {value}")


# setdefault
my_dict = {'name': 'Shubham'}
# Example 1: Key exists
value1 = my_dict.setdefault('name', 'Unknown')
print("Example 1 - Value:", value1)            # Output: Shubham
print("Dictionary after Example 1:", my_dict)  # Output: {'name': 'Shubham'}
# Example 2: Key doesn't exist, default provided
value2 = my_dict.setdefault('age', 25)
print("\nExample 2 - Value:", value2)          # Output: 25
print("Dictionary after Example 2:", my_dict)  # Output: {'name': 'Shubham', 'age': 25}
# Example 3: Key doesn't exist, default NOT provided
value3 = my_dict.setdefault('city')
print("\nExample 3 - Value:", value3)          # Output: None
print("Dictionary after Example 3:", my_dict)  # Output: {'name': 'Shubham', 'age': 25, 'city': None}


# update() method
# Initial dictionary
my_dict = {'name': 'Shubham', 'age': 24}
# Example 1: Update with another dictionary
my_dict.update({'age': 26, 'city': 'Kanpur'})
print("After Example 1:", my_dict)
# Output: {'name': 'Shubham', 'age': 26, 'city': 'Kanpur'}
# Example 2: Update with keyword arguments
my_dict.update(country='India', age=27)
print("After Example 2:", my_dict)
# Output: {'name': 'Shubham', 'age': 27, 'city': 'Kanpur', 'country': 'India'}
# Example 3: Update with list of tuples
my_dict.update([('email', 'shubham@example.com'), ('age', 28)])
print("After Example 3:", my_dict)
# Output: {'name': 'Shubham', 'age': 28, 'city': 'Kanpur', 'country': 'India', 'email': 'shubham@example.com'}
# Example 4: Update with empty dictionary (no change)
my_dict.update({})
print("After Example 4:", my_dict)


# keys() method
d = {'name': 'Shubham', 'age': 24, 'city': 'Kanpur'}
k = d.keys()
# Adding a new key-value pair to the dictionary
# Dynamic nature of keys()
d['Country'] = "India"
print(k)


# items() method
a = {'A': 'Python', 'B': 'Java'}
# getting items
items = a.items()
# adding a new key-value pair
a['C'] = 'C++'
print(items)


# fromkeys() method
# Example 1: Create dictionary from list of keys with default value None
keys = ['name', 'age', 'city']
dict1 = dict.fromkeys(keys)
print("Example 1:", dict1)
# Output: {'name': None, 'age': None, 'city': None}
# Example 2: Create dictionary from list of keys with a given default value
dict2 = dict.fromkeys(keys, 'unknown')
print("Example 2:", dict2)
# Output: {'name': 'unknown', 'age': 'unknown', 'city': 'unknown'}
# Example 3: Create dictionary from string (each character becomes a key)
dict3 = dict.fromkeys("abc", 0)
print("Example 3:", dict3)
# Output: {'a': 0, 'b': 0, 'c': 0}
# Example 4: Create dictionary from tuple of keys
dict4 = dict.fromkeys(('x', 'y', 'z'), True)
print("Example 4:", dict4)
# Output: {'x': True, 'y': True, 'z': True}
# Example 5: Create empty dictionary (using empty iterable)
dict5 = dict.fromkeys([], 'default')
print("Example 5:", dict5)
# Output: {}


