# dynamic typing
a = 5 

'''
static typing
int b = 10
'''
# dynamic binding
# in python a variable can store multiple datatype value
s = 505
print(s)
s = 'Shubham'
print(s)

# stylish declaration techniques
e, f, g = 10, 20, 30
print(e,f,g)
h = i = j = 15
print(h,i,j)

# Global Variable
a = "I am global"
def f():
    global a
    a = "Modified globally"
    print(a)
f()
print(a)  # Variables defined outside any function are global and can be accessed inside functions using the global keyword.


# Local Variable
def f():
    a = "I am local"
    print(a)
f()
# print(a)  # This would raise an error since 'local_var' is not accessible outside the function
