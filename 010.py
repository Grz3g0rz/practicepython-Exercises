"""
write a program that returns a list that contains only the elements that are common between the lists (without duplicates).
Make sure your program works on two lists of different sizes. Write this in one line of Python using at least one list comprehension.

Extra:

Randomly generate two lists to test this
"""

import random
firstList = []
secondList = []
overlap = []
for x in range (0, 10, 1):
    num = random.randint(0, 10)
    firstList.append(num)
for x in range (0, 15, 1):
    num = random.randint(2, 12)
    secondList.append(num)

overlap = [a for a in firstList if a in secondList and not overlap]

print(firstList)
print(secondList)
print(overlap)