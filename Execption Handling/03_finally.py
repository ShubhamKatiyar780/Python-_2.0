try:
    # Define the file path as a string
    file = 'C:/Users/katiy/OneDrive/Desktop/Python-_2.0/File Handling/samplefile.txt'
    
    # Attempt to open the file in read mode
    # This may raise FileNotFoundError if the file doesn't exist
    # or other exceptions like PermissionError if access is denied
    f = open(file, 'r')

# Handle the specific exception when the file cannot be found
except FileNotFoundError:
    print("No such file or directory")

# Catch any other exceptions that aren't handled by the specific block above
except Exception as e:
    # Print the exception message (note: the f-string is inside quotes so it won't format)
    print(f"An exception occurred {e}")

# This block executes ONLY if no exceptions occurred in the try block
else:
    # Read and print the entire contents of the file
    # end='' prevents adding an extra newline at the end
    print(f.read(), end='')

# This block ALWAYS executes, regardless of whether an exception occurred or not
finally:
    # Close the file to free up system resources
    # Important: This will run even if an exception occurred in the try block
    f.close()
    
    # Print confirmation that the file has been closed
    print('file closed!')