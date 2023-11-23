
from random import randint
import sys

logo = """

  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|
/ /_\\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_|  
"""
print(logo)



def play():
    number=int(input("enter your guess: "))
    if number == random_number:
        print("You got the number!")
        sys.exit(0)
    elif number < random_number:
        print("Too low!")
    else:
        print("Too high!")

def level(prompt):
    if prompt == "easy":
        for i in range(10):
            play()
    else:
        for i in range(5):
            play()
    print("Game over!")

def printer():
    global random_number
    random_number=randint(1,100)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    prompt=input("Choose a difficulty. Type 'easy' or 'hard' :")
    level(prompt)

printer()





