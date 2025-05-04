def duplicate_removal(s):
    a = set()          # Set to keep track of already seen characters
    result = ''        # String to store the final result without duplicates

    for char in s:     # Loop through each character in the input string
        if char not in a:    # If character hasn't been added yet
            a.add(char)      # Add character to the set
            result += char   # Append character to result string

    return result       # Return the final string with duplicates removed

# Input string with mixed case
s = 'ShuBHaM KaTiYAr'

# Output after removing duplicates (case-sensitive)
print(duplicate_removal(s))
