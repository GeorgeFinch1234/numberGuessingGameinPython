import random
import re #regex

def getUserSelection():
    userGuess = input("input a number between 0 and 50 ")
    while(re.fullmatch("^[0-9]*$", userGuess) == None):
        userGuess = input("invalid input, input a number between 0 and 50 ")
    else:
       return int(userGuess)    


hiddenNumber = random.randint(0,50);
userGuessInt = getUserSelection()


while(hiddenNumber != userGuessInt):
    
    whichSide = ""
    if hiddenNumber > userGuessInt:
         whichSide = "lower"
    else:
         whichSide = "higher"
    print(f"That number is {whichSide} than your guess")

    userGuessInt = getUserSelection()
    
else:
     print("Congratulations, you have won")
    



 