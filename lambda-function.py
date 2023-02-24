#lambda function ia a anonymous function.
#It can take no of arguments but can have only one expression.

import numpy as np
import pandas as pd

#1
#simple lambda function for add method
add=lambda x,y:x+y
print(add(10,20))

#2
#lambda function in a another function
def myfunc(n):
    return lambda a,b:(a+b)-n
sub=myfunc(1)
print(sub(2,2))

#3
#Write a Python program to create a lambda function that adds 15 to a given number passed in as an argument,
#also create a lambda function that multiplies argument x with argument y and prints the result.

#a
add15=lambda x:x+15
print(add15(10))

#b
mul=lambda x,y:x*y
print("muliplication:{}".format(mul(2,3)))

#4
#Write a Python program to sort a list of tuples using Lambda.
lst4=[('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
lst4.sort(key = lambda x: x[1])
print("Sorted tuple:{}".format(lst4))

#5
#Write a Python program to filter a list of integers using Lambda. Go to the editor
#Original list of integers:[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#Even numbers from the said list:[2, 4, 6, 8, 10]
#Odd numbers from the said list:[1, 3, 5, 7, 9]
lst5=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#evenlist
evenlst=list(filter((lambda x:x%2==0),lst5))
print("EvenList:{}".format(evenlst))

#oddlist
oddlst=list(filter((lambda x:x%2!=0),lst5))
print("oddList:{}".format(oddlst))

#squarelist
sqlst=list(map((lambda x:x ** 2 ),lst5))
print(sqlst)

#6
#Write a lambda function that takes x as parameter and returns x+2. Then assign it to a variable named L.
i=6
L=lambda x:x+2
print(L(i))


#7
#Using sorted() function and lambda sort the tuples in the list based on the last character of the second items.
lst7=[(19542209, "New York") ,(4887871, "Alabama"), (1420491, "Hawaii"), (626299, "Vermont"), (1805832, "West Virginia"), (39865590, "California")]
#Type your answer here.
lst7a=sorted(lst7,key=lambda x:x[1][-1])
print(lst7a)


#8
#Using sorted() function, reverse parameter and lambda sort the tuples in the list based on the last character of the second items in reverse order.
lst8=[(19542209, "New York") ,(4887871, "Alabama"), (1420491, "Hawaii"), (626299, "Vermont"), (1805832, "West Virginia"), (39865590, "California")]
#Type your answer here.
lst8a=sorted(lst8,key=lambda x:x[1][-1],reverse=True)
print(lst8a)

#Write a Python program to find the elements of a given list of strings that contain a specific substring using lambda. Go to the editor
lst9=['red', 'black', 'white', 'green', 'orange']
chk_str = "abc"
def check_string(str_lst,chk_str):
    return list(filter(lambda x:x if chk_str in x else "",str_lst))
ans=check_string(lst9,chk_str)
print(ans)




#Write a Python program to check whether a given string is a number or not using Lambda


