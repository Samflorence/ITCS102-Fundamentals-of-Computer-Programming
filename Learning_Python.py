import os
print('Learn Python In Weeks Using This Code')
while True:
    print('\n===========================================')
    print('\n\t\t1 - 1st Week\n\t\t2 - 2nd Week\n\t\t3 - 3rd Week\n\t\t4 - 4th Week\n\t\tX - Exit')
    print('\n===========================================')
    count = input('\nPlease Select From Above: ')
    
    if count == '1':
        os.system('cls')
        while True:
            print('\nFirst Week')
            print('\n===========================================')
            print('\n\tA - What Is Python\n\tB - Basic Printing in python\n\tC - Go Back')
            print('\n===========================================')
            day = input('Please Select From Above: ')
            
            if day == 'a':
                pass
                continue
            elif day == 'b':
                pass
                continue
            elif day == 'c':
                pass
                break
            else:
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
    elif count == 'x':
        print('\nExiting')
        break
    else:
        print('\nInput Invalid Please Choose Again')
        continue