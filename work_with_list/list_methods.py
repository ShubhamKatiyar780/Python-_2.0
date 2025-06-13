# Create a list 'a' with four elements
a = ['Learn', 'Quiz', 'Practice', 'Contribute']

# 'b' is assigned to reference the same list as 'a' (both point to the same object in memory)
b = a

# 'c' is a shallow copy of 'a' using slicing (creates a new list object with the same elements)
c = a[:]

# Print memory addresses (IDs) of a, b, and c
print(id(a))  # ID of list 'a'
print(id(b))  # ID of list 'b' (same as 'a' since b = a)
print(id(c))  # ID of list 'c' (different from 'a' and 'b')

# Modify the first element of list 'b'
b[0] = 'Code'  # Since 'b' and 'a' refer to the same list, this also affects 'a'

# Modify the second element of list 'c'
c[1] = 'Mcq'  # 'c' is a separate copy, so this change doesn't affect 'a' or 'b'

# Print all three lists to observe the differences
for i in (a, b, c):
    print(i)


# Adding elements in to list
# append()
a.append('Python')  # add at the end of the list
print(a)
# extend()
c.extend('abcd')    # add multiple elements to the end of the list
print(c)
b.extend([1,2,3])
print(b)
# insert()
c.insert(2, 'shubham')  # add at a specific position
print(c)


# Removing elements from the list
#remove()
a = [10, 20, 30, 40, 50]
a.remove(30)    # Removes the first occurrence of 30
print("After remove(30):", a)
popped_val = a.pop(1)   # Removes the element at index 1 (20) and by default removes from the end
print("Popped element:", popped_val)
print("After pop(1):", a)
del a[0]  # Deletes the first element (10)
print("After del a[0]:", a)
a.clear()   # This keeps 'a' as an empty list
# del a   # Delete the variable 'a'

# Get list as input Using split() Method
# Get user input and split it into a list
user_input = input("Enter elements separated by space: ").split()
print("List:", user_input)


# Get list as input Using map()
# Get user input, split it, and convert to integers
user_input = list(map(int, input("Enter numbers separated by space: ").split()))
print("List:", user_input)

# Get list as input Using map()
nums = [1, 2, 3, 4]
def double(x):
    return x * 2
result = map(double, nums)
print(list(result))  # Output: [2, 4, 6, 8]


a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Get every second element from the list
# starting from the beginning
b = a[::2]
print(b)
# Get every third element from the list
# starting from index 1 to 8(exclusive)
c = a[1:28:3]
''' Out-of-bound slicing
In Python, list slicing allows out-of-bound indexing without raising errors.
If we specify indices beyond the list length then it will simply return the available items.   '''
print(c)


# Using filter function
print('Using filter function')
def is_even(n):
    return n % 2 == 0
numbers = [1, 2, 3, 4, 5, 6]
result = filter(is_even, numbers)
print(list(result))  # Output: [2, 4, 6]


# Using index() Method
# .index(value, start, stop)
print('Using index() Method')
nums = [10, 20, 30, 20, 40, 50, 20, 60, 20]
print(nums.index(20, 3, 7))  # Output: 3 (starts searching from index 2)


# Creating a Matrix of user-defined order (e.g., 5*5)
# Initialize an empty list to store the matrix
matrix = []
# Take matrix order input in 'rows*columns' format (e.g., 5*5)
order = input('Enter the order of matrix (rows*columns): ').split('*')
# Loop through each row index (starting from 1 to number of rows)
for i in range(1, int(order[0]) + 1):
    row = []  # Initialize an empty row
    # Loop through each column index (starting from 1 to number of columns)
    for j in range(1, int(order[1]) + 1):
        # Take input for each matrix element
        val = int(input(f"Enter element at [{i}][{j}]: "))
        row.append(val)  # Add the element to the current row
    # Add the completed row to the matrix
    matrix.append(row)
# Print the entire matrix
print("The entered matrix is:", matrix)

