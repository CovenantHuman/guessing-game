"""A number-guessing game."""

import random
tries = 0
 
# ----- welcome / user input --------
name = input("Howdy! What's your name? ")
print(f"Okay, {name}, we're thinking of a number between 1 and 100.")
secret_number = random.randint(1,100)
# for testing coding
print(f"The secret number is {secret_number}")

game_over = False

while not game_over:
    guess = input("What do you think the number is? ")
    tries += 1
    try:
        guess = int(guess)
    except ValueError:
        print("You are ridiculous. Enter an integer.")
        continue
        
    if guess >= 101 or guess <= 0:
            print("You fool. Play the game correctly")
    else: 
        if guess > secret_number:
            print("Too high! Try again.")
        elif guess < secret_number:
            print("Too low! Try again")
        else:
            game_over = True
            print(f"You got it! The secret number was {secret_number}. You got it in {tries} guesses")
                


        
