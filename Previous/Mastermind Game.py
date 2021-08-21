colours=["red", "green", "blue", "yellow", "white", "black"]   #Initialise colours
print("Possible colours are red, green, blue, yellow, white and black.")   #Tell user possible colours.
while True:#Player 1 decides on pattern combination.
    answers=input("Player 1, please enter 4 colours in any order, separated by a space: ")
    answers=answers.lower()
    answers=answers.split()#Colours separated in a group
    correct=True
    for answer in answers:#Check if colours entered are in possible selection.
        if answer not in colours:
            correct=False
            print("You can only choose the colours red, blue, green, yellow, white and black. Please try again.")
    if not correct:
        continue
    if len(answers)!=4:#Check no. of colours
        print("Need only 4 colours. Please try again.")
        continue
    if correct:
        print("Colours have been accepted.")#When colours meet the given criteria.
        break
win=False#Initialise
for chances_left in range(10,0,-1):#Player 2 guesses pattern combination.
    print("Player 2, you have "+str(chances_left)+" chance(s) to guess the colours and order given by player 1.")
    correct_colour=0#Shows no. of balls with correct colour in the guess.
    correct_position=0#Shows no. of balls of the correct colour in the correct position in the guess.
    guesses=input("Please enter 4 colours in any order, separated by a space: ")
    guesses=guesses.lower()
    guesses=guesses.split()#Colours guessed separated in a group
    answers_for_testing=[]#Creating alternative variable same as variable 'answers' that shows correct combination.
    for answer in answers:#Answers_for_testing=answers will not work as the two variables will be connected to a single value; when one changes, the other does as well.
        answers_for_testing.append(answer)
    for guess in guesses:#Test for no. of balls with correct colour in guess. This set-up allows for program to detect repeated colours in both guesses and the answer without possible errors.
        if guess in answers_for_testing:
            correct_colour+=1
            answers_for_testing.remove(guess)#Any change in the value in variable answers_for_testing will not affect_ the value in variable answers.
    for position in range(4):#Test for no. of balls of the correct colour in the correct position in the guess.
        if guesses[position]==answers[position]:
            correct_position+=1
    if correct_position==4:
        print("Congratulations, you have found the answer!")#If player 2 guesses colour combination correctly.
        win=True
        break
    else:
        print("Number of colours that are in answer: "+str(correct_colour)+"\nNumber of colours that are in the correct position: "+str(correct_position))#Shows how close the user is to getting the answer (No. of balls in correct position and No.of balls in pattern with correct colour.)
if not win:
    print("You have lost the game. The correct combination is "+", ".join(answers)+".")#If player 2 fails to guess colour combination + shows the answer for player 2 to see how close/far they were.
