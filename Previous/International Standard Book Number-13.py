ISBN=input("Enter the first 12 number of your International Standard Book Number (ISBN): ")
first=0
second=1
total=0
for n in range (6):
    number=ISBN[first:second]
    total=total+int(number)
    first+=1
    second+=1
    number=ISBN[first:second]
    total=total+int(number)*3
    first+=1
    second+=1
remainder=total%10
if remainder==0:
    check_digit=0
else:
    check_digit=10-remainder
print("The 13th number of your ISBN, the check digit, is "+str(check_digit)+".")



"""
Examples:
978-3-16-148410-0
978-1-56619-909-4
978-1-4028-9462-6
"""
