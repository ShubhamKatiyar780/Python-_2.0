# function for subtraction of 2 numbers.
def subNumbers(x, y):
    return (x-y)
# main code
a = 90
b = 50
# finding subtraction
res = subNumbers(a, b)
# print statement
print("subtraction of ", a, " and ", b, " is: ", res)


class Person:
    # Constructor to initialize the person's name and age
    def __init__(self, name, age):
        self.name = name  # Set the name attribute
        self.age = age    # Set the age attribute
    # Method to print a greeting message
    def greet(self):
        print(f"Name - {self.name} and Age - {self.age}.")
# Create an instance of the Person class
p1 = Person("Shubham Katiyar", 24)
# Call the greet method to display the greeting message
p1.greet()