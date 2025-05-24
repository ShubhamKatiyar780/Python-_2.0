# initialising nested lists
ini_list = [[1, 2], [4, 3], [45, 65], [223, 2]]

# printing initial lists
print("initial list", str(ini_list))

# code to split it into 2 lists
res1, res2 = map(list, zip(*ini_list))

# printing result
print("final lists", res1, "\n", res2)