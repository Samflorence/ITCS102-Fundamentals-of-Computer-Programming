import os
from Learning import *
import code
print('Learn Python In Weeks Using This Code')
while True:
    print('\n===========================================')
    print('\n\t\t1 - 1st Week')
    print('\t\t2 - 2nd Week')
    print('\t\t3 - 3rd Week')
    print('\t\t4 - 4th Week')
    print('\t\t5 - Challenges')
    print('\t\tX - Exit')
    print('\n===========================================')
    count = input('\nPlease Select From Above: ').lower()
    os.system('cls')
    if count == '1':
        while True:
            print('\n~~~~~~~~~~~~~~~First Week~~~~~~~~~~~~~~~~~')
            print('\n\tA - What Is Python')
            print('\tB - Using the print() Function')
            print('\tC - Using the input() Function')
            print('\tD - Using the ___ Function')
            print('\tS - Try it yourself')
            print('\tT - Activity')
            print('\tX - Go Back')
            print('\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            day = input('Please Select From Above: ').lower()
            os.system('cls')
            if day == 'a':
                os.system('cls')
                print('Coding is a coding language that is beginer friendly')
                input('Press Enter to continue: ')
                continue
            elif day == 'b':
                os.system('cls')
                printing()
                continue
            elif day == 'c':
                os.system('cls')
                inputing()
                continue
            elif day == 'd':
                os.system('cls')
                continue
            elif day == 's':
                # os.system('cls')
                # console = code.InteractiveConsole(globals())    
                # console.push("print('Welcome to the interactive console!')")
                # print('To exit input exit()')
                # console.interact("Enter your code below: ")
                continue
            elif day == 'x':
                print('Going Back')
                break
            else:
                os.system('cls')
                print('Invalid Input Please Choose Again')
                continue
        continue
    elif count == '2':
        while True:
            print('\n~~~~~~~~~~~~~~~Second Week~~~~~~~~~~~~~~~~~')
            print('\tA - ')
            print('\tB - ')
            print('\tC - ')
            print('\tD - ')
            print('\tS - Try it yourself')
            print('\tT - Activity')
            print('\tX - Go back')
            print('\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            day = input('Please Select From Above: ').lower()
            if day == 'a':
                pass
                continue
            elif day == 'b':
                pass 
                continue
            elif day == 'c':
                pass
                continue
            elif day == 'x':
                break
            else:
                os.system('cls')
                print('Invalid Input Please Choose Again')
        continue
    elif count == '3':
        while True:
            print('\n~~~~~~~~~~~~~~~Third Week~~~~~~~~~~~~~~~~~')
            print('\tA - ')
            print('\tB - ')
            print('\tC - ')
            print('\tD - ')
            print('\tS - Try it yourself')
            print('\tT - Activity')
            print('\tX - Go back')
            print('\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            day = input('Please Select From Above: ').lower()
            if day == 'a':
                pass
                continue
            elif day == 'b':
                pass 
                continue
            elif day == 'c':
                pass
                continue
            elif day == 'x':
                break
            else:
                os.system('cls')
                print('Invalid Input Please Choose Again')
        continue
    elif count == '4':
        while True:
            print('\n~~~~~~~~~~~~~~~Forth Week~~~~~~~~~~~~~~~~~')
            print('\tA - ')
            print('\tB - ')
            print('\tC - ')
            print('\tD - ')
            print('\tS - Try it yourself')
            print('\tT - Activity')
            print('\tX - Go back')
            print('\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            day = input('Please Select From Above: ').lower()
            if day == 'a':
                pass
                continue
            elif day == 'b':
                pass 
                continue
            elif day == 'c':
                pass
                continue
            elif day == 'x':
                break
            else:
                os.system('cls')
                print('Invalid Input Please Choose Again')
        continue
    elif count == '5':
        while True:
            print('\n~~~~~~~~~~~~~~~Fifth Week~~~~~~~~~~~~~~~~~')
            print('\tA - ')
            print('\tB - ')
            print('\tC - ')
            print('\tD - ')
            print('\tS - Try it yourself')
            print('\tT - Activity')
            print('\tX - Go back')
            print('\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            day = input('Please Select From Above: ').lower()
            if day == 'a':
                pass
                continue
            elif day == 'b':
                pass 
                continue
            elif day == 'c':
                pass
                continue
            elif day == 'x':
                break
            else:
                os.system('cls')
                print('Invalid Input Please Choose Again')
        continue
    elif count == 'x':
        print('\nGood bye!')
        break
    else:
        os.system('cls')
        print('\nInput Invalid Please Choose Again')
        continue
