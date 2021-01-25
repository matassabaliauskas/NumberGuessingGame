# this game asks user to guess the number from 1 to 10
import random

randomval = random.randint(1,10)

guess = int(input("Guess the number from 1 to 10: "))

if guess == randomval:
    print("Congratulations! You won!")
    print("The correct number is: ", randomval)
else:
    print("You lose!")
    print("The correct number is: ", randomval)