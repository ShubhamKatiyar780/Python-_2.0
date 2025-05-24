# create a string with single quotes or double quotes or tri ple quotes
a = 'it is a string'
b = "it is also a string"
c = """I am Learning
Python it is multiline string"""

# Accessing characters with positive index
print('Accessing characters with positive index')
print(a[0]) # putput: i
print(b[7]) # putput: l
print(c[14]) # putput: P

# Accessing characters with negative index which is start from the last
print('Accessing characters with negative index')
print(a[-1]) # putput: g
print(b[-8]) # putput: a
print(c[-13]) # putput: t

'''Note: Accessing an index out of range will cause an IndexError. 
Only integers are allowed as indices and using a float or other types will result in a TypeError'''

# slicing
print('slicing method')
# Retrieves characters from index 1 to 3: 'is'
print(b[3:5])  
# Retrieves characters from beginning to index 2: 'I am Learn'
print(c[:10])   
# Retrieves characters from index 3 to the end: 'i  tig'
print(a[3::2])   
# Reverse a string
print(a[::-1])

# Immutability
s = "Ghubham"
# Trying to change the first character raises an error
# s[0] = 'G'  # Uncommenting this line will cause a TypeError
# Instead, create a new string
s = "S" + s[1:]
print(s)

# max(), min()
print('Using max(), min()')
w = 'shubham'
print(max(w))   # 'u'  because ASCII value of u is more than other characters which is present in our string
print(min(w))   # 'a'  because ASCII value of a is minimum than other characters which is present in our string

# Using soretd()
print('Using soretd()')
# always return in the form of list
print(sorted(w, reverse= True))
print(sorted(w))

# Deleting
del s
'''After deleting the string using del and if we try to access s then 
it will result in a NameError because the variable no longer exists.'''
# print(s)

# updating
s = "hello shubham"
# replacnig "shubham" with "katiyar"
print(s.replace("shubham", "katiyar")) # always return a new string
print(s) # original string can not be changed

# strip()
s = '   shubham with leading and trailing whitespace  '
# removes leading and trailing whitespace from the string
print(s.strip())

# Concatenating and Repeating
e = 'concatenate'
f = 'repeat'
print(e + f) # concatenate with both string
print(f * 3) # 'f' string repeat with 3 times

# Using f-strings
name = "Shubham"
age = 24
print('Using f-strings')
print(f"Name: {name}, Age: {age}")

# Using format()
print('Using format()')
s = "My name is {} and I am {} years old.".format("Shubham", 24)
print(s)

# using capitalize() method
print('using capitalize() method')
s = "my NAME is Shubham and I am 24 Years old."
# capitalizes the first letter of each word
print(s.capitalize())

# using title() method
print('using title() method')
s = "my name is Shubham and I am 24 Years old."
# capitalizes the first letter of each word
print(s.title())

# using swapcase() method
print('using swapcase() method')
s = "mY nAme Is ShubhaM AnD I am 24 YeaRs oLD."
# swap upper to lower case and vice versa
print(s.swapcase())

# using find() method
print('using find() method')
s = "my name is Shubham and I am 24 Years old."
# find the first occurrence index of substring and returns -1 if not found
print(s.find('m'))

# using zfill()
print('using zfill() method')
# Pads the string on the left with zeros to make it width characters long
print(s.zfill(50))

# using center()
print('using center() method')
a = 'shubh'
# Centers the string in a field of given width, padded with spaces
print(a.center(20))

# Using ljust(), rjust()
print('Using ljust(), rjust()')
# Left/right -justifies the string in a field of given width
s = 'Shubham'
print(s.ljust(10)) # output: Shubham___
print(s.rjust(10)) # output: ___Shubham

# find the length of a string with the help of count() method
print('find the length of a string with the help of count() method')
a = "Hello"
#It counts the number of occurrences of the specified substring 
length = a.count("") - 1
print(length)

# Using enumerate function
print('Using enumerate function')
# used to loop over an iterable and keep track of both the index and the value of elements
x = 'Shubham'
length_str = 0
for i, j in enumerate(x): # i for index and j for element
    length_str += 1
    print(f'index {i}: {j}')
print(f'length of the string "{x}" is: {length_str}')


# string comparison
# lexicographical comparison
s1 = 'apple'
s2 = 'banana'
# "banana" comes after "apple", therefore it is False
print(s1 > s2)
# "apple" appears before "banana" alphabetically, therefore it is True
print(s2 > s1)


# using zip()
# it's used to combines two or more iterable element wise in to tuples.
print('using zip()')
names = ['shubham', 'rajat', 'banti']
ages = [25, 30, 35]
zipped = zip(names, ages)
print(list(zipped))


# using splitlines()
# it is a method splits each string in to a list of lines. 
print('using splitlines()')
text = "shubham\nrajat\nbanti"
print(text.splitlines())