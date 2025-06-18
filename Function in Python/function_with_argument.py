# Passing Function as an Argument
# A function that takes another function as an argument
def fun(func, arg):
    return func(arg)
def square(x):
    return x ** 2
# Calling fun and passing square function as an argument  
res = fun(square, 5)
print(res)

