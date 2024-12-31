from ast import Global
from random import randint as ri
import random
choice = ""
randomDigits = []
tries = 0
valid = True
guess = ""
print("High Score (Avg Num. Tries) = ", ri(1, 20))
def easy():
    guess = []
    global tries
    tries = 0
    correct = 0
    striDigits = "0000"
    for i in range(4):
        digit = ri(1, 9)
        randomDigits.append(digit)
    print(randomDigits)
    print(striDigits)
    while guess != randomDigits:
        guess.clear()
        for i in range(4):
            guess.append(int(input("Guess the 4 digit number. One Number at a time.")))
            print(guess)
            print(i)
        tries += 1
        for i in range(4):
            if guess[i] == randomDigits[i]:
                correct +=1
                print(correct)
        print(f"You got {correct} right. Out of 4.")
    tries = tries
    return tries

def hard():
    guess = []
    global tries
    tries = 0
    correct = 0
    striDigits = "00000"
    for i in range(5):
        digit = ri(1, 9)
        randomDigits.append(digit)
    print(randomDigits)
    print(striDigits)
    while guess != randomDigits:
        guess.clear()
        for i in range(5):
            guess.append(int(input("Guess the 5 digit number. One Number at a time.")))
            print(guess)
            print(i)
        tries += 1
        if guess != randomDigits:
            print("Incorrect, Try agin.")
    tries = tries
    return tries

while valid == True:
    choice = input("Easy or Hard Mode?")
    if choice.lower() == "easy":
        print("Guesses = ",easy())
        valid = False
    elif choice.lower() == "hard":
        print("Guesses = ",hard())
        valid = False
    else:
        print("Not Valid")
        valid = True
print("\nCorrect, Well done.\n\n")
name = input("Enter name: ")
scores = name, tries
print(scores)