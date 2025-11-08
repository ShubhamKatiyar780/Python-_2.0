# Define a function that accepts any number of positional arguments
def fun(*args):
    # Iterate over the tuple of arguments
    total = 0
    for arg in args:
        # Print each argument
        print(arg)
        total += arg
    print('total sum:', total)

# Calling the function with multiple positional arguments
# These arguments are passed as a tuple: (1, 2, 3, 4, 5)
fun(1, 2, 3, 4, 5)
