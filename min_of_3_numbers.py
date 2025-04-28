# we take the input from the users
a = int(input('enter first number: '))
b = int(input('enter second number: '))
c = int(input('enter third number: '))
# suppose we have smallest no. is: a
smallest = a
# check with second no. if samllest ig greater than b then smallest will be b
if b < smallest:
    smallest = b
# check with third no. if samllest ig greater than c then smallest will be b
if c < smallest:
    smallest = c
# print the smallest number 
print(f'The smallest number is: {smallest}')
# using the min function
print(min(a,b,c))