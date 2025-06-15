# Define a function that accepts any number of keyword arguments
def fun(**kwargs):
    # Iterate over the dictionary of keyword arguments
    for k, val in kwargs.items():
        # Print each key-value pair
        print(f"{k}: {val}")

# Calling the function with keyword arguments
# These arguments are passed as a dictionary: {"name": "Alice", "age": 30, "city": "New York"}
fun(name="Shubham Katiayr", age=24, city="Kanpur")
