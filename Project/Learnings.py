import os
import time
import random

#Introduction
def introduction():
    print('=' * 100)
    print("🐍 PYTHON LEARNING MENU")

    print('\n👋 Welcome!\
        \n\nThis program is designed to help beginners understand the basic concepts of Python\
        \nprogramming through simple examples and clear explanations.\
        \n\nEach lesson in this menu demonstrates how Python works, including loops, lists,\
        \nfunctions, and other important topics. Users can select a lesson from the menu\
        \nand learn step by step at their own pace.\
        \n\n👤 Created by: Sam Sio\
        \n🎓 Course: Information Technology\
        \n\nEnjoy learning Python and have fun exploring the basics of programming!')

    print('=' * 100)
    input('Press Enter to continue... ')
    os.system('cls')

#user information
def user():
    print('=' * 100)
    print("👤 USER INFORMATION")

    name = input("\nPlease enter your name: ")

    print(f"\n✨ Welcome, {name}!\
        \nThis Python learning menu is designed to guide you through the basics of programming\
        \nusing simple explanations and hands-on examples.\
        \n\nYou will explore topics such as loops, lists, functions, and other fundamental concepts.\
        \nTake your time, practice each lesson, and enjoy the learning process.\
        \n\nLet's begin your Python journey!")

    print('=' * 100)
    input('Press Enter to continue... ')
    os.system('cls')

#what is python
def python():
    print('=' * 100)
    print("\n📌 TOPIC: WHAT IS PYTHON")
    print('\n🧠 Explanation\n\
        \nPython is a high-level programming language used to create programs by writing clear and\
        \neasy-to-understand instructions. It is designed to be beginner-friendly and readable,\
        \nmaking it one of the best languages for new programmers.\
        \n\nPython is an interpreted language, which means the code runs line by line.\
        \nThis allows programmers to quickly identify and fix errors.\
        \n\nPython is versatile and widely used in web development, game creation, data analysis,\
        \nautomation, and artificial intelligence.\
        \n\n👤 Creator: Guido van Rossum\
        \n📅 First Release: 1991\n')
    print('=' * 100)
    input('\n➡ Press enter to continue...')
    os.system('cls')
    
#LESSON 1
# PRINT
def printing():
    print('=' * 100)
    print("\n📌 TOPIC: PRINT FUNCTION")
    print('\n▶ Example')
    print("print('Hello World')")
    print("\n🧠 Explanation - The print() function is one of the most basic and important functions in Python.\
          \nIt is used to display text, numbers, or results of calculations on the screen.\
          \nAnything written inside quotation marks is treated as text and will be printed exactly as it is written.\
          \nThis is often the first function learned by beginners because it helps show output and test code.\n")
    print('✅ Output')
    print('Hello World\n')
    print('=' * 100)
    input('\n➡ Press enter to continue...')
    os.system('cls')

# INPUT
def inputing():
    print('=' * 100)
    print("\n📌 TOPIC: INPUT FUNCTION")
    print('\n▶ Example')
    print("word = input('Enter any word')\nprint('You Enter the Word:', word)")
    print("\n🧠 Explanation - The input() function asks the user to type something using the keyboard.\
          \nWhen the user types a word and presses Enter, that value is SAVED inside a variable named 'word'.\
          \nA variable works like a container that stores data in memory.\
          \nAfter storing the input, the print() function is used to CALL the variable 'word' \
          \nand display its value on the screen. This is why whatever the user types is shown again \
          \nwhen print('You entered:', word) is executed.")
    print('\n✅ Output')
    word = input("Enter any word: ")
    print('You Enter the Word:', word, '\n')
    print('=' * 100)
    input('\n➡ Press Enter to continue...')
    os.system('cls')


# ESCAPE SEQUENCE
def escape_sequence():
    print('=' * 100)
    print("\n📌 Topic: ESCAPE SEQUENCE")
    print('\n▶ Example')
    print("print('Hello\\nWorld')")
    print('print("Hello\\tWorld")')
    print("Backslash: \\\\")
    print("\n🧠 Explanation - Escape sequences are special characters that start with a backslash (\\).\
          \nThey are used to format text inside strings.\
          \n\\n moves the text to a new line,\
          \n\\t adds a tab space,\
          \nand \\\\ prints a backslash.\
          \nEscape sequences make text output cleaner and more readable.")
    print('\n✅ Output')
    print("Hello\nWorld")
    print("Hello\tWorld")
    print('Backslash: \\\\\n')
    print('=' * 100)
    input('Press Enter to continue... ')
    os.system('cls')

