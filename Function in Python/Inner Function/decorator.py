import time  # Importing time module to measure execution time

# 🔸 This is a decorator function
def timer_decorator(func):
    # This inner function wraps the actual function
    def wrapper(*args, **kwargs):
        start_time = time.time()  # Record start time
        print(f"Running function: {func.__name__}")  # Print the function name
        result = func(*args, **kwargs)  # Call the actual function with any arguments
        end_time = time.time()  # Record end time after function finishes
        # Print how long the function took to execute
        print(f"Execution Time: {end_time - start_time:.4f} seconds\n")
        return result  # Return the result of the actual function
    return wrapper  # Return the inner wrapper function

# 🔸 Apply the timer_decorator to this function
@timer_decorator
def slow_function():
    print("Processing...")
    time.sleep(2)  # Simulates a delay (like a slow task)
    print("Done!")

# 🔸 Apply the timer_decorator to this function with a parameter
@timer_decorator
def greet(name):
    time.sleep(1)  # Simulates a shorter delay
    print(f"Hello, {name}!")  # Print a greeting message

# 🔸 Calling the decorated functions
slow_function()       # Will print process messages and execution time
greet("Shubham")      # Will greet and also show execution time
