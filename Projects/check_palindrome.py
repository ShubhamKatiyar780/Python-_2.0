# Take input from the user
input_str = input('Enter a string: ')

# ---------- Method 1: Character-by-character comparison ----------
# Loop from the start to the middle of the string
for i in range(0, len(input_str) // 2):
    # Compare the ith character from start and end
    if input_str[i] != input_str[len(input_str) - i - 1]:
        # If characters don't match, it's not a palindrome
        print("Given string", "'", input_str, "'", 'is not a palindrome')
        break
else:
    # This else runs only if the loop wasn't broken (i.e., it's a palindrome)
    print("Given string", "'", input_str, "'", 'is a palindrome')



# ---------- Method 2: Using string reversal ----------
# Reverse the string using slicing
reverse_str = input_str[::-1]

# Check if original and reversed strings are the same
if input_str == reverse_str:
    print("Given string", "'", input_str, "'", 'is a palindrome')
else:
    print("Given string", "'", input_str, "'", 'is not a palindrome')