# LEN()
def length_function():
    print('=' * 100)
    print('\n📌 Topic: LEN FUNCTION')
    print('\n▶ Example')
    print('print(len("Hello"))')
    print("\n🧠 Explanation - The len() function is used to count how many characters are in a string\
          \nor how many elements are inside a list or other collection.\
          \nIt helps programmers measure the size of data and is often used in loops and conditions.")
    print('\n✅ Output')
    print(len('Hello'), '\n')
    print('=' * 100)
    input('Press Enter to continue... ')
    os.system('cls')

#LESSON 2
# ARITHMETIC OPERATORS
def arithmetic_operators():
    print('=' * 100)
    print('\n📌 Topic: ARITHMETIC OPERATORS')
    print('\n▶ Example')
    print('a = 10\nb = 3\nprint("10 + 3 =", a + b)\nprint("10 - 3 =", a - b)\nprint("10 * 3 =", a * b)\
          \nprint("10 / 3 =", a / b)\nprint("10 % 3 =", a % b)\nprint("10 ** 3 =", a ** b)')
    print("\n🧠 Explanation - Arithmetic operators are used to perform mathematical calculations.\
          \nAddition (+) adds values, subtraction (-) subtracts values, multiplication (*) multiplies values,\
          \ndivision (/) divides values, modulo (%) finds the remainder,\
          \nand exponent (**) raises a number to a power.")
    print('\n✅ Output')
    a = 10
    b = 3
    print("\n10 + 3 =", a + b)
    print("10 - 3 =", a - b)
    print("10 * 3 =", a * b)
    print("10 / 3 =", a / b)
    print("10 % 3 =", a % b)
    print("10 ** 3 =", a ** b, '\n')
    print('=' * 100)
    input('Press Enter to continue... ')
    os.system('cls')

# ASSIGNMENT OPERATORS
def assignment_operators():
    print('=' * 100)
    print('\n📌 Topic: ASSIGNMENT OPERATORS')
    print('\n▶ Example')
    print('x = 10\nprint("x =", x)\nx += 5\nprint("x += 5 =", x)\nx *= 2\nprint("x *= 2 =", x)\nx /= 15\nprint("x /= 15 =", x)')
    print("\n🧠 Explanation - Assignment operators are used to assign and update values in variables.\
          \nInstead of writing long equations, these operators shorten the code.\
          \nFor example, x += 5 means the current value of x is increased by 5.")
    print('\n✅ Output')
    x = 10
    print("\nx =", x)
    x += 5
    print("x += 5 =", x)
    x *= 2
    print("x *= 2 =", x)
    x /= 15
    print("x /= 15 =", x, '\n')
    print('=' * 100)
    input('Press Enter to continue... ')
    os.system('cls')

# RATIONAL OPERATORS
def rational_operators():
    print('=' * 100)
    print('\n📌 Topic: RATIONAL OPERATORS')
    print('\n▶ Example')
    print('print("5 == 5:", 5 == 5)\nprint("5 != 3:", 5 != 3)\nprint("5 > 3 :", 5 > 3)\nprint("5 < 3 :", 5 < 3)')
    print('=' * 100)
    print("\n🧠 Explanation - Relational operators compare two values and return either True or False.\
          \nThey are commonly used in decision-making statements like if and while.\
          \nThese operators help programs make choices based on conditions.")
    print('\n✅ Output')
    print("\n5 == 5:", 5 == 5)
    print("5 != 3:", 5 != 3)
    print("5 > 3 :", 5 > 3)
    print("5 < 3 :", 5 < 3,' \n')
    print('=' * 100)
    input('Press Enter to continue... ')
    os.system('cls')

