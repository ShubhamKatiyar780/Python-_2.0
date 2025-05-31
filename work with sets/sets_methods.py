# A normal set
s = set(["a", "b","c"])
print("Normal Set")
print(s)


# A frozen set
fs = frozenset(["e", "f", "g"])
print("\nFrozen Set")
print(fs)


# -------------------Adding elements-------------------
people = {"Jay", "Idrish", "Archi"}
print(people)
# This will add Shubham
people.add("Shubham")
# set using iterator
for i in range(1, 6):
    people.add(i)
print("\nSet after adding element:", end = " ")
print(people)
# Add multiple items using update() method
set1 = {1, 2, 3}
set1.update([5, 6])
print(set1)


# -------------------Removing elements-------------------
# remove()
def Remove(sets):
    sets.remove("aakash")
    print (sets)
sets = set(["ram", "aakash", "kaushik", "anand", "prashant"])
Remove(sets)

# Discard()
def Discard(sets):
    sets.discard(21)
    print (sets)
sets = set([10, 20, 26, 41, 54, 20])
Discard(sets)

# pop()
s1 = {1, 2, 3, 4}
print("Before popping: ",s1)
s1.pop()
s1.pop()
s1.pop()
print("After 3 elements popped, s1:", s1)

# clear()
set1 = {1,2,3,4,5,6}
print("Initial set")
print(set1)
# This method will remove all the elements of the set
set1.clear()
print("\nSet after using clear() function")
print(set1)


# -------------------Union operation-------------------
people = {"Jay", "Idrish", "Archil"}
vampires = {"Karan", "Arjun"}
dracula = {"Deepanshu", "Raju"}
# Union using union()
# function
population = people.union(vampires)
print("Union using union() function")
print(population)
# Union using "|" operator
population = people|dracula
print("\nUnion using '|' operator")
print(population)



# -------------------Intersection operation-------------------
set1 = set()
set2 = set()
for i in range(5):
    set1.add(i)
for i in range(3,9):
    set2.add(i)
# Intersection using intersection() function
set3 = set1.intersection(set2)
print("Intersection using intersection() function")
print(set3)
# Intersection using "&" operator
set3 = set1 & set2
print("\nIntersection using '&' operator")
print(set3)

# Using intersection() + * operator
# initializing list
test_list = [{5, 3, 6, 7}, {1, 3, 5, 2}, {7, 3, 8, 5}, {8, 4, 5, 3}]
# printing original list
print("The original list is : " + str(test_list))
# getting all sets intersection using intersection()
res = set.intersection(*test_list)
# printing result
print("Intersected Sets : " + str(res))


# -------------------difference_update()-------------------
A = {10, 20, 30, 40, 80}
B = {100, 30, 80, 40, 60}
# Modifies A and returns None
A.difference_update(B)
# Prints the modified set
print (A)



# -------------------difference()-------------------
A = {1, 2, 3, 4, 5}
B = {3, 4, 5, 6, 7}
C = {5, 6, 7, 8, 9}
res = A.difference(B, C)  # Elements in A that are not in B or C
print(res)

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
# Using '-' operator
res1 = A - B
print("using '-':", res1)
# Using difference() method
res2 = A.difference(B)
print("using difference():", res2)


# -------------------symmetric_difference()-------------------
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
# Using '^' operator
res1 = A ^ B
print("using '^':", res1)
# Using symmetric_difference() method
res2 = A.symmetric_difference(B)
print("using symmetric_difference():", res2)


# -------------------issuperset()-------------------
A = {4, 1, 3, 5}
B = {6, 0, 4, 1, 5, 0, 3, 5}
print("A.issuperset(B) : ", A.issuperset(B))
print("B.issuperset(A) : ", B.issuperset(A))


# -------------------issubset()-------------------
s1 = {1, 2, 3, 4, 5}
s2 = {4, 5}
print(s2.issubset(s1))


# -------------------isdisjoint()-------------------
set1 = {2, 4, 5, 6}
set2 = {7, 8, 9, 10}
set3 = {1, 2}
# checking of disjoint of two sets
print("set1 and set2 are disjoint?",
      set1.isdisjoint(set2))
print("set1 and set3 are disjoint?",
      set1.isdisjoint(set3))


# -------------------intersection_update()-------------------
# if there are no common elements between the sets, so the output should be empty.
s1 = {1, 2, 3}
s2 = {4, 2, 5}
s1.intersection_update(s2)
# print updated s1 set
print("After intersection_update, s1:", s1)


# -------------------issuperset()-------------------


