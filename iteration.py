'''
Iteration--> Iteration is a general term for taking each item og somthing
one after another. Any time you use a loop, explicit, to go over a group
of items, that is iteration.
'''
# example
l = [1,2,3]
# for i in l:
#     print(i, end = " ")
# print()


'''
Iterator--> An Iterator is an object that allows the programmer to traverse
through a sequence of data without having to store the entire data in memory.
'''

# exmaple
import sys
L = [x for x in range(101)]
# for i in L:
#     print(i*2, end=" ")
# print()
# print(f"Size: {sys.getsizeof(L)/1024} KB")

x = range(1, 1001)
# for i in x:
#     print(i*2, end = " ")
# print()
# print(f"Size: {sys.getsizeof(x)/1024} KB")


'''
Iterable---> Iterable is an object, which one can iterate over.
It generates an iterator when passed to iter() method.
'''

# example
listt = [1,2,3]
# print(type(listt))
# listt is an iterable
# print(iter(listt))
# print(type(iter(listt)))
# iter(listt)--> iterator
# print(dir(listt))   # if __iter__ is present then it is iterable.
# every iterator has both __iter__ as well as a __next__


# create our custom loop
def my_loop(iterable):
    iterator = iter(iterable)
    while True:
        try:
            print(next(iterator))
        except StopIteration:
            break
a = [1,2,3,4,5]
b = range(6, 11)
# my_loop(a)
# my_loop(b)



class MyRange:

    def __init__(self, *args):
        # Handle 1-3 arguments like built-in range()
        if len(args) <= 3:
            if len(args) == 1:
                # range(stop)
                self.start = 0
                self.end = args[0]
                self.step = 1
            elif len(args) == 2:
                # range(start, stop)
                self.start = args[0]
                self.end = args[1]
                self.step = 1
            elif len(args) == 3:
                # range(start, stop, step)
                self.start = args[0]
                self.end = args[1]
                self.step = args[2]
            else:
                # No arguments
                raise TypeError(f"MyRange expected at least 1 argument, {len(args)} got.")
        else:
            # Too many arguments
            raise TypeError(f"MyRange expected at most 3 arguments, {len(args)} got.")

    def __iter__(self):
        # Return iterator object
        return MyRangeIterator(self)


class MyRangeIterator:

    def __init__(self, iterable_object):
        # Store reference to the MyRange object
        self.iterable = iterable_object

    def __iter__(self):
        # Iterator must return itself
        return self
    
    def __next__(self):
        # Check if we've reached the end
        if self.iterable.start >= self.iterable.end:
            raise StopIteration
        
        # Get current value and increment start for next call
        current = self.iterable.start
        self.iterable.start += self.iterable.step
        return current

for i in MyRange(1, 11, 2):
    print(i)

xyz = MyRange(1, 6)
print(type(xyz))
print(iter(xyz))
