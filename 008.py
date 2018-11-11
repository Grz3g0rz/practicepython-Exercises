"""
Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input),
compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)
"""
import random
#0 = rock
#1 = paper
#2 = scisors

while playerChose != "q":
    playerChose = input("(r)ock, (p)aper, (s)cisors, (q)uit: ")
    compChose = random.randint(0, 2)
    if playerChose == "r" and compChose == 1:
        print("User won")
    elif playerChose == "p" and compChose == 2:
        print("User won")
    elif playerChose == "s" and compChose ==  0:
        print("User won")
    elif playerChose == compChose:
        print("Remis")
    else:
        print("Comp won")