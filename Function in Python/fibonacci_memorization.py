import time

def fibonacci1(number):
    if number <= 0:
        return 0
    elif number == 1:
        return 1
    else:
        return fibonacci1(number - 1) + fibonacci1(number - 2)

start_time = time.time()
print(fibonacci1(12))
end_time = time.time()
print(f"total execution time: {end_time - start_time:.8f}")



def fibonacci2(key, dictionary):
    if key in dictionary:
        return dictionary[key]
    else:
        dictionary[key] = fibonacci2(key-1, dictionary) + fibonacci2(key-2, dictionary)
        return dictionary[key]
    
dictionary = {0:0, 1:1}
start_time = time.time()
print(fibonacci2(80, dictionary))
end_time = time.time()
print(f"total execution time: {end_time - start_time:.8f}")
print(dictionary)