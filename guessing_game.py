#Task 1:  Guessing Game
'''Write a Python program that generates a random number between 1 and 100. The user should then try to guess the number.
 The program should provide hints such as"too high" or "too low" until the correct number is guessed.'''
 
import random

def number_guessing_game():
    guess_the_number = random.randint(1, 100)
    print("Guess the number between 1 and 100!")

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


number_guessing_game()
