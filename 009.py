"""
Generate a random number between 1 and 9 (including 1 and 9).
Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right.
(Hint: remember to use the user input lessons from the very first exercise)

Extras:

Keep the game going until the user types “exit”
Keep track of how many guesses the user has taken, and when the game ends, print this out.
"""
import random
userGuess = None
secretNumber = random.randint(1, 9)
counter = 0
while userGuess != "exit":
    userGuess = input("Guess number: ")
    if userGuess != "exit":
        userGuess = int(userGuess)
        counter +=1
        if userGuess == secretNumber:
            print("Success in", counter, "shots")
            break
        else:
            print("Try again")