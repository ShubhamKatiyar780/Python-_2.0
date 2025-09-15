# Simple closure example
def outer():
    msg = 'Hey'  # Define a variable in the outer function
    def inner():
        return msg  # Inner function accesses outer variable (closure)
    return inner()  # Call inner() and return its result

# Prints the result of calling outer(), which internally calls inner()
print(outer())  # Output: Hey


# Using nonlocal to modify outer variable
def outer():
    msg = 'Hello Shubham'  # Outer function variable

    def inner():
        nonlocal msg        # Declare that we want to use and modify 'msg' from outer()
        msg = 'hi Katiyar'  # Modify the outer variable
        return msg          # Return the modified value

    print(msg)              # Print the original message before inner() is called
    print(inner())          # Call inner() and print the returned (modified) value
    print(msg)              # Print the value of msg after modification

# Call the outer() function to execute everything
outer()

# Expected Output:
# Hello Shubham     <- Before modification
# hi Katiyar        <- inner() modifies and returns new value
# hi Katiyar        <- After modification, 'msg' is updated
