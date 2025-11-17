def check_datatype(datatype):
    def outer_wrapper(function):
        def inner_wrapper(*args, **kwargs):
            # if type(args[0]) == datatype:
            if type(*args) == datatype:
                function(*args)
            else:
                raise TypeError ("daya type not valid.")
        return inner_wrapper
    return outer_wrapper

@check_datatype(int)
def square(number):
    print(number ** 2)

@check_datatype(str)
def greet(name):
    print(f"Hello {name}!")


square(12)

greet("Shubham")