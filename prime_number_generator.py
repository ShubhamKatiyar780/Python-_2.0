# Take input for the lower bound of the range
lower_range = int(input('Enter lower range: '))

# Take input for the upper bound of the range
upper_range = int(input('Enter upper range: '))

# Initialize a counter to count total prime numbers
count = 0

# Loop through each number from lower_range to upper_range (inclusive)
for i in range(lower_range, upper_range + 1):

    # Skip numbers less than 2 since 0 and 1 are not prime
    if i < 2:
        continue

    # Check if the number 'i' is divisible by any number from 2 to i-1
    for j in range(2, i):
        if i % j == 0:
            break  # Not a prime number
    else:
        # If the loop completes without break, 'i' is a prime number
        print(i)
        count += 1

# Print the total number of prime numbers found
print('Total prime numbers between', '(', lower_range, ':', upper_range, ')', 'is:', count)
