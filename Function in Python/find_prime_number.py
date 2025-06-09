# Python program to print first 10 prime numbers
# using def keyword for creating a function
def fun(n):
    x = 2
    count = 0
    while count < n:
        for d in range(2, int(x ** 0.5) + 1):  # check divisibility only up to sqrt(x)
            if x % d == 0:
                break  # if divisible, it's not prime, so break the loop
        else:
            print(x)  # prime number
            count += 1
        x += 1
# Driver Code
n = 10
fun(n)