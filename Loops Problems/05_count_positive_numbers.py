# Problem: Given a list of numbers, count how many are positive.

# List of numbers (both positive and negative)
numbers = [1, -2, 3, -4, 5, 6, -7, -8, 9, 10]

# Counter to store number of positive values
count = 0

# Loop through each number in the list
for num in numbers:
    # Check if the number is positive
    if num > 0:
        # Increase the counter
        count += 1

# Print the total number of positive values
print('Total Positive numbers:', count)
