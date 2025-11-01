try:
    # Define a variable x with value 2500
    x = 2500
    
    # Define the file path as a string
    file = 'C:/Users/katiy/OneDrive/Desktop/Python-_2.0/Execption Handling/my_file.txt'
    
    # Attempt to open the file in read mode using a context manager
    # The 'with' statement ensures proper file closure even if exceptions occur
    with open(file, 'r') as f:
        # Read and print the entire contents of the file
        print(f.read())
        
        # Print the value of variable x (2500)
        print(x)
        
        # Attempt to divide 5 by 0 - this will raise a ZeroDivisionError
        print(5/0)
        
        # Define a list with three elements [1, 2, 3]
        l = [1,2,3]
        
        # Attempt to print the element at index 10 - this will raise an IndexError
        # since the list only has 3 elements (indices 0, 1, 2)
        print(l[10])

# Handle the specific exception when the file cannot be found
except FileNotFoundError:
    print("No such file or directory")

# Handle the specific exception when a variable is not defined
except NameError:
    print('variable not defined')

# Handle the specific exception when attempting to divide by zero
except ZeroDivisionError:
    print("can't divide by zero")

# Catch any other exceptions that aren't handled by the specific blocks above
except Exception as e:
    # Print the exception message using f-string formatting
    print(f"An exception occurred {e}")
    
    # Attempt to print the traceback information (note: this line has an issue)
    # with_traceback is a method, not an attribute, so this will cause an AttributeError
    print(e.with_traceback)