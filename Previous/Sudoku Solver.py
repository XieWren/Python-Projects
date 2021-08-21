"""
Algorithm
‾‾‾‾‾‾‾‾‾
Starting with an incomplete board:

 1)Find some empty space
 2)Attempt to place the digits 1-9 in that space
 3)Check if that digit is valid in the current spot based on the current board
   a. If the digit is valid, recursively attempt to fill the board using steps 1-3.
   b. If it is not valid, reset the square you just filled and go back to the previous step.
 4)Once the board is full by the definition of this algorithm we have found a solution.
"""
def start():
    while True:
        global sudoku
        sudoku=str(input("Enter sudoku values (or enter 'guide' to understand the format of entering): "))
        if sudoku=='guide':
            print("\n\
                Given the following input:\n\
                \n\
               '004006079000000602056092300\n\
                078061030509000406020540890\n\
                007410920105000000840600100'\n\
                \n\
         It is represented in the following format:\n\
                \n\
                 0 0 4 ┃ 0 0 6 ┃ 0 7 9\n\
                 0 0 0 ┃ 0 0 0 ┃ 6 0 2\n\
                 0 5 6 ┃ 0 9 2 ┃ 3 0 0\n\
                ━━━━━━━╋━━━━━━━╋━━━━━━━\n\
                 0 7 8 ┃ 0 6 1 ┃ 0 3 0\n\
                 5 0 9 ┃ 0 0 0 ┃ 4 0 6\n\
                 0 2 0 ┃ 5 4 0 ┃ 8 9 0\n\
                ━━━━━━━╋━━━━━━━╋━━━━━━━\n\
                 0 0 7 ┃ 4 1 0 ┃ 9 2 0\n\
                 1 0 5 ┃ 0 0 0 ┃ 0 0 0\n\
                 8 4 0 ┃ 6 0 0 ┃ 1 0 0\n\
                \n\
         Where '0' represents an unknown character\n")
            continue
        if not sudoku.isdigit():
            print("Error. Numbers only")
            continue
        elif float(sudoku)%1!=0:
            print("Error. Numbers only")
            continue
        elif len(sudoku)!=81:
            print("Error. Incorrect number of items.")
            continue
        display="              "
        print("The following is a preview of what you have entered.")
        for n in range(81):
            display+=" "
            if n%3==0 and display!="               ":
                display+="┃ "
            display+=sudoku[n]
            if n%9==8:
                print(display)
                display="              "
            if n%27==26 and n<80:
                print("              ━━━━━━━╋━━━━━━━╋━━━━━━━")
        confirm=input("Please confirm whether your input is correct. (Y/N): ")
        if confirm=="Y":
            global s_l
            s_l=[0]*81
            for n in range(81):
                if sudoku[n]=="0":
                    s_l[n]=int(sudoku[n])
                else:
                    s_l[n]=sudoku[n]
            break
        if confirm=="N":
            continue

def rd_3s(r_c):
    if r_c < 3:
        r_c=0
    elif r_c < 6:
        r_c=3
    else:
        r_c=6
    return r_c

def row():
    global rowL,n,s_l,reset
    rowL=[]
    for check in range(n//9*9,n//9*9+9):
        rowL.append(s_l[check])
    #print(s_l[n])
    #print(rowL)
    rowL.remove(s_l[n])
    if str(s_l[n]) in rowL or s_l[n] in rowL:
        reset=True
def column():
    global columnL,n,s_l,reset
    columnL=[]
    for check in range(n%9,81,9):
        columnL.append(s_l[check])
    #print(columnL)
    columnL.remove(s_l[n])
    if str(s_l[n]) in columnL or s_l[n] in columnL:
        reset=True
def box(): #!!!
    global boxL,n,s_l,reset
##  row=n//9
##  column=n%9
    r_Grp=rd_3s(n//9)
    c_Grp=rd_3s(n%9)
    boxL=[]
    for r_add in range(3):
        for c_add in range(3): 
            boxL.append(s_l[(r_add+r_Grp)*9+c_add+c_Grp])
    #print(s_l)
    #print(n)
    #print(boxL)
    boxL.remove(s_l[n])
    if str(s_l[n]) in boxL or s_l[n] in boxL:
        reset=True
#   for n in range(81):
#	print('Row:',n//9,'Column:',n%9,'\nR_Grp:',n//9//3,'C_Grp:',n%9//3,'\nn =',n)

def calculation():
    global s_l,n,reset,broke
    n=0
    reset=False
    broke=False
    while n<81:
        while type(s_l[n])!=int and n<80:
            n+=1
        if s_l[n]==0:
            s_l[n]+=1
            #print(s_l[n],'plus (start)')
        row()
        #print('rc')
        if not reset:
            column()
            #print('cc')
        if not reset:
            box()
            #print('bc')
        if reset:
            if s_l[n]>=9:
                s_l[n]=0
                n-=1
                #print('reset previous',n)
                while True:
                    if type(s_l[n])!=int:
                        n-=1
                    elif s_l[n]>=9:
                        s_l[n]=0
                        n-=1
                    else:
                        break
            s_l[n]+=1
            #print(s_l[n],'plus')
            reset=False
            #print('reset')
            if n<0:
                broke=True
                break
        else:
            n+=1
            #print(n,'next')
def result():
    global s_l, broke
    if broke:
        print("This puzzle appears to be unsolvable. Please ensure your values have been input correctly.")
        main()
    else:
        print("The above sudoku puzzle has the following answer: ")
        sudoku=""
        s_l.reverse()
        while len(s_l)!=0:
            sudoku+=str(s_l.pop())
        display="              "
        for n in range(81):
            display+=" "
            if n%3==0 and display!="               ":
                display+="┃ "
            display+=sudoku[n]
            if n%9==8:
                print(display)
                display="              "
            if n%27==26 and n<80:
                print("              ━━━━━━━╋━━━━━━━╋━━━━━━━")
    
def main():
    start()
    calculation()
    result()

if __name__=="__main__":
    main()


###Examples
#Puzzle:   000000000000003085001020000000507000004000100090000000500000073002010000000040009
#Solution: 987654321246173985351928746128537694634892157795461832519286473472319568863745219
#Note:     Meant to work against brute-force alghorithms like this one. Might have more solutions.
#Sauce:    https://en.wikipedia.org/wiki/Sudoku_solving_algorithms

#Puzzle:   004006079000000602056092300078061030509000406020540890007410920105000000840600100
#Solution: 284136579913754682756892341478961235539287416621543897367415928195328764842679153
#Note:     The original puzzle that started the whole thing.
#Sauce:    Unfortunately lost =(

#Puzzle:   200900000000000060000001000502600407000004100000098023000003080005010000007000000
#Solution: N.A.
#Note:     An impossible puzzle.
#Sauce:    https://www.reddit.com/r/sudoku/comments/7q76ay/friend_tells_me_that_this_is_unsolvable_sudoku/
