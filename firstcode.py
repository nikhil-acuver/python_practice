patient_name = "Smith"
age = 20
is_new = True
print(patient_name, age, is_new)

# taking input
name = input("What is your name?")
fav_color = input('What is your fav Color?')

print(name+' likes '+fav_color)


# type-conversion or typecasting
birth_year = input('Birth year:')
print(type(birth_year))
age = 2023-int(birth_year)
print(age)

user_weight = int(input('tell us your weight in pounds:'))
weight_kg = 0.45*user_weight
print('your weight in kg:{}'.format(weight_kg))

course = 'Python for "Beginners"'
print(course)

memo = '''
hello there,
this is our day for python
enjoy coding!
'''
print(memo)
