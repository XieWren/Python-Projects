hexadecimal=["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]
denary=["0","1","2","3","4","5","6","7","8","9"]
binary=["0","1"]
octal=["0","1","2","3","4","5","6","7"]
systems=["denary","binary","hexadecimal","octal"]
error=True
value=0
key=0
new=0
actual=""


print("Number Systems Converter\n\
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾\n\
Choices:\n\
1)Denary (Base 10)\n\
2)Binary (Base 2)\n\
3)Hexadecimal (Base 16)\n\
4)Octal (Base 8)")
original=int(input("Please enter your original number system (1, 2, 3 or 4): "))
switch=int(input("Please enter the number system you want to switch it to (1, 2, 3 or 4): "))
while error:
    error=False
    num=input("Please enter your number: ")
    for n in range(len(num)):
        if not num[n].isspace():
            if original==1 and num[n] not in denary:
                print("Error. Digits in binary form range from 0 to 9 only. Try again.")
                error=True
                break
            elif original==2 and num[n] not in binary:
                print("Error. Numbers in binary form can only have digits '0' and '1'. Try again.")
                error=True
                break
            elif original==3 and num[n] not in hexadecimal:
                print("Error. Digits in hexadecimal values range from 0 to F only. Try again.")
                error=True
                break
            elif original==4 and num[n] not in octal:
                print("Error. Digits in octal values range from 0 to 7 only. Try again.")
                error=True
                break
for n in range(-1,-len(num)-1,-1):
    if not num[n].isspace():
        if original==1:
            value=int(num)
            break
        elif original==2:
            value+=int(num[n])*2**key
        elif original==3:
            if num[n] not in denary:
                for x in range(16):
                    if num[n]==hexadecimal[x]:    
                        value+=(10+int(hexadecimal[x-10]))*16**key
            else:
                value+=int(num[n])*16**key
        else:
            value+=int(num[n])*8**key
        key+=1
if switch==1:
    actual=" "+str(value)
elif switch==2:
    while value!=0:
        power=0
        while value>=2**power:
            power+=1
        value-=2**(power-1)
        new+=1*10**(power-1)
    new=str(new)
    while len(new)%4!=0:
        new="0"+new
    for n in range(0,len(new),4):
        actual+=" "+new[n:n+4]
elif switch==3:
    new=""
    power=1
    while value!=0 or not power==0:
        power-=1
        base=0
        while value>=base*16**power:
            base+=1
            if base==17:
                power+=1
                base=0
        value-=(base-1)*16**power
        new+=hexadecimal[base-1]
    while len(new)%2!=0:
        new="0"+new
    for n in range(0,len(new),2):
        actual+=" "+new[n:n+2]
else:
    while value!=0:
        power=0
        base=0
        while base*8**power<=value:
            base+=1
            if base==9:
                power+=1
                base=0
        value-=(base-1)*8**power
        new+=(base-1)*10**power
    new=str(new)
    while len(new)%3!=0:
        new="0"+new
    for n in range(0,len(new),3):
        actual+=" "+new[n:n+3]
print("Number in "+str(systems[switch-1])+" form is"+actual+".")
    
##"""Perpetual Testing Initiative:""" (bROkeN)
##original=0
##value=original
##key=0
##new=""
##actual=""
##power=1
##while True:
##    ##Part 1 (Den --> Hex)
##    value=original
##    key=0
##    new=""
##    actual=""
##    power=1
##    while value!=0 or not power==0:
##        power-=1
##        base=0
##        while value>=base*16**power:
##            base+=1
##            if base==17:
##                power+=1
##                base=0
##        value-=(base-1)*16**power
##        new+=hexadecimal[base-1]
##    while len(new)%2!=0:
##        new="0"+new
##    for n in range(0,len(new),2):
##        actual+=new[n:n+2]+" "
##    ##Part 2 (Hex --> Den)
##    num=actual
##    for n in range(-1,-len(num)-1,-1):
##        if not num[n].isspace():
##            if num[n] not in denary:
##                for x in range(16):
##                    if num[n]==hexadecimal[x]:    
##                        value+=(10+int(hexadecimal[x-10]))*16**key
##            else:
##                value+=int(num[n])*16**key
##        key+=1
##    ##Part 3 (Check)
##    if value!=original:
##        print(value)
##        print(original)
##        break
##    ##Part 4 (Reset)
##    original+=1
##    value=original
##    key=0
##    new=""
##    actual=""
##    power=1
