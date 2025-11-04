'''
Pickling:- pickling is the process whereby a python object
hierarchy is converted into a byte stream, and unpickling
is the inverse operation, whereby a byte stream (from a binary
                                        file or bytes-like object)
is converted back into an object hierarchy.
'''


import pickle

class Person:
    def __init__(self, fname, lname, age, gender):
        self.fname = fname
        self.lname = lname
        self.age = age
        self.gender = gender

    def display_data(self):
        return f"my name is {self.fname} {self.lname} and i am {self.age} years old."


p1 = Person('Shubham', 'Katiyar', 24, 'Male')

# pickle dump
with open('C:/Users/katiy/OneDrive/Desktop/Python-_2.0/File Handling/pickl.pkl', 'wb') as f:
    pickle.dump(p1, f)

# pickle load
with open('C:/Users/katiy/OneDrive/Desktop/Python-_2.0/File Handling/pickl.pkl', 'rb') as f:
    data = pickle.load(f)


print(data.display_data())


# PICKLE vs JSON
# ==================
# PICKLE lets the user to store data in binary format.
# JSON lets the user store data in a human readable text format.