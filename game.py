"""A number-guessing game."""

import random

best_score = None
play_again = True
name = input("Howdy! What's your name? ")
user_min = int(input("Give us your lowest number, human scum: "))
user_max = int(input("What is your highest number, feeble mortal: "))



while play_again: 
    game_mode = int(input("Do you want to guess, or should the computer?\n 1 for you\n 2 for computer: "))
 
    if game_mode == 1:
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

    # game mode where computer attempts to guess secret number              
    elif game_mode == 2:
        print(f"Pick a number between {user_min} and {user_max}.")
        print("The computer will take guesses.")
        print("If the computer guesses too high, enter too high.")
        print("If the computer guesses too low, enter too low.")
        print("If the computer guess right, enter you won.")
        comp_win = False
        low = user_min
        high = user_max + 1
        while not comp_win:
            computer_guess = int((high + low)/ 2)
            print(computer_guess)
            user_response = input("How did I guess? ")
            if user_response.lower() == "too high":
                high = computer_guess
            elif user_response.lower() == "too low":
                low = computer_guess
            else:
                print("The computer has bested you")
                break


    else: 
        print("I really wish you could read.") 


    restart = input("Would you like to play again? Y/N ").lower()
    if restart == "n":
        play_again = False
        print("Thanks for playing!")
        