# LOGICAL OPERATORS
def logical_operators():
    print('=' * 100)
    print('\n📌 Topic: LOGICAL OPERATORS')
    print('\n▶ Example')
    print('x = 5\nprint("(x > 2 and x < 10):", x > 2 and x < 10)\nprint("(x < 2 or x == 5):", x < 2 or x == 5)\nprint("not(x > 2):", not(x > 2))')
    print("\n🧠 Explanation - Logical operators are used to combine multiple conditions.\
          \n'and' returns True only if both conditions are True.\
          \n'or' returns True if at least one condition is True.\
          \n'not' reverses the result of a condition.")
    print('\n✅ Output')
    x = 5
    print("\n(x > 2 and x < 10):", x > 2 and x < 10)
    print("(x < 2 or x == 5):", x < 2 or x == 5)
    print("not(x > 2):", not(x > 2), '\n')
    print('=' * 100)
    input('Press Enter to continue... ')
    os.system('cls')

#Lesson 3
# STRING FORMATTING
def string_formatting():
    print('=' * 100)
    print('\n📌 Topic: STRING FORMATING')
    print('\n▶ Example')
    print('name = "Sam"\nage = 18\nprint("Using ,__,: My name is",name, "and I am", age)\
      \nprint(f"Using f-string : My name is {name} and I am {age}.")')
    print("\n🧠 Explanation - String formatting allows variables to be inserted into a string \
          \ninstead of writing text manually. In this example, the values stored in the variables\
          \n'name' and 'age' are CALLED and placed inside the string.\
          \nThe ,__, method replaces the curly braces {} with the values of the variables in order.\
          \nThe f-string directly reads the variables inside the string and prints their values \
          \nautomatically when print() is executed.")
    print('\n✅ Output')
    name = "Sam"
    age = 18
    print("Using ,__,: My name is",name, "and I am", age)
    print(f"Using f-string : My name is {name} and I am {age}.\n")
    print('=' * 100)
    input('Press Enter to continue... ')
    os.system('cls')

# CONDITIONAL STATEMENT
def conditional_statement():
    print('=' * 100)
    print('\n📌 Topic: IF AND ELSE STATEMENT')
    print('\n▶ Example')
    print('age = 18\nif age >= 18:\n\tprint("You are an adult.")\nelse:\n\tprint("You are a minor.")')
    print("\n🧠 Explanation - The if-else statement checks a condition before deciding which code will run.\
          \nThe value stored in the variable 'age' is COMPARED using a relational operator.\
          \nIf the condition evaluates to True, the print() inside the if block is CALLED and executed.\
          \nIf the condition is False, the print() inside the else block is executed instead.")
    print('\n✅ Output')
    age = 18
    if age >= 18:
        print("\nYou are an adult.\n")
    else:
        print("\nYou are a minor.\n")
    print('=' * 100)
    input('Press Enter to continue... ')
    os.system('cls')

# IF AND ELIF
def if_elif():
    print('=' * 100)
    print('\n📌 Topic: IF, ELIF, ELSE STATEMENT')
    print('\n▶ Example')
    print('grade = 85\nif grade >= 90:\n\tprint("A")\nelif grade >= 80:\n\tprint("B")\nelif grade >= 70:\n\tprint("C")\nelse:\n\tprint("F")')
    print("\n🧠 Explanation - The if-elif-else structure checks multiple conditions one by one.\
          \nThe value stored in the variable 'grade' is compared against each condition from top to bottom.\
          \nOnce a condition becomes True, the corresponding print() statement is CALLED and executed,\
          \nand the remaining conditions are skipped.")
    print('\n✅ Output')
    grade = 85
    if grade >= 90:
        print("\nA\n")
    elif grade >= 80:
        print("\nB\n")
    elif grade >= 70:
        print("\nC\n")
    else:
        print("\nF\n")
    print('=' * 100)
    input('Press Enter to continue... ')
    os.system('cls')

#Lesson 4
# FOR LOOP
def loop_section():
    print('=' * 100)
    print('\n📌 Topic: FOR LOOP')
    print('\n▶ Example')
    print('for i in range(1, 6, 1):\n\tprint("Number:", i)')
    print("\n🧠 Explanation - The for loop is used to repeat a block of code multiple times.\
          \nThe range(start, stop, step) function controls how the loop runs.\
          \nThe loop starts at 1, stops before reaching 6, and increases by 1 each time.\
          \nDuring each loop cycle, the current number is stored in the variable 'i'.\
          \nThe print() function then CALLS the value stored in 'i' and displays it on the screen.")
    print('\n✅ Output')
    for i in range(1, 6, 1):
        print("Number:", i)
    print()
    print('=' * 100)
    input('Press Enter to continue... ')
    os.system('cls')

