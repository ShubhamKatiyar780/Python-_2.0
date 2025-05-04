# Function to calculate the minimum distance between two words in a list
def min_distance(str, word1, word2):
    index1 = index2 = -1               # Initialize positions of word1 and word2 as -1 (not found yet)
    minimum_distance = float('inf')    # Set initial minimum distance to infinity

    # Loop through each word in the list with its index
    for i, word in enumerate(str):
        if word == word1:
            index1 = i                 # Update index1 if word1 is found
        elif word == word2:
            index2 = i                 # Update index2 if word2 is found

        # If both words have been seen at least once, calculate their distance
        if index1 != -1 and index2 != -1:
            # Update minimum distance if the current distance is smaller
            minimum_distance = min(minimum_distance, abs(index1 - index2))

    return minimum_distance             # Return the smallest distance found

# List of words (input text as a list of strings)
S = ["the", "quick", "the", "fox", "quick"]

# Target words to find the distance between
word1 = "the"
word2 = "fox"

# Output the result
print(f'''Minimum distance between "{word1}" and "{word2}" is: ''', min_distance(S, word1, word2))
