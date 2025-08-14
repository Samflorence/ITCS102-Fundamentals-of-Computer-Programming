ammount=eval(input("Enter the amount to deposit:"))

n1 = ammount // 1000
m1 = ammount % 1000

n2 = m1 // 500
m2 = m1 % 500

n3 = m2 // 200
m3 = m2 % 200

n4 = m3 // 100
m4 = m3 % 100

n5 = m4 // 50
m5 = m4 % 50

n6 = m5 // 20
m6 = m5 % 20

n7 = m6 // 10
m7 = m6 % 10

n8 = m7 // 5
m8 = m7 % 5

n9 = m8 // 1
m9 = m8 % 1

print("Here is your breakdown to your deposit", ammount)
print(n1 ,"-₱1000") 
print(n2 ,"-₱500")    
print(n3 ,"-₱200") 
print(n4 ,"-₱100") 
print(n5 ,"-₱50") 
print(n6 ,"-₱20") 
print(n7 ,"-₱10") 
print(n8 ,"-₱5") 
print(n9 ,"-₱1")