# SUM AUTOMATION
def sum_automation():
    print('=' * 100)
    print('\n📌 Topic: SUM AUTOMATION')
    print('\n▶ Example')
    print('total = 0\nfor i in range(1, 11, 1):\n\ttotal += i\nprint("\nTotal =", total)')
    print("\n🧠 Explanation - This program uses a for loop to automatically add numbers.\
          \nThe variable 'total' is used to store the running sum.\
          \nEach time the loop runs, the current value stored in 'i' is added to 'total'.\
          \nAfter the loop finishes, print() CALLS the final value stored in 'total' and displays the result.")
    print('\n✅ Output')
    total = 0
    for i in range(1, 11, 1):
        total += i
    print("\nTotal =", total)
    print()
    print('=' * 100)
    input('Press Enter to continue... ')
    os.system('cls')

# DESCENDING LOOP
def descending_loop():
    print('=' * 100)
    print('\n📌 Topic: DESCENDING LOOP')
    print('\n▶ Example')
    print('for i in range(10, 0, -1):\n\tprint(i)')
    print("\n🧠 Explanation - This loop counts backward by using a negative step value in range().\
          \nThe loop starts at 10 and decreases by 1 each time until it reaches 1.\
          \nEach number is stored in the variable 'i'.\
          \nThe print() function CALLS the value of 'i' during each loop cycle and prints it on the screen.")
    print('\n✅ Output')
    for i in range(10, 0, -1):
        print(i)
    print()
    print('=' * 100)
    input('Press Enter to continue... ')
    os.system('cls')

# HORIZONTAL END
def horizontal_end():
    print('=' * 100)
    print('\n📌 Topic: HORIZONTAL END')
    print('\n▶ Example')
    print('for i in range(5, 0, -1):\nprint(i, end=" ")')
    print("\n🧠 Explanation - A nested loop means one loop runs inside another loop.\
          \nThe outer loop controls the number of rows, while the inner loop controls how many stars are printed per row.\
          \nEach time the outer loop runs, the inner loop prints stars based on the current value of 'i'.\
          \nThe print() function is called repeatedly to create a pattern.")
    print('\n✅ Output')
    for i in range(5, 0, -1):
        print(i, end=" ")
    print('\n')
    print('=' * 100)
    input('Press Enter to continue... ')
    os.system('cls')

# NESTED LOOP (DESCENDING)
def nested_loop():
    print('=' * 100)
    print('\n📌 Topic: NESTED LOOP ( DESCENDING STAR )')
    print('\n▶ Example')
    print('for i in range(5, 0, -1):\n\tfor j in range(i):\n\t\tprint("*", end=" ")\n\tprint()')
    print("\n🧠 Explanation - A nested loop means one loop runs inside another loop.\
          \nThe outer loop controls the number of rows, while the inner loop controls how many stars are printed per row.\
          \nEach time the outer loop runs, the inner loop prints stars based on the current value of 'i'.\
          \nThe print() function is called repeatedly to create a pattern.")
    print('\n✅ Output')
    for i in range(5, 0, -1):
        for j in range(i):
            print("*", end=" ")
        print()
    print()
    print('=' * 100)
    input('Press Enter to continue... ')
    os.system('cls')

# WHILE LOOP
def while_loop_section():
    print('=' * 100)
    print('\n📌 Topic: WHILE LOOP')
    print('\n▶ Example')
    print('x = 1\nwhile x <= 5:\n\tprint("Count:", x)\n\tx += 1')
    print("\n🧠 Explanation - The while loop continues running as long as the condition is True.\
          \nThe value stored in 'x' is checked before every loop iteration.\
          \nEach time the condition is True, print() is CALLED to display the current value of 'x',\
          \nthen 'x' is updated until the condition becomes False.")
    print('\n✅ Output')
    x = 1
    while x <= 5:
        print("Count:", x)
        x += 1
    print()
    print('=' * 100)
    input('Press Enter to continue... ')
    os.system('cls')

