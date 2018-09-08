"""
Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. Hint: how does an even / odd number react differently when divided by 2?

Extras:

1. If the number is a multiple of 4, print out a different message.
2. Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). If check divides evenly into num, tell that to the user.
        If not, print a different appropriate message.
"""


userNumber = int(input("Your number:"))
if userNumber%4 == 0:
    print("Even, div by 4 mod 0")
elif userNumber%2 == 0:
    print("Even, div by 2 mod 0")
else:
    print("Odd")

check = int(input("Give another number: "))
if userNumber%check == 0:
    print("Divides evenly")
else:
    print("Divides NOT evenly!")