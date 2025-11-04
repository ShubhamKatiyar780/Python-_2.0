import json

class Person:
    def __init__(self, fname, lname, age, gender):
        self.fname = fname
        self.lname = lname
        self.age = age
        self.gender = gender

    # make dictionary
    def to_dict(self):
        return {
            'fname': self.fname,
            'lname': self.lname,
            'age': self.age,
            'gender': self.gender
        }

p1 = Person('Shubham', 'Katiyar', 24, 'Male')

file_path = 'C:/Users/katiy/OneDrive/Desktop/Python-_2.0/File Handling/oject.json'
with open(file_path, 'w') as f:
    json.dump(p1.to_dict(), f)


def show_object(person):
    if isinstance(person, Person):
        # string format
        return f"Name: {person.fname} {person.lname}, Age: {person.age}, Gender: {person.gender}"

        # dictionary format
        # return {
        #     'fname': person.fname,
        #     'lname': person.lname,
        #     'age': person.age,
        #     'gender': person.gender
        # }
    
with open('C:/Users/katiy/OneDrive/Desktop/Python-_2.0/File Handling/oject_copy.json', 'w') as f:
    json.dump(p1, f, default=show_object)