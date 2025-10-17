name = input("Enter Your Name --> ")
print("\t++++++++++++++++++++++++++++++++++++++\n\tODD NUMBER SUMMATION, press 0 to stop\n\t++++++++++++++++++++++++++++++++++++++")
sum = 0
odd = ""
while True:
    ramdom_number = eval(input("Input a ramdom number --> "))
    if ramdom_number %2 == 1:
        print('ODD NUMBER DETECTED, continue')
        sum += ramdom_number
        odd += str(ramdom_number) + " "
        continue
    elif ramdom_number == 0:
        print('Program Stop!!!')
        break
    else:
        if ramdom_number %2 == 0:
            print('EVEN NUMBER DETECTED, continue')
        else:
            print('Invalid input')
        continue
print(f'Hi {name}, The sum of all ODD number is {sum}')
print(f'ODD numbers detected included the ff {odd}')