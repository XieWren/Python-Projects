first=0
second=1
multiply=10
total=0

ISBN=input("Enter first 9 digits of your International Standard Book Number (ISBN): ")

for n in range(9):
    digit=ISBN[first:second]
    total=total+int(digit)*multiply
    first+=1
    second+=1
    multiply-=1
remainder=total%11
if remainder==0:
    check_digit=0
else:
    check_digit=11-remainder
    if check_digit==10:
        check_digit="X"
print("The last digit of your International Standard Book Number (ISBN), the check digit, is "+str(check_digit)+".")



"""
Examples:
99921-58-10-7
9971-5-0210-0
960-425-059-0
80-902734-1-6
85-359-0277-5
1-84356-028-3
0-684-84328-5
0-8044-2957-X
0-85131-041-9
93-86954-21-4
0-943396-04-2
0-9752298-0-X
"""


"""
Simpler Format:
total=0
remainder=0
ISBN=input("Enter first 9 digits of your International Standard Book Number (ISBN): ")

for n in range(9):
    total=total+int(ISBN[n])*(10-n)
remainder=total%11
if remainder==0:
    check_digit=0
else:
    check_digit=11-remainder
    if check_digit==10:
        check_digit="X"
print("The last digit of your International Standard Book Number (ISBN), the check digit, is "+str(check_digit)+".")
