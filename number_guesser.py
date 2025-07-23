#Task 2:  Number Guesser
'''Create a number guessing game where the program generates a random number between a specified range, 
and the user tries to guess it. Provide feedback to the user if their guess is too high or too low.'''

import random

def number_guesser():
    starting_number = int(input("staring_number:"))
    ending_number = int(input("ending_number:"))

    if starting_number == ending_number:
        print("Invalid range. Staring number and ending number must not be equal.")
        return
    elif starting_number >= ending_number:
        print("Invalid range. Starting number must be less than ending number.")
        return

    guess_the_number = random.randint(starting_number, ending_number)
    print(f"Guess the number between {starting_number} and {ending_number}!")


    while True:
        try:
            guess = int(input("Your guess: "))

            if guess < 1 or guess > 100:
                print("Please guess a number within 1 and 100.")
            elif guess < guess_the_number:
                print("Too low")
            elif guess > guess_the_number:
                print("Too high")
            else:
                print(f"{guess_the_number} is Correct! You guessed it")
                break

        except ValueError:
            print("Invalid input. Please enter an integer.")


number_guesser()

 