print("This is a number guessing game. Guess any number between 1 to 10.")
print("Note:You will get 3 chances to guess.")
secret_number = 6
i = 0
while i < 3:
    number = int(input('Guess the secret number: '))
    if number == secret_number:
        print('You won!')
        break
    else:
        print("Wrong number")
        if i == 2:
            print('You lost all chances')
    i = i + 1