#Lesson 5
# IMPORT RANDOM
def import_random():
    print('=' * 100)
    print('\n📌 Topic: IMPORT RAMDOM')
    print('\n▶ Example')
    print('import random\nprint("\nRandom number (1 - 10):", random.randint(1, 10))')
    print("\n🧠 Explanation - The random module is a built-in Python module used to generate random values.\
          \nWhen 'import random' is executed, Python loads the module so its functions can be used.\
          \nThe randint(1, 10) function randomly selects an integer between 1 and 10.\
          \nThe print() function CALLS the generated random number and displays it on the screen.")
    print('\n✅ Output')

    print("\nRandom number (1 - 10):", random.randint(1, 10))
    print()
    print('=' * 100)
    input('Press Enter to continue... ')

# LIST OPERATION
def list_operation():
    print('=' * 100)
    print('\n📌 Topic: LIST OPERATION')
    print('\n▶ Example')
    print("anime = ['one piece','naruto','solo leveling','dan da dan']\nprint(anime)\nprint(anime[3])\nprint(anime[2 : 4])\
        \n\nanime.append('death note')\nprint(anime)\n\nanime.insert(2 , 'jujutsu kaisen')\nprint(anime)\n\nanime.remove('naruto')\
        \nprint(anime)\n\nanime.pop()\nprint(anime)\n\nprint(len(anime))\n\nanime.sort()\nprint(anime)\nanime.reverse()\nprint(anime)")
    print('\n🧠 Explanation - Lists are used to store multiple values in a single variable.\
        \nEach value has an index starting from 0, which allows you to access or modify specific items.\
        \nThe print() function CALLS the list or selected elements to display their current state on the screen.\
        \nCommon list functions demonstrated in this lesson:\
        \n- append(): Adds a value at the end of the list\
        \n- insert(): Adds a value at a specified index\
        \n- remove(): Deletes a value by name\
        \n- pop(): Removes a value by index (default is last item)\
        \n- len(): Returns the number of items in the list\
        \n- sort(): Arranges the list in ascending order\
        \n- reverse(): Reverses the order of items in the list')
    print('\n✅ Output')
    anime = ['one piece','naruto','solo leveling','dan da dan']
    print(anime)
    print(anime[3])
    print(anime[2 : 4])

    anime.append('death note')
    print(anime)

    anime.insert(2 , 'jujutsu kaisen')
    print(anime)

    anime.remove('naruto')
    print(anime)

    anime.pop()
    print(anime)

    print(len(anime))

    anime.sort()
    print(anime)

    anime.reverse()
    print(anime)
    print()
    print('=' * 100)
    input('Press Enter to continue... ')

# IMPORTING DEF
def importing_def():
    print('=' * 100)
    print('\n📌 Topic: IMPORTING DEF')
    print('\n▶ Example')
    print("def example():\n\tprint('This is an example of def')\nexample()")
    print("\n🧠 Explanation - Functions in Python can be called from inside other functions.\
        \nThis allows code reuse and better organization.\
        \nWhen example() is called, Python jumps to the example() function,\
        \nexecutes all the code inside it, and then returns back to this function.\
        \nThis shows how functions are connected and how execution flows in a program.")
    print('\n✅ Output')
    def example():
        print('This is an example of def')
    example()
    print()
    print('=' * 100)
    input('Press Enter to continue... ')

# DICTIONARY OPERATION
def dictionary_operation():
    print('=' * 100)
    print('\n📌 Topic: DICTIONARY OPERATION')
    print('\n▶ Example')
    print('student = {"name": "Sam", "age": 18, "course": "IT"}\nprint("\nOriginal:", student)\nstudent["age"] = 19\nprint("Updated:", student)')
    print("\n🧠 Explanation - A dictionary stores data using key-value pairs.\
        \nEach key is used to access its corresponding value.\
        \nValues can be updated by referring to their key name.\
        \nThe print() function CALLS the dictionary before and after the update to show the changes.")
    print('\n✅ Output\n')
    student = {"name": "Sam", "age": 18, "course": "IT"}
    print("\nOriginal:", student)
    student["age"] = 19
    print("Updated:", student)
    print('=' * 100)
    input('Press Enter to continue... ')

