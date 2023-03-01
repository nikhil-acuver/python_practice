new_string = 'Python for "Beginners"'
# indexing on string
print(new_string[0])
print(new_string[-1])
print(new_string[5])
print(new_string[10])

# slicing on a string
print(new_string[0:4])
print(new_string[:8])
print(new_string[:])

name = 'jennifer'
print(name[1:-1])

# formatting
first = 'Navin'
last = 'reddy'
msg = f'{first} [{last}] is a coder'
print(msg)

# upper and lower
print(new_string.upper())
print(new_string.lower())

# find method
print(new_string.find(' '))
print(new_string.find('B'))

# replace method
print(new_string.replace('beginners', 'practice'))


print('Python' in new_string)
