
import random

hiddenNumber = random.randint(0,50);
print(hiddenNumber)
userGuess = int(input("input a number between 0 and 50 "))

while(hiddenNumber != userGuess):
    
    whichSide = ""
    if hiddenNumber > userGuess:
         whichSide = "lower"
    else:
         whichSide = "higher"
    print(f"that number is {whichSide} than guess")

    userGuess = int(input("input a number between 0 and 50 "))
    
else:
     print("Congradulations, you have won")
    
