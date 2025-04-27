# Arithmetric Operators-------------------
print(5+6)
print(5-6)
print(5*6)

arr = ['s', 'h', 'u', 'b', 'h']
# without using asterisk(*)
print(' '.join(map(str,arr)))
# using asterisk(*)
print(*arr)

# using asterisk(*)
def addition(*args):
  return sum(args)
print(addition(5, 10, 20, 6))

# using asterisk(*)
def food(**kwargs):
  for items in kwargs:
    print(f"{kwargs[items]} is a {items}")
food(fruit = 'cherry', vegetable = 'potato', boy = 'srikrishna')

print(5/2)
print(5//2)
print(5%2)
print(5**2)
# example of (**) double star
def intro(name, age, city):
    print(f"My name is {name}, I'm {age} years old and I live in {city}.")
p = {
    "name": "Prajjwa'",
    "age": 23,
    "city": "Prayagraj"
}
intro(**p)
# example of (**) double star
def fun(**kwargs):
    for key, val in kwargs.items():
        print("{} : {}".format(key, val))
fun(n_1="Prajjwal", n_2="Kareena", n_3="Brijkant")

# Relational/Comparision Operators---------------
print(4>5)
print(4<5)
print(4>=4)
print(4<=4)
print(4==4)
print(4!=4)
# chaining comparison operators
a = 5
print(1 < a < 10)
print(10 > a <= 9)
print(5 != a > 4)
print(a < 10 < a*10 == 50)

# Logical Operators----------------------
print(1 and 0)
a = 10
b = 10
c = -10
if a > 0 and b > 0:
    print("The numbers are greater than 0")
if a > 0 and b > 0 and c > 0:
    print("The numbers are greater than 0")
else:
    print("Atleast one number is not greater than 0")

print(1 or 0)
a = 10
b = -10
c = 0
if a > 0 or b > 0:
    print("Either of the number is greater than 0")
else:
    print("No number is greater than 0")
if b > 0 or c > 0:
    print("Either of the number is greater than 0")
else:
    print("No number is greater than 0")

print(not 1)
a = 10
if not a:
    print("Boolean value of a is True")
if not (a % 3 == 0 or a % 5 == 0):
    print("10 is not divisible by either 3 or 5")
else:
    print("10 is divisible by either 3 or 5")

# Bitwise Operators---------------------------
# bitwise and
print(2 & 3)
# bitwise or
print(2 | 3)
# bitwise xor
print(2 ^ 3)
# bitwise not
print(~3)
# Bitwise Right Shift
'''Shifts the bits of the number to the right and fills 0 on voids left
( fills 1 in the case of a negative number) as a result.
Similar effect as of dividing the number with some power of two.'''
print(4 >> 2)
# Bitwise Left Shift
''''Shifts the bits of the number to the left and fills 0 on voids right as a result.
Similar effect as of multiplying the number with some power of two.'''
print(5 << 2)

# Assignment Operators-----------------------------
a = 2
# a = a % 2
a %= 2
# a++ ++a    it is not use in python
print(a)

# Membership Operators
# in/not in    here it is 2 type only
print(1 in [2,3,4,5,6])
print('D' not in 'Delhi')


# operator.contains() Method
# import module
import operator
print("operator.contains() Method")
# using operator.contain()
# checking an integer in a list
print(operator.contains([1, 2, 3, 4, 5], 2))
# checking a character in a string
print(operator.contains("Hello World", 'O'))
# checking an integer in aset
print(operator.contains({1, 2, 3, 4, 5}, 6))
# checking for a key in a dictionary
print(operator.contains({1: "Geeks", 2:"for", 3:"geeks"}, 3))


#  Identity Operators
# is/is not in    here it is 2 type only
# Python program to illustrate the use
# of 'is' identity operator
print("Identity Operators")
num1 = 5
num2 = 5
a = [1, 2, 3]
b = [1, 2, 3]
c = a
s1 = "hello world"
s2 = "hello world"
# using 'is' identity operator on different datatypes
print(num1 is num2) # output True  (-5 se 256 tak) ke liye ek internal memory optimization hoti hai
print(a is b)   # output False (check the memory location not comparison)
print(a is c)   # output True
print(s1 is s2) # output True
print(s1 is s2) # output True


# Ternary Operator
n = 5
print("Even" if n % 2 == 0 else "Odd")
# Ternary Operator in Nested If else
m = -8
res = "Positive" if m > 0 else "Negative" if m < 0 else "Zero"
print(res)
# Ternary Operator using Tuple 
k = 7
resul = ("Odd", "Even")[k % 2 == 0]
print(resul)
# Ternary Operator using Dictionary
a = 10
b = 20
max = {True: a, False: b}[a > b]
print(max)