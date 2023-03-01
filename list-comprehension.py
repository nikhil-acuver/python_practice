# List comprehension offers shorter syntax whe you want list based values of an existing list

# 1
# printing a same  list using list comprehension
fruits = ["apple", "banana", "mango", "kiwi", "grapes"]
new_lst = [x for x in fruits]
print(new_lst)

# check for banana in a list
# 2
lst2 = [x for x in fruits if "banana" in x]
print(lst2)

# 3
lst3 = [x for x in fruits if "banana" != x]
print(lst3)


# using iterable with condition
# 4
number = [x for x in range(20) if x > 10]
print(number)

# change in expression
# 5
name = ["moody"]
str = [x.upper() for x in name]
print(str)

# 6
name1 = ["moody", "foodie", "hoodie", "rudy", "rodie"]
str2 = ["vanish" for x in name1]
print(str2)

# expression with condition
# 7
lst4 = [x if "mango" != x else "ripe mango" for x in fruits]
print(lst4)

# 8
# Using list comprehension, construct a list from the squares of each element in the list,
# if the square is greater than 50.
lt = [2, 4, 6, 8, 10, 12, 14]
lst8 = [x**2 for x in lt if x**2 > 50]
print(lst8)

'''
8
Given dictionary is consisted of vehicles and their weights in kilograms. Construct a list of the names of vehicles with 
weight below 5000 kilograms. 
In the same list comprehension make the key names all upper case.
'''
dict = {"Sedan": 1500, "SUV": 2000, "Pickup": 2500, "Minivan": 1600, "Van": 2400, "Semi": 13600, "Bicycle": 7, "Motorcycle": 110}
lst9 = [x.upper() for x in dict if dict[x] < 5000]
print(lst9)
