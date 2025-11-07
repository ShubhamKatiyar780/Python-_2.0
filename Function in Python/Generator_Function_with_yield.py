# Problem: Write a generator function that yields even numbers up to a specified limit.

def even_generator1(limit):
    my_list = []
    for i in range(2, limit + 1, 2):
        my_list.append(i)
    return my_list
    
# print(even_generator1(10))



# Yaha yield use kiya gaya hai, isiliye function ek generator ban gaya.
# Matlab ye ek-ek karke value dega, list memory me nahi banayega.
def even_generator2(limit):
    for i in range(2, limit + 1, 2):
        yield i
    
obj = (even_generator2(10))
# print(next(obj))
# print(next(obj))
# print(next(obj))
# print(next(obj))
# print(next(obj))

for num in obj:
    print(num)