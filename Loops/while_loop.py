# --------------------------
# While Loop
# --------------------------
cnt = 0
while (cnt < 3):       # Loop will run as long as cnt is less than 3
    cnt = cnt + 1       # Increment cnt by 1
    print("Hello Shubham")  # Prints message 3 times

# --------------------------
# While Loop with else block
# --------------------------
cnt = 0
while (cnt < 3):       # Loop will run while cnt is less than 3
    cnt = cnt + 1       # Increment cnt
    print("Hello Katiyar")  # Prints message 3 times
else:
    print("In Else Block")  # Executes after while loop finishes normally (no break)

# --------------------------
# Infinite While Loop
# --------------------------
count = 0
while (count == 0):    # Condition is always true (count remains 0)
    print("Hello Geek")     # Will print this infinitely
