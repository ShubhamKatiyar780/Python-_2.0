def fun1(msg):  # Outer function that takes a message as argument
    def fun2():  # Inner function
        print(msg)  # Inner function accesses 'msg' from the outer function (closure)
    fun2()  # Call the inner function

print(fun1("hello"))