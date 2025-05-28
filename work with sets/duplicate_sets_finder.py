# Python program to find duplicate sets in a list of sets

# Initializing list of sets
test_list = [{4, 5, 6, 1}, {6, 4, 1, 5}, {1, 3, 4, 3}, 
             {1, 4, 3}, {7, 8, 9}]

# Printing original list
print("The original list is : " + str(test_list))

# Creating an empty set to store unique duplicate sets (as frozensets)
result = set()

# Using nested loops to compare each set with every other set
for i in range(len(test_list)):
    for j in range(i + 1, len(test_list)):
        # If two sets are equal (same elements, order doesn't matter in sets)
        if test_list[i] == test_list[j]:
            # Add as frozenset because sets can't be added to another set
            result.add(frozenset(test_list[i]))

# Converting result to list and printing
print("Duplicate sets list : " + str(list(result)))

# This code is contributed by Jyothi Pinjala
