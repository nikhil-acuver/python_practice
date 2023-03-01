flag = True
while True:
    sample = input('>')
    if sample.lower() == 'help':
        print('''start - to start the car \nstop - to stop the car \nquit - to exit''')
    elif sample.lower() == 'start':
        if flag:
            print("Car started...Ready to go")
            flag = False
        else:
            print("Car is already running!")
    elif sample.lower() == 'stop':
        if not flag:
            print("Car stopped!")
            flag = True
        else:
            print("Car stopped already")
    elif sample.lower() == 'quit':
        break
    else:
        print("I don't understand that...")