#Notepad coding
def coding():
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
            input('\nPress Enter to continue... ')
            os.system('cls')
            continue
        elif try_code == 'x':
            break
        else:
            print('choose another')
            continue

#loading
def loading():
    symbols = ['|', '/', '—', '\\']
    for i in range(8):
        print(f'\rProcessing {symbols[i % 4]}', end='')
        time.sleep(0.2)
    os.system('cls')

#activity 1
def activity_1():
    print('Look at the output shown below. Your task is to write one Python program that produces the same output.')
    print('=' * 104)
    
    print('\n\tPython Basics Activity')

    name = input('\nEnter your name: ')
    print(f'\nHello {name}!')
    print('\tyour name has', (len(name)), 'characters')
    print()
    print('=' * 104)

    input('\nClick Enter to try it in [S] Try it yourself: ')
    os.system('cls')

#activity 2
def activity_2():
    print('Look at the output shown below. Your task is to write one Python program that produces the same output.')
    print('=' * 104)
    
    print("\n\tOperators Activity")

    a = int(input("\nEnter first number: "))
    b = int(input("Enter second number: "))

    print("\n[A] Arithmetic Operation")
    print("\tSum:", a + b)
    print("\tDifference:", a - b)
    print("\tProduct:", a * b)
    print("\tQuotient:", a / b)

    print("\n[B] Assignment Operation")
    x = a
    x += b
    print("\tx after += :", x)
    x -= b
    print("\tx after -= :", x)

    print("\n[C] Relational Operation")
    print("\tIs first number greater than second?", a > b)
    print("\tIs first number equal to second?", a == b)

    print("\n[D] Logical Operation")
    print("\tIs both numbers positive?", a > 0 and b > 0)

    print()
    print('=' * 104)
    input('\nClick Enter to try it in [S] Try it yourself: ')
    os.system('cls')

#activity 3
def activity_3():
    print('Look at the output shown below. Your task is to write one Python program that produces the same output.')
    print('=' * 104)
    
    print("\n\tString Activity")
    print('\n90 - 100 → Excellent\n80-89 → Very Good\n75-79 → Good\nBelow 75 → Try Again')
    name = input("\nEnter your name: ")
    score = int(input("Enter your score: "))

    print(f"\nHello {name}!")
    print(f"\tYour score is {score}.")
    
    if score >= 90 and score <= 100:
        print("\tExcellent!")
    elif score >= 80 and score <= 89:
        print("\tVery Good!")
    elif score >= 75 and score <= 79:
        print("\tGood!")
    else:
        print("\tTry Again!")
    print()
    print('=' * 104)
    input('\nClick Enter to try it in [S] Try it yourself: ')
    os.system('cls')

#activity 4
def activity_4():
    print('Look at the output shown below. Your task is to write one Python program that produces the same output.')
    print('=' * 104)

    print('\n\tDiamond Loop Acivity')
    for x in range(1, 11,1):
        for i in range(10, x, -1):
            print(" ", end=" ")
        for b in range(1, x, 1):
            print('*',end=" ")
        for v in range(1, x, 1):
            print("*",end=" ")
        print()

    for x in range(1, 11,1):
        for i in range(1, x, 1):
            print(" ", end=" ")
        for b in range(10, x, -1):
            print('*',end=" ")
        for v in range(10, x, -1):
            print("*",end=" ")
        print()
    print()
    print('=' * 104)
    input('\nClick Enter to try it in [S] Try it yourself: ')
    os.system('cls')

#activity 5
def activity_5():
    print('Look at the output shown below. Your task is to write one Python program that produces the same output.')
    print('=' * 104)
    
    print("\n\tData & Functions Activity")

    rand_num = random.randint(1, 10)
    print(f"\n[A] Random Number\n\tRandom number between 1 and 10: {rand_num}")

    my_list = [10, 20, 30]
    print(f"\n[B] List Operation\n\tMy list: {my_list}")
    my_list.append(40)
    print(f"\tAdd 40: {my_list}")
    my_list.remove(20)
    print(f"\tRemove 20: {my_list}")

    def add(a, b):
        return a + b

    result = add(5, 3)
    print(f"\n[C] Using Function\n\tResult of add(5, 3): {result}")

    student = {'name': 'Juan', 'age': 18}
    print(f"\n[D] Dictionary Operation\n\tStudent: {student}")
    student['age'] = 19
    print(f"\tUpdate age to 19: {student}")
    
    print()
    print('=' * 104)

    input('\nClick Enter to try it in [S] Try it yourself: ')
    os.system('cls')

