# Function to calculate the sum of each column in a 2D list
def column_sum(lst):
    res = []  # This will store the sum of each column

    # Outer loop runs for each column index
    for i in range(len(lst[0])):  # Use len(lst[0]) to get number of columns
        sum = 0  # Initialize sum for the current column

        # Inner loop runs through each row to access column 'i'
        for j in range(len(lst)):
            sum += lst[j][i]  # Add the value at row j and column i

        res.append(sum)  # Append the total sum of column i to the result list

    return res  # Return the list containing column-wise sums

# Sample 2D list
lst = [[1, 5, 3], [2, 7, 8], [4, 6, 9]]

# Call the function and print the result
print(column_sum(lst))  # Output: [7, 18, 20]
