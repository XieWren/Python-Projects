NRIC=input("Enter the first eight digits of your NRIC: ")
total=0
multiply=7
check_sum=0
number=NRIC[1:2]
total+=int(number)*2
for position in range (2,8):
    number=NRIC[position:position+1]
    total+=int(number)*multiply
    multiply-=1
if NRIC[:1]=="T" or NRIC[:1]=="G":
    total+=4
remainder=total%11
##if NRIC[:1]=="S" or NRIC[:1]=="T":
##    if remainder==0:
##        check_sum='J'
##    elif remainder==1:
##        check_sum='Z'
##    elif remainder==2:
##        check_sum='I'
##    elif remainder==3:
##        check_sum='H'
##    elif remainder==4:
##        check_sum='G'
##    elif remainder==5:
##        check_sum='F'
##    elif remainder==6:
##        check_sum='E'
##    elif remainder==7:
##        check_sum='D'
##    elif remainder==8:
##        check_sum='C'
##    elif remainder==9:
##        check_sum=B''
##    elif remainder==10:
##        check_sum='A'
##elif NRIC[:1]=="F" or NRIC[:1]=="G":
##    if remainder==0:
##        check_sum='X'
##    elif remainder==1:
##        check_sum='W'
##    elif remainder==2:
##        check_sum='U'
##    elif remainder==3:
##        check_sum='T'
##    elif remainder==4:
##        check_sum='R'
##    elif remainder==5:
##        check_sum='Q'
##    elif remainder==6:
##        check_sum='P'
##    elif remainder==7:
##        check_sum='N'
##    elif remainder==8:
##        check_sum='M'
##    elif remainder==9:
##        check_sum='L'
##    elif remainder==10:
##        check_sum='K'
if NRIC[:1]=='S' or NRIC[:1]=='T':
    last='JZIHGFEDCBA'
    for sequence in range (0,11):
        if sequence != remainder:
            continue
        else:
            check_sum=last[sequence:sequence+1]
elif NRIC[:1]=='F' or NRIC[:1]=='G':
    last='XWUTRQPNMLK'
    for sequence in range (0,11):
        if sequence != remainder:
            continue
        else:
            check_sum=last[sequence:sequence+1]
print("The last digit of your NRIC is "+str(check_sum)+".")

"""
If the IC starts with S or T: 0=J, 1=Z, 2=I, 3=H, 4=G, 5=F, 6=E, 7=D, 8=C, 9=B, 10=A
If the IC starts with F or G: 0=X, 1=W, 2=U, 3=T, 4=R, 5=Q, 6=P, 7=N, 8=M, 9=L, 10=K
"""
