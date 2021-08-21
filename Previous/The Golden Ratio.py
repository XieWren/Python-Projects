import random
phi=float(input("Enter a number: "))
phi_not=phi
while True:
    phi_not=phi
    phi=(1/phi)+1
    print(phi)
##    print("Calculating... "+str(random.randint(1,100)*phi/1.618033988749895*100)+"% complete")
    if phi==phi_not:
        break
print("The Golden Ratio: "+str(phi))
