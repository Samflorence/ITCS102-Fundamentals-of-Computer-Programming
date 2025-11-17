import os 
os.system('cls')
print("Student Information System")
print("=============================")

student_record = {}#Empty Dictionary
while True:
    print("A - Add Student Record\nB - Print All student Record\nC - Search Student Record\nD - Delete Student Record\nE - Edit Student Record\nF - Export Student Record\nG - Exit System")
    choice = input("Select From the action above -->").lower()
    if choice == 'a' :
        os.system('cls')
        print("\nAdding new student record")

        id_no = input("Please Input Student ID number:")
        first_name = input("PLease input first name:").upper()
        last_name = input('Please input last name:').upper()
        age = eval(input('Please input age:'))
        section = input('Please input section:').upper()
        course = input('Please input course:').upper()
        student_record[id_no] = [first_name, last_name, age, course, section]
        print('Data Saved Successfully')
        continue 
    elif choice == 'b':
        os.system('cls')
        print('Printing Student Record')
        print(student_record)
        continue
    elif choice == 'c':
        pass
        continue
    elif choice == 'd':
        pass
        continue
    elif choice == 'e':
        pass
        continue
    elif choice == 'f':
        pass
        continue
    elif choice == 'g':
        print("Exit System")
        break
    else:
        print('Invalid Input')
        continue