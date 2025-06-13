words = ["apple", "banana", "cherry"]
print(max(words, key=len))  # Output: "banana" (longest word)


# Function to find the most frequent element in a list
def most_frequent(List):
    # Convert the list to a set to get unique elements,
    # then use max() to find the element with the highest count in the original list.
    return max(set(List), key=List.count)
# Sample input list
List = [2, 1, 2, 2, 1, 3]
# Call the function and print the result
print(most_frequent(List))


a = [1, 2, 3]
b = [4, 5, 6]
# Use the unpacking operator to merge the lists
c = [*a, *b]
print(c)


a = [[4, 3, 5], [1, 2, 3], [3, 7, 4]]
b = [[1, 3], [9, 3, 5, 7], [8]]
# Combine corresponding sublists from a and b using list comprehension and zip
a = [x + y for x, y in zip(a, b)]  # x from a, y from b → x + y means concatenating two lists
print(a)


a = [[4, 3, 5], [1, 2, 3], [3, 7, 4]]
b = [[1, 3], [9, 3, 5, 7], [8]]
# Same operation as above using map and lambda instead of list comprehension
# zip(a, b) pairs corresponding sublists, and lambda x: x[0] + x[1] merges them
a = list(map(lambda x: x[0] + x[1], zip(a, b)))
print(a)


a = [[4, 3, 5], [1, 2, 3], [3, 7, 4]]
b = [[1, 3], [9, 3, 5, 7], [8]]
# Loop through each index of a and extend each sublist with corresponding sublist in b
for i in range(len(a)):
    a[i].extend(b[i])  # Adds all elements of b[i] to a[i] in-place
print(a)


# All elements concatenation across lists using list comprehension
# Step 1: Initializing lists
test_list1 = ["India", "is", "Great"]
test_list2 = ["love", "Army"]
# Step 2: Printing original lists
print("The original list 1 is : " + str(test_list1))
print("The original list 2 is : " + str(test_list2))
# Step 3: Creating all possible pairs using nested list comprehension
# For each element 'a' in test_list1 and each element 'b' in test_list2,
# create a tuple (a, b)
temp = [(a, b) for a in test_list1 for b in test_list2]
res = [x + ' ' + y for (x, y) in temp]
# Step 5: Printing the final result
print("The paired combinations : " + str(res))


# Define three lists with similar and differing values
a = [1, 2, 'Shubham']   # List 'a' with integer and string elements
b = [1, 2, 'Shubham']   # List 'b' has the same values as list 'a'
c = [1, 2, 'shubham']   # List 'c' differs from 'a' and 'b' in the string element (case-sensitive)
# Compare entire lists 'a' and 'b' element-wise in order
print(a == b)  # True, because all elements and their order are the same
# Compare entire lists 'a' and 'c' element-wise in order
print(a == c)  # False, because 'Shubham' != 'shubham' (case-sensitive comparison)
# Create a list of boolean results comparing corresponding elements of 'a' and 'b'
result1 = [i == j for i, j in zip(a, b)]
print(result1)  # [True, True, True], each element in 'a' matches with 'b'
# Create a list of boolean results comparing corresponding elements of 'a' and 'c'
result2 = [i == k for i, k in zip(a, c)]
print(result2)  # [True, True, False], only the string element differs due to case


# Combining Two Sorted Lists
a = [1, 3, 5, 7]
b = [8 ,2, 9, 4, 6]
c = a + b # [1,3,5,7,8,2,9,4,6]
for i in range(1, len(c)):
    for j in range(len(c)-i):
        if c[j] > c[j+1]:
            c[j], c[j+1] = c[j+1], c[j]
print(c)


# Unpack List
# List with five elements
li = [1, 2, 3, 4, 5]
# Unpacking the first two elements and collecting the rest
a, b, *rest = li
print(a)      
print(b)    
print(rest)