import string

while True:
    start = input('Do you want to start?\n[Y/N]\n>')
    if start.lower() == 'y':
        while True:
            print("true")
            break

    elif start.lower() == 'n':
        print("ja")
        break

    else:
        print('Please choose one of the options!\n-------')
        continue

