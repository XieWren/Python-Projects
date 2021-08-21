characters=["!","\"","$","&","'","(",")","+",",","-",".","/","0","1","2","3","4","5","6","7","8","9",":",";","=","?","@","_","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
values=[2793,113,210,17,4803,393,2751,106,2499,77,742,64,16807,4802,1029,196,35,6,11,52,345,2402,346,400,70,149,694,1036,14,10,57,9,2,22,50,5,3,686,56,16,49,8,343,99,350,15,4,7,21,28,98,63,392,51]
total=1
decoded=""

sentence=input("Please enter you morse code (using - and .): ")
for letter in range(len(sentence)):
        if sentence[letter].isspace():
            for n in range(len(values)):
                if values[n]==total:
                    decoded+=characters[n]
                    break
            total=1
        elif sentence[letter]==".":
            total+=1
        elif sentence[letter]=="-":
            total*=7
        elif sentence[letter]=="/":
            decoded+=" "
for n in range(len(values)):
    if values[n]==total:
        decoded+=characters[n]
print("Here is your translation: \n"+decoded)
