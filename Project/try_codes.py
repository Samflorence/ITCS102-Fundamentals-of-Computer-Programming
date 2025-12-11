import os

while True:
    print('Remider always save before closing notepad (ctrl + s)')
    try_code = input('A - try code\nB - output\nX - Exit\nChoose: ').lower()
    os.system('cls')
    if try_code == 'a':
        os.system('type nul > try.py')
        os.system('notepad try.py')
        input('Enter to go back')
        os.system('cls')
        continue
    elif try_code == 'b':
        os.system('cls')
        os.system('python try.py')
        continue
    elif try_code == 'x':
        break
    else:
        print('choose another')
        continue