#challenge_1
def challenge_1():
    print('Instructions:\n- Ask the user for their name.\
        \n- Ask the user for a number n.\
        \n- Print numbers from 1 to n using a for loop.\
        \n- Calculate the sum of numbers from 1 to n and display it.\
        \n- If the sum is even, print "Your sum is even!"; else print "Your sum is odd!".\
        \n- Use \\n and \\t for formatting.')
    
    print()
    print('=' * 50)
    name = input("Enter your name: ")
    n = int(input("Enter a number: "))

    print(f"\nHello {name}!\nNumbers from 1 to {n}:")
    total = 0
    for i in range(1, n + 1):
        print(i)
        total += i

    print(f"Sum: {total}")
    if total % 2 == 0:
        print("Your sum is even!")
    else:
        print("Your sum is odd!")
    input('\nClick Enter to try it in [S] Try it yourself: ')
    os.system('cls')

#challenge_2
def challenge_2():
    print('Instructions:\n- Ask the user for their name and score (0-100).\
        \n- Create a function that takes the score and returns a grade:\
        \n- 90-100 → Excellent\
        \n- 80-89 → Very Good\
        \n- 75-79 → Good\
        \n- Below 75 → Try Again\
        \n- Display a greeting using f-strings: "Hello <name>! Your grade is <grade>."\
        \n- Using a for loop, print a star * pattern where the number of stars = tens digit of the score.\
        \n- Use \\t for formatting the star pattern.')
    
    print()
    print('=' * 50)
    name2 = input("Enter your name: ")
    score = eval(input("Enter your score (0-100): "))

    def get_grade(score):
        if 90 <= score <= 100:
            return "Excellent"
        elif 80 <= score <= 89:
            return "Very Good"
        elif 75 <= score <= 79:
            return "Good"
        else:
            return "Try Again"

    grade = get_grade(score)
    print(f"\nHello {name2}! Your grade is {grade}.")

    print("Star pattern:")
    stars = score // 10
    for i in range(stars):
        print("\t* " * stars)
    input('\nClick Enter to try it in [S] Try it yourself: ')
    os.system('cls')

#chalenge_3
def challenge_3():
    print('Instructions:\n- Ask the user 3 random addition questions with numbers from 1 to 10.\
        \n- Store each question, the user\'s answer, and the correct answer in a dictionary.\
        \n- Create a function that checks if the user\'s answer is correct.\
        \n- Keep track of the total correct answers.\
        \n- After the quiz, display each question, the user\'s answer, and whether it was correct.\
        \n- Finally, display the total correct answers and a performance message:\
        \n- 3 correct → Excellent\
        \n- 2 correct → Good\
        \n- 1 correct → Try Again\
        \n-0 correct → Better Luck Next Time\
        \n- Use \\n and \\t for formatting the output.')

    print()
    print('=' * 50)

    def check_answer(correct, user):
        if correct == user:
            return True
        else:
            return False

    quiz_results = {} 
    score = 0 

    for i in range(1, 4):
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        correct_answer = num1 + num2
        user_answer = int(input(f"Question {i}: {num1} + {num2} = "))
        
        is_correct = check_answer(correct_answer, user_answer)
        quiz_results[f"Question {i}: {num1} + {num2}"] = (user_answer, is_correct, correct_answer)
        
        if is_correct:
            print("Correct!\n")
            score += 1
        else:
            print(f"Incorrect, the correct answer is {correct_answer}\n")

    print(f"You got {score} out of 3 correct.\nPerformance: ", end="")
    if score == 3:
        print("Excellent")
    elif score == 2:
        print("Good")
    elif score == 1:
        print("Try Again")
    else:
        print("Better Luck Next Time")
    input('\nClick Enter to try it in [S] Try it yourself: ')
    os.system('cls')
