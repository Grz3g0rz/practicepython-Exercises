"""
Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.

Extras:

1. Add on to the previous program by asking the user for another number and printing out that many copies of the previous message. (Hint: order of operations exists in Python)
2. Print out that many copies of the previous message on separate lines. (Hint: the string "\n is the same as pressing the ENTER button
"""


userName = input("Your name is: ")
userAge = int(input("Your age is: "))
century = (2018-userAge+100)
print(userName, "your hundredth birthday is", century)
counter = int(input("Set counter: "))
print(counter*(userName+"\n"))