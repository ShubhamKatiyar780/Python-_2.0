x = 50  # This is a global variable (yeh global variable hai)

def global_var():
    global x  # This tells Python to use the global variable 'x', not create a new local one (global x ka use karein)
    x = x + 10  # Global variable ko modify kar rahe hain
    print("Global x inside function:", x)  # Function ke andar updated global x print ho raha hai

global_var()  # Function call, jisme global x ko modify kiya gaya hai
print("Global x outside function:", x)  # Function ke baad bhi global x updated hai, isliye yahan bhi updated value print hogi
