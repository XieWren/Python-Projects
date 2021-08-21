import math
x1=input("Enter the x part of coordinate 1: ")
y1=input("Enter the y part of coordinate 1: ")
x2=input("Enter the x part of coordinate 2: ")
y2=input("Enter the y part of coordinate 2: ")
count=3
perimeter=math.sqrt((float(x2)-float(x1))**2+(float(y2)-float(y1))**2)
x_start=x1
y_start=y1
while count>0:
    x1=x2
    y1=y2
    x2=input("Enter the x part of coordinate "+str(count)+" (or blank to quit): ")
    if str(x2).isspace():
        break
    y2=input("Enter the y part of coordinate "+str(count)+":")
    count+=1
    perimeter+=math.sqrt((float(x2)-float(x1))**2+(float(y2)-float(y1))**2)
x2=x_start
y2=y_start
perimeter+=math.sqrt((float(x2)-float(x1))**2+(float(y2)-float(y1))**2)
print("The perimeter of the polygon is: "+str(perimeter))
