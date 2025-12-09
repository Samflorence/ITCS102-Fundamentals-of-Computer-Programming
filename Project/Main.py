import os
from Learning import *
print('Learn Python In Weeks Using This Code')
while True:
    print('\n===========================================')
    print('\n\t\t1 - 1st Week')
    print('\n\t\t2 - 2nd Week')
    print('\n\t\t3 - 3rd Week')
    print('\n\t\t4 - 4th Week')
    print('\n\t\t5 - Challenges')
    print('\n\t\tX - Exit')
    print('\n===========================================')
    count = input('\nPlease Select From Above: ').lower()
    
    if count == '1':
        os.system('cls')
        while True:
            print('\n~~~~~~~~~~~~~~~First Week~~~~~~~~~~~~~~~~~')
            print('\n\tA - What Is Python')
            print('\n\tB - Using the print() Function')
            print('\n\tC - Using the input() Function')
            print('\n\tD - Using the _______ Function')
            print('\n\tS - Try it yourself')
            print('\n\tT - Activity')
            print('\n\tX - Go Back')
            print('\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            day = input('Please Select From Above: ').lower()
            
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
                pass
                continue
            elif day == 'd':
                os.system('cls')
                pass
                continue
            elif day == 'x':
                break
            else:
                os.system('cls')
                print('Invalid Input Please Choose Again')
                continue    
        continue
    elif count == '2':
        pass
        continue
    elif count == '3':
        pass
        continue
    elif count == '4':
        pass
        continue
    elif count == '5':
        pass
        continue
    elif count == 'x':
        print('\nGood bye!')
        break
    else:
        os.system('cls')
        print('\nInput Invalid Please Choose Again')
        continue
