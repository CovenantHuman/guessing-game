"""A number-guessing game."""

import random
tries = 0
 
# ----- welcome / user input --------
print("Howdy!")
name = input("What's your name? ")
print(f"Okay, {name}, we're thinking of a number between 1 and 100.")
secret_number = random.randint(1,100)
# for testing coding
print(f"The secret number is {secret_number}")

game_over = False

def check_guess(guess, secret_number):
    global tries
    if guess > secret_number:
        tries += 1
        print("Too high! Try again.")
    elif guess < secret_number:
        tries += 1
        print("Too low! Try again")
    else:
        game_over = True
        tries += 1
        print(f"You got it! The secret number was {secret_number}. You got it in {tries} guesses")
        return game_over


while not game_over:
    try:
        guess = int(input("What do you think the number is? "))
        if guess >= 101 or guess <= 0:
            tries += 1
            print("You fool. Play the game correctly")
        else: 
            game_over = check_guess(guess, secret_number)
    except ValueError:
        tries += 1
        print("You are ridiculous. Enter an integer.")

        
