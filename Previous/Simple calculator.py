print("*****Types of operation*****\n\
1. +\n\
2. -\n\
3. *\n\
4. /\n\
***************************")
x=int(input("Key in the number for operator (1 to 4): "))
while x <= 0 or x > 4:
    x=int(input("Key in the number for operator (1 to 4): "))
y=float(input("Enter your first number: "))
z=float(input("Enter your second number: "))
if x==1:
    print(y+z)
elif x==2:
    print(y-z)
elif x==3:
    print(y*z)
elif x==4:
    print(y/z)
