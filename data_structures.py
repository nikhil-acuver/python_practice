# list
name = ['vaibhav', 'palash','jay', 'yash', 'ritesh','nikhil']
print(name)
print(name[3])
print(name[1:5])
name.append('robin')
print(name)
name[0]="vebs"
print(name)
name.insert(7,"rajat")
print(name)
name.remove("rajat")
print(name)
name.sort()
print(name)
name.pop(1)
print(name)

lst = [2, 4, 6, 7, 8, 2, 4, 10, 9]
lst
lst2=[]
for i in lst:
    if i not in lst2:
        lst2.append(i)
print(lst2)


numbers=[1, 4, 5, 35, 34, 6, 78, 788, 7675, 7577, 5563, 5789]
max = 0
for i in numbers:
    if max < i:
        max = i
print(max)

# 2 dimensional list
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
print(matrix)

print(matrix[2][0])
print(matrix[1:][1:])
