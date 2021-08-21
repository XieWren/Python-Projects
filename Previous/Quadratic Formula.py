import math

print("Solving quadratic equation ax² + bx + c = 0...")
a = int(input("Enter the coefficient a: "))
if a == 0:
    print("Error. Coefficient 'a' cannot be 0.")
    a = int(input("Enter the coefficient a: "))
b = int(input("Enter the coefficient b: "))
c = int(input("Enter the coefficient c: "))

discriminant=b**2-4*a*c

if discriminant < 0:
    print("Complex Numbers.")
elif discriminant == 0:
    x=-b/(2*a)
    x=round(x,2)
    print("There is only one value of x which is "+str(x)+".")
else:
    x1=(-b+math.sqrt(discriminant))/(2*a)
    x1=round(x1,2)
    x2=(-b-math.sqrt(discriminant))/(2*a)
    x2=round(x2,2)
    print("There are two values of x which are "+str(x1)+" and "+str(x2)+".")
