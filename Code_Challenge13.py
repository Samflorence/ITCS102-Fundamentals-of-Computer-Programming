Name = input("Enter Your Name --> ")
print("\t++++++++++++++++++++++++++++++++++++++\n\tODD NUMBER SUMMATION, press 0 to stop\n\t++++++++++++++++++++++++++++++++++++++")

num = True
odd = 0
while num == True:
    ramdom_number = eval(input("Input a ramdom number --> "))
    if ramdom_number %2 == 1:
        print('ODD NUMBER DETECTED, continue')
        continue
        odd += ramdom_number 
    elif ramdom_number == 0:
        print('EVEN NUMBER DETECTED, continue')
        continue
    else:
        print('Program Stop!!!')
        break
print (odd)