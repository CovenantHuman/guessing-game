"""A number-guessing game."""

import random
# Put your code here
print("Howdy!")
name = input("What's your name?")
print(f"Okay, {name}, we're thinking of a number between 1 and 100.")
secret_number = random.randint(1,100)
# for testing coding
print(f"The secret number is {secret_number}")

game_over = False

while not game_over:
    guess = int(input("What do you think the number is?"))
    if guess > secret_number:
        print("Too high! Try again.")
    elif guess < secret_number:
        print("Too low! Try again")
    else:
        game_over = True
        print(f"You got it! The secret number was {secret_number}")