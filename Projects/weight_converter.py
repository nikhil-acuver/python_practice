print("Hello sir/madam, Please enter your weight: ")
weight = int(input())
print("In which unit constant you have entered your weight? ")
unit = input("(L)bs or (K)g : ")
if unit.upper() == "K":
    ans = weight / 0.45
    print(f"You are {ans} pounds ")
elif unit.upper() == "L":
    ans = weight * 0.45
    print(f"You are {ans} kg ")
else:
    print('Enter appropriate constant.')
