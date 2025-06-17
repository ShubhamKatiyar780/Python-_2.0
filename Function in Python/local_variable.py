# Function to demonstrate local variable scope
def local_var():
    x = 10  # 'x' is a local variable to this function
    print("Local x:", x)  # prints the value of local variable x

local_var()

# print(x)  # This will cause an error because 'x' is not defined outside the function scope


# Function to demonstrate use of 'nonlocal' keyword in nested functions
def outer():
    x = 10  # 'x' is a variable in the scope of the outer function

    # Nested function (inner function)
    def inner():
        nonlocal x  # Refers to the 'x' in the outer function, not a new local variable
        x = x + 5   # Modifies the 'x' defined in the outer function
        print("Inner x:", x)  # prints the modified value of x

    inner()  # Call the inner function
    print("Outer x after inner:", x)  # prints the updated value of x after modification by inner()

outer()
