# Fun Fact: Encrypting/Decrypting Beaufort Classic with
# the same key and ciphertext gives the same output.
t_list=[]
print("""
Select Cipher:
‾‾‾‾‾‾‾‾‾‾‾‾‾‾
1.Caesar Shift
2.Atbash Cipher
3.A1Z26 Cipher
4.Vigenère Square
5.Beaufort Classic (Key-Txt)
6.Beaufort Cipher (German Variant: Txt-Key)""")
#7.Autoclave Cipher (W.I.P)""")
cipher=input("Select a number (1-4): ")
while not cipher.isdigit() or not 1<=int(cipher)<=7:
    print("Error.")
    cipher=input("Select a number (1-4): ")
while True:
    code=input("Encode/Decode: ").upper()
    if code!="ENCODE" and code!="DECODE":
        print("Error. Enter only encode or decode.")
        continue
    break
while True:
    text=input("Enter text to be encoded/decoded: ")
    if text.isspace():
        print("Error. Input must not be left blanked.")
        continue
    break


if cipher=='1':
    for n in range(len(text)):
        t_list.append(text[n])
    shift=input("Enter shift (1-25): ")
    while not shift.isdigit() and not 1<=int(shift)<=25:
        print("Error.")
        shift=input("Enter shift (1-25): ")
    shift=int(shift)
    if code=="DECODE":
        shift*=-1
    for n in range(len(t_list)):
        if 97<=ord(t_list[n])<=122:
            if ord(t_list[n])+shift>122:
                t_list[n]=chr(ord(t_list[n])+shift-26)
            elif ord(t_list[n])+shift<97:
                t_list[n]=chr(ord(t_list[n])+shift+26)
            else:
                t_list[n]=chr(ord(t_list[n])+shift)
        elif 65<=ord(t_list[n])<=90:
            if ord(t_list[n])+shift>90:
                t_list[n]=chr(ord(t_list[n])+shift-26)
            elif ord(t_list[n])+shift<65:
                t_list[n]=chr(ord(t_list[n])+shift+26)
            else:
                t_list[n]=chr(ord(t_list[n])+shift)
    print("Result: ","".join(t_list))
                

elif cipher=='2':
    for n in range(len(text)):
        t_list.append(text[n])
    for n in range(len(t_list)):
        if 97<=ord(t_list[n])<=122:
            t_list[n]=chr(27-(ord(t_list[n])-96)+96)
        elif 65<=ord(t_list[n])<=90:
            t_list[n]=chr(27-(ord(t_list[n])-64)+64)
    print("Result: ","".join(t_list))            
        

elif cipher=='3':
    for n in range(len(text)):
        t_list.append(text[n])
    result=""
    if code=="ENCODE":
        n=0
        while n<len(t_list):
            if t_list[n].isalpha() and 97<=ord(t_list[n])<=122:
                result+=str(ord(t_list[n])-96)
                if t_list[n+1].isalpha():
                    result+="-"
            elif t_list[n].isalpha() and 65<=ord(t_list[n])<=90:
                result+=str(ord(t_list[n])-64)
                if t_list[n+1].isalpha():
                    result+="-"
            else:
                result+=t_list[n]
            n+=1
    elif code=="DECODE":
        for n in range(len(text)):
            if not text[n].isdigit() and text[n+1].isdigit() and text[n-1].isdigit() and not text[n].isspace():
                seperate=text[n]
                break
        n=0
        while n<len(t_list):
            if t_list[n].isdigit():
                if t_list[n+1].isdigit():
                    result+=chr(int(t_list[n]+t_list[n+1])+64)
                    n+=1
                else:
                    result+=chr(int(t_list[n])+64)
            elif t_list[n]!=seperate:
                result+=t_list[n]
            n+=1
    print("Result: ",result)

                
elif cipher=='4' or cipher=="7":
    result=""
    letter=-1
    key=input("Enter key: ").upper()
    while not key.isalpha():
        print("Error. Text only.")
        key=input("Enter key: ").upper()
    if cipher=="7" and code=="ENCODE":
        key+=text.upper()
    for n in range(len(text)):
        t_list.append(text[n])
    if code=="ENCODE":
        for n in t_list:
            if 65<=ord(n)<=90:
                letter+=1
                n=ord(n)
                if n+ord(key[letter%len(key)])>155: #>=65+65+26
                    n-=26
                result+=chr(n+ord(key[letter%len(key)])-65)
            elif 97<=ord(n)<=122:
                letter+=1
                n=ord(n)
                if n+ord(key[letter%len(key)])>187: #>=97+65+26
                    n-=26
                result+=chr(n+ord(key[letter%len(key)])-65)
            else:
                result+=n
        print("Result: ",result)
    elif code=="DECODE":
        for n in t_list:
            if 65<=ord(n)<=90:
                letter+=1
                n=ord(n)
                shift=ord(key[letter%len(key)])-65
                if n-shift<65: #
                    n+=26
                result+=chr(n-shift)
                if cipher=="7":
                    key+=chr(n-shift)
            elif 97<=ord(n)<=122:
                letter+=1
                n=ord(n)
                shift=ord(key[letter%len(key)])-65
                if n-shift<97: #
                    n+=26
                result+=chr(n-shift)
            else:
                result+=n
        print("Result: ",result)

elif cipher=="5"or cipher=="6":
    result=""
    letter=-1
    key=input("Enter key: ").upper()
    while not key.isalpha():
        print("Error. Text only.")
        key=input("Enter key: ").upper()
    for n in range(len(text)):
        t_list.append(text[n])
    if code=="ENCODE":
        for n in t_list:
            if 65<=ord(n)<=90:
                letter+=1
                n=ord(n)-65
                shift=ord(key[letter%len(key)])-65
                if cipher=="5":
                    if shift-n<0:
                        shift+=26
                    result+=chr(shift-n+65)
                else:
                    if n-shift<0:
                        n+=26
                    result+=chr(n-shift+65)
            elif 97<=ord(n)<=122:
                letter+=1
                n=ord(n)-97  #0≤n≤25
                shift=ord(key[letter%len(key)])-65  #0≤shift≤25
                if cipher=="5":
                    while shift-n<0:  #-25≤shift-n≤25
                        shift+=26
                    result+=chr(shift-n+97)  #0≤shift-n≤25
                else:
                    if n-shift<0:
                        n+=26
                    result+=chr(n-shift+97)
            else:
                result+=n
    if code=="DECODE":
        for n in t_list:
            if 65<=ord(n)<=90:
                letter+=1
                n=ord(n)-65
                shift=ord(key[letter%len(key)])-65
                if cipher=="5":
                    if shift-n<0:
                        shift+=26
                    result+=chr(shift-n+65)
                else:
                    if n+shift>25: #
                        n-=26
                    result+=chr(n+shift+65)
            elif 97<=ord(n)<=122:
                letter+=1
                n=ord(n)-97
                shift=ord(key[letter%len(key)])-65
                if cipher=="5":
                    if shift-n<0:
                        shift+=26
                    result+=chr(shift-n+97)
                else:
                    if n+shift>25: #
                        n-=26
                    result+=chr(n+shift+97)
            else:
                result+=n
    print("Result: ",result)
