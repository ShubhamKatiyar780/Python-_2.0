def add(a, b):
    # returning sum of a and b
    return a + b
def is_true(a):
    # returning boolean of a
    return bool(a)
# calling function
res = add(2, 3)
print(res)
res = is_true(2<5)
print(res)


# Returning Multiple Values
def fun():
    name = "Shubham"
    age = 24
    return name, age
name, age = fun()
print(name)  # Output: Shubham
print(age)   # Output: 24


# Returning List
def fun(n):
    return [n**2, n**3, n**4]
res = fun(3)
print(res)


# Function returning another function
def fun1(msg):
    def fun2():
        # Using the outer function's message
        return f"Message: {msg}"
    return fun2
# Getting the inner function
fun3 = fun1("Hello, Shubham")
# Calling the inner function
print(fun3())