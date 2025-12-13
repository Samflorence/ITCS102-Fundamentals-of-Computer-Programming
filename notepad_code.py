  while True:
        print('~~~~~~~~~~~~~~~~~~~[ Remiders ]~~~~~~~~~~~~~~~~~~~~~')
        print("- Always save before closing notepad (ctrl + s)\n- Once you save, returning to A will erase your code.")
        try_code = input('\t\tA - try code\n\t\tB - output\n\t\tX - Exit\nChoose ➤ ').lower()
        os.system('cls')
        if try_code == 'a':
            os.system('type nul > try.py')
            os.system('notepad try.py')
            input('Enter to go back')
            os.system('cls')
            continue
        elif try_code == 'b':
            os.system('python try.py')
            input('\nPress Enter to continue: ')
            os.system('cls')
            continue
        elif try_code == 'x':
            break
        else:
            print('choose another')
            continue
