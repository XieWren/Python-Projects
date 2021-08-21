##Initialising
import math
arranged=[]
value_list=[]
lower_half=[]
upper_half=[]
total=0
variance=0

##Entering values
value=input("Enter a number: ")
while not(not value.isalpha() and value.isalnum()):##Ensuring values entered can only be positive whole numbers
    print("Error. Please enter only positive whole numbers.")
    value=input("Enter a number: ")
value_list.append(value)
while value!="End":
    value=input("Enter more numbers (or enter 'End' to end): ")
    while not(not value.isalpha() and value.isalnum()) and value!="End":
        print("Error. Please enter only numbers.")
        value=input("Enter more numbers (or enter 'End' to end): ")
    value_list.append(value)
value_list.pop()
length=len(value_list)


##Rearranging in ascending order
while len(value_list)!=0:
    smallest=value_list[0]
    for value in value_list:
        if int(value)<int(smallest):
            smallest=value
    arranged.append(smallest)
    value_list.remove(smallest)


##Finding min and max
minimum=int(arranged[0])
maximum=int(arranged[-1])


##Finding HCF:
check=True
for value in arranged:
    if int(value)<=0:
        check=False
        HCF="Not Applicable"
if check:
    for number in range(1,int(maximum)+2):
        for value in arranged:
            if int(value)%number!=0:
                break
            elif int(value)==arranged[-1]:
                HCF=number
            
        
##Finding LCM:
number=maximum
found=False
while not found:
    found=True
    for value in arranged:
        if number%int(value)!=0:
            found=False
            number+=1
            break
    LCM=number

    
##Finding sum and mean
for value in arranged:
    total+=int(value)
total=round(total,3)
mean=round(total/len(arranged),3)

##Finding variance and S.D.
for value in arranged:
    variance+=int(value)**2
variance=variance/len(arranged)-mean**2
Standard_Deviation=round(math.sqrt(variance),3)
variance=round(variance,3)

##Finding median
if len(arranged)%2==1:
    median=arranged[int(len(arranged)/2-0.5)]
    arranged.remove(median)
else:
    median=(int(arranged[int(len(arranged)/2-1)])+int(arranged[int(len(arranged)/2-2)]))/2


##Separating halves
q1="Not Applicable"
q3="Not Applicable"
interquartile_range="Not Applicable"
if length>=3:
    for n in range(int(len(arranged)/2)):
        lower_half.append(arranged[0])
        arranged.remove(arranged[0])
    upper_half=arranged


##Finding lower quartile
    if len(lower_half)%2==1:
        q1=int(lower_half[int(len(lower_half)/2-0.5)])
    else:
        q1=(int(lower_half[int(len(lower_half)/2-1)])+int(lower_half[int(len(lower_half)/2-2)]))/2


##Finding upper quartile
    if len(upper_half)%2==1:
        q3=int(upper_half[int(len(upper_half)/2-0.5)])
    else:
        q3=(int(upper_half[int(len(upper_half)/2-1)])+int(upper_half[int(len(upper_half)/2-2)]))/2


##Finding ranges
    interquartile_range=q3-q1
actual_range=maximum-minimum


##Output
print("Data Analysis:\n\
‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
print("Sum: "+str(total)+"\n\
Average: "+str(mean)+"\n\
Standard Deviation: "+str(Standard_Deviation)+"\n\
Variance: "+str(variance)+"\n\
Range: "+str(actual_range)+"\n\
Minimum value: "+str(minimum)+"\n\
1st Quartile: "+str(q1)+"\n\
Median: "+str(median)+"\n\
3rd Quartile: "+str(q3)+"\n\
Maximum value: "+str(maximum)+"\n\
Interquartile Range: "+str(interquartile_range))

