is_hot = True
if is_hot:
    print("It's a hot day. \nDrink plenty of water!")
else:
    print("It's a cold day. \nWear warm cloths!")

is_hot = False
if is_hot:
    print("It's a hot day. \nDrink plenty of water!")
else:
    print("It's a cold day. \nWear warm cloths!")

is_hot = False
is_cold = False
if is_hot:
    print("It's a hot day. \nDrink plenty of water!")
elif is_hot:
    print("It's a cold day. \nWear warm cloths!")
else:
    print("It's a lovely day")
print("Enjoy your day")


price = 1000000
has_good_credit = True
if has_good_credit:
    down_payment = 0.1 * price
    print("Price will be dropped by 10%")
else:
    down_payment = 0.2 * price
    print("price will be dropped by 20%")
print(f"Down Payment: {down_payment}")


has_high_income = True
has_good_credit = False

if has_high_income and  not has_good_credit:
    print("Eligible for loan")
else:
    print('Not eligible for loan')


if has_good_credit or has_high_income:
    print("eligible")

temperature = 34
if temperature > 30:
    print("It's a hot day")
elif temperature < 30:
    print("It's a cold day")
else:
    print("It's neither hot or cold")

name = input("Enter your name")

if len(name) < 3:
    print("name must be at least 3 character")
elif len(name) > 10:
    print("name can be maximum 10 character")
else:
    print("name looks good")

