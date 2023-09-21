from random import random

guessed_number = random.randomint(1, 10)
guess = int(input("Enter your guess number between 1 and 10"))
while guessed_number != guess:
    guess = int(input("Enter your guess number between 1 and 10"))
    if guessed_number == guess:
     print("You Won!")