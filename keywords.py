import keyword
# printing all keywords at once using "kwlist()"
print("The list of keywords is : ")
print(keyword.kwlist)

# None
a=None
print(id(None))
print(id(a))


# Return and Yield Keyword use in Python
# return
'''Purpose: It exits a function and sends a value back to where the function was called.
Once return runs, the function ends immediately — no code after it will be executed.
It’s used when you want the result of a function.'''
def add(a, b):
    return a + b
result = add(5, 3)
print(result)  # Output: 8

# yield
'''Purpose: It pauses a function and saves its state for later resumption.
Functions that use yield are called generators.
It’s used when you want to produce a series of values one at a time, without storing them all in memory.'''
def generate_numbers():
    for i in range(3):
        yield i
gen = generate_numbers()
print(next(gen))  # Output: 0
print(next(gen))  # Output: 1
print(next(gen))  # Output: 2


# Lambda keyword
# Lambda keyword is used to make inline returning functions with no statements allowed internally. 
g = lambda x: x*x*x
print(g(7))


# async, await
'''async: Used to declare a function as asynchronous, allowing it to run concurrently with other tasks.'''
'''await: Used to pause the execution of an async function until the awaited task is complete.'''
import asyncio
async def task(name, delay):
    print(f"Task {name} started")
    await asyncio.sleep(delay)
    print(f"Task {name} finished after {delay} seconds")
async def main():
    await asyncio.gather(
        task("A", 2),
        task("B", 1),
        task("C", 3)
    )
asyncio.run(main())