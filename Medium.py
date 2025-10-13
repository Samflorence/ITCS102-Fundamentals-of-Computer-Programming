column = eval(input("Enter how many column you want --> "))
for x in range(1, 11, 1):
    for z in range(1, column + 1, 1):
        print(f'{x} x {z} = {x*z}',end=("\t"))
    print()

for x in range(1, 6, 1):
    for z in range(6, x, -1):
        print(" ",end=(""))
    for c in range(1, x + 1, 1):
        print("* ",end=(""))
    print()