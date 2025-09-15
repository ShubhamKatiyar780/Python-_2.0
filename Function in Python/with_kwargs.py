# Define a function that accepts any number of keyword arguments
def fun(**kwargs):
    # Iterate over the dictionary of keyword arguments
    for key, val in kwargs.items():
        # Print each key-value pair
        print(f"{key}: {val}")

# Calling the function with keyword arguments
# These arguments are passed as a dictionary: {"name"="Shubham Katiayr", 'age'=24, 'city'="Kanpur"}
fun(name="Shubham Katiayr", age=24, city="Kanpur")
