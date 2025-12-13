import os
from Learnings import * 
while True:
    print('~~~~~~~~~~~[ MENU ]~~~~~~~~~~~~')
    print('\n\t[1] 1st Week')
    print('\t[2] 2st Week')
    print('\t[3] 3st Week')
    print('\t[4] 4st Week')
    print('\t[5] 5th Week')
    print('\t[6] Challenges')
    print('\t[X] Exit')
    choose = input('\nChoose a lesson ➤  ')
    os.system('cls')
    
    if choose == '1':
        os.system('cls')
        while True:
            loading()
            print('\n~~~~~~~~~~~~~~~[ FIRST WEEK ]~~~~~~~~~~~~~~~~~')
            print('\n\t[A] What Is Python\
                  \n\t[B] Using the print() Function\
                  \n\t[C] Using the input() Function\
                  \n\t[D] Using the len() Function\
                  \n\t[E] Understanding Escape Sequence\
                  \n\t[S] Try it Yourself\
                  \n\t[T] Activity\
                  \n\t[X] Go Back')
            day = input('\nChoose a lesson ➤  ').lower()
            os.system('cls')
            if day == 'a':
                print('\nPython is a popular programming language. It was created by Guido van Rossum, and released in 1991.')
                input('Press Enter to continue: ')
                os.system('cls')
                continue
            elif day == 'b':
                printing()
                continue
            elif day == 'c':
                inputing()
                continue
            elif day == 'd':
                length_function()
                continue
            elif day == 'e':
                escape_sequence()
                continue
            elif day == 's':
                coding()
                continue
            elif day == 't':
                activity_1()
                continue
            elif day == 'x':
                loading()
                break
            else:
                print("\nInvalid Input Please Choose From The Above")
                continue
        continue
    elif choose == '2':
        while True:
            loading()
            print('\n~~~~~~~~~~~~~~~[ SECOND WEEK ]~~~~~~~~~~~~~~~~~')
            print('\n\t[A] Understanding Aritmetic Operation\
                  \n\t[B] Understanding Assignment Operation\
                  \n\t[C] Understanding Rational Operation\
                  \n\t[D] Understanding Logical Operation\
                  \n\t[S] Try it yourself\
                  \n\t[T] Activity\
                  \n\t[X] Go Back')
            day = input('\nChoose a lesson ➤  ').lower()
            os.system('cls')
            if day == 'a':
                arithmetic_operators()
                continue
            elif day == 'b':
                assignment_operators()
                continue
            elif day == 'c':
                rational_operators()
                continue
            elif day == 'd':
                logical_operators()
                continue 
            elif day == 's':
                coding()
                continue 
            elif day == 't':
                activity_2()
                continue
            elif day == 'x':
                loading()
                break
            else:
                os.system('cls')
                print('Invalid Input Please Choose Again')
        continue
    elif choose == '3':
        loading()
        while True:
            print('\n~~~~~~~~~~~~~~~[ THIRD WEEK ]~~~~~~~~~~~~~~~~~')
            print('\n\t[A] Understanding String Formating\
                  \n\t[B] Understanding Conditional Statement\
                  \n\t[C] Understanding if, elif, else Statement\
                  \n\t[S] Try it yourself\
                  \n\t[T] Activity\
                  \n\t[X] Go Back')
            day = input('\nChoose a lesson ➤  ').lower()
            os.system('cls')
            if day == 'a':
                string_formatting()
                continue
            elif day == 'b':
                conditional_statement() 
                continue
            elif day == 'c':
                if_elif()
                continue
            elif day == 's':
                coding()
                continue 
            elif day == 't':
                activity_3()
                continue
            elif day == 'x':
                loading()
                break
            else:
                os.system('cls')
                print('Invalid Input Please Choose Again')
        continue
    elif choose == '4':
        loading()
        while True:
            print('\n~~~~~~~~~~~~~~~[ FORTH WEEK ]~~~~~~~~~~~~~~~~~')
            print('\n\t[A] Understanding For Loop\
                  \n\t[B] Understanding Sum Automation\
                  \n\t[C] Understanding Descending Loop\
                  \n\t[D] Understanding Horizontal End\
                  \n\t[E] Understanding Nested Loop\
                  \n\t[F] Understanding While Loop\
                  \n\t[S] Try it yourself\
                  \n\t[T] Activity\
                  \n\t[X] Go Back')
            day = input('\nChoose a lesson ➤  ').lower()
            os.system('cls')
            if day == 'a':
                loop_section()
                continue
            elif day == 'b':
                sum_automation()
                continue
            elif day == 'c':
                descending_loop()
                continue
            elif day == 'd':
                horizontal_end()
                continue
            elif day == 'e':
                nested_loop()
                continue
            elif day == 'f':
                while_loop_section()
                continue
            elif day == 's':
                coding()
                continue 
            elif day == 't':
                activity_4()
                continue
            elif day == 'x':
                loading()
                break
            else:
                os.system('cls')
                print('Invalid Input Please Choose Again')
        continue
    elif choose == '5':
        loading()
        while True:
            print('\n~~~~~~~~~~~~~~~[ FIFTH WEEK ]~~~~~~~~~~~~~~~~~')
            print('\n\t[A] Understanding Import Ramdom\
                  \n\t[B] Understanding List Operation\
                  \n\t[C] Understanding Importing Def\
                  \n\t[D] Understanding Dictionary Operation\
                  \n\t[S] Try it yourself\
                  \n\t[T] Activity\
                  \n\t[X] Go Back')
            day = input('\nChoose a lesson ➤  ').lower()
            os.system('cls')
            if day == 'a':
                import_random()
                continue
            elif day == 'b':
                list_operation()
                continue
            elif day == 'c':
                importing_def()
                continue
            elif day == 'd':
                dictionary_operation()
                continue
            elif day == 's':
                coding()
                continue 
            elif day == 't':
                activity_5()
                continue
            elif day == 'x':
                loading()
                break
            else:
                os.system('cls')
                print('Invalid Input Please Choose Again')
        continue
    elif choose == '6':
        loading()
        while True:
            print('\n~~~~~~~~~~~~~~~[ CHALLENGES ]~~~~~~~~~~~~~~~~~')
            print('\t[A] Beginner Level\
                  \n\t[B] Intermediate Level\
                  \n\t[C] Advance Level\
                  \n\t[S] Try it Yourself\
                  \n\t[X] Go Back')
            level = input('\nChoose a lesson ➤  ').lower()
            os.system('cls')

            if level == 'a':
                challenge_1()
                continue
            elif level == 'b':
                challenge_2()
                continue
            elif level == 'c':
                challenge_3()
                continue
            elif level == 's':
                coding()
            elif level == 'x':
                loading()
                break
            else:
                os.system('cls')
                print('Invalid Input Please Choose Again')
        continue
    elif choose == 'x':
        print('\nGood bye!')
        break
    else:
        os.system('cls')
        print('\nInput Invalid Please Choose Again')
        continue