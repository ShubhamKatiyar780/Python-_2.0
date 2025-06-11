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