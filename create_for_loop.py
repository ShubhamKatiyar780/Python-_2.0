class Range:

    def __init__(self, *args):
        if len(args) <= 3:
            if len(args) == 1:
                self.start = 0
                self.end = args[0]
                self.step = 1
            elif len(args) == 2:
                self.start = args[0]
                self.end = args[1]
                self.step = 1
            elif len(args) == 3:
                self.start = args[0]
                self.end = args[1]
                self.step = args[2]
            else:
                raise TypeError(f"ABC expected at least 1 argument, {len(args)} got.")
        else:
            raise TypeError(f"ABC expected at most 3 arguments, {len(args)} got.")

    def __iter__(self):
        return RangeIterator(self)


class RangeIterator:

    def __init__(self, iterable_object):
        self.iterable = iterable_object

    def __iter__(self):
        return self

    def __next__(self):
        if self.iterable.start >= self.iterable.end:
            raise StopIteration('dsfghj')
        current_value = self.iterable.start
        self.iterable.start += self.iterable.step
        return current_value

# for i in Range(5, 16):
    # print(i, end= " ")


def my_range(*args):
        if len(args) <= 3:

            if len(args) == 1:
                start = 0
                end = args[0]
                step = 1

            elif len(args) == 2:
                start = args[0]
                end = args[1]
                step = 1

            elif len(args) == 3:
                start = args[0]
                end = args[1]
                step = args[2]

            else:
                raise TypeError(f"my_range expected at least 1 argument, {len(args)} got.")
            
            for i in range(start, end, step):
                 yield i

        else:
            raise TypeError(f"my_range expected at most 3 arguments, {len(args)} got.")

# for i in my_range(1,11,2,5):
#     print(i)


# create Generator expression
l = [i**2 for i in range(1,11)]     # list
t = (i**2 for i in range(1,11))     # generator

print(l)
print(t)

for i in l:
    print(i)
print("----- Generator -----")
for j in t:
    print(j)