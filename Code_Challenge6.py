#enter 10 random numbers, then get the summation of all odd numbers

print('Odd Number Summation')

num = 0

for x in range(1, 11, 1):
    number = eval(input('Enter Ramdom Number --> '))
    if number % 2:
        num += number

print("This is the summation of all odd number:",num)