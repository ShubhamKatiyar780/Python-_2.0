# Create a dictionary with personal information
d = {'Name': 'Shubham Katiyar', 'Age': 24, 'Branch': 'Computer Science', 'City': 'Kanpur'}

# Print the original dictionary
print('Original Dictionary: ' + str(d))

# Convert the dictionary items (key-value pairs) into a list of tuples
tups = list(d.items())

# Swap the 2nd (index 1) and 4th (index 3) elements in the list
tups[1], tups[3] = tups[3], tups[1]

# Convert the list of tuples back into a dictionary after swapping
print('After Swaping: ' + str(dict(tups)))
