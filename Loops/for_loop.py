# --------------------------
# For Loop using range()
# --------------------------
n = 4
for i in range(0, n):
    print(i)  # Prints numbers from 0 to 3

# --------------------------
# Iteration over a Set using for loop
# --------------------------
set1 = {1, 2, 3, 4, 5, 6}
for i in set1:
    print(i)  # Prints each element in the set (order is not guaranteed)

# --------------------------
# Iteration over a List using index
# --------------------------
list = ["Shubham", "Katiyar", "UP"]
for index in range(len(list)):
    print(list[index])  # Prints each item from the list by index
else:
    print("Inside Else Block")  # Executes after the for loop completes normally

# --------------------------
# Nested Loops
# --------------------------
for i in range(1, 5):  # Outer loop from 1 to 4
    for j in range(i):  # Inner loop runs i times
        print(i, end=' ')  # Print i on the same line
    print()  # Moves to the next line after inner loop finishes
