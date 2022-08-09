"""A number-guessing game."""

import random

best_score = None
play_again = True
name = input("Howdy! What's your name? ")
user_min = int(input("Give us your lowest number, human scum"))
user_max = int(input("What is your highest number, feeble mortal"))


while play_again: 
    tries = 0
    print(f"Okay, {name}, we're thinking of a number between {user_min} and {user_max}. You get 7 guesses.")
    secret_number = random.randint(user_min,user_max)
    # for testing coding
    print(f"The secret number is {secret_number}")

    game_over = False

    while not game_over:
        if tries > 6:
            print("You took too many guesses!")
            break
        else:
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
                    if best_score == None or best_score > tries:
                        best_score = tries
                    print(f"You got it! The secret number was {secret_number}. You got it in {tries} guesses")
                    print(f"The current best score is: {best_score}")

              
                
    restart = input("Would you like to play again? Y/N ").lower()
    if restart == "n":
        play_again = False
        print("Thanks for playing!")
        
