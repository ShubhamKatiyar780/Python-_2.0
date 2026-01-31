class Person:
    __counter = 1

    def __init__(self,name,gender):
        self.name = name
        self.gender = gender
        self.costumer_id = Person.__counter
        Person.__counter = Person.__counter + 1

    @staticmethod
    def get_counter():
        return Person.__counter
        

p1 = Person('A','M')
print(p1.costumer_id)
p2 = Person('B','F')
print(p2.costumer_id)
p3 = Person('C','T')
print(p3.costumer_id)
print(Person.get_counter())

Person.__counter = "abc"
print(Person.counter)
