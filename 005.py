"""
take two lists, say for example these two:

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
and write a program that returns a list that contains only the elements that are common between the lists (without duplicates).
Make sure your program works on two lists of different sizes.

Extras:

Randomly generate two lists to test this
Write this in one line of Python (don’t worry if you can’t figure this out at this point - we’ll get to it soon)
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

for x in range (0, len(secondList), 1):
    if (secondList[x] not in firstList) and (secondList[x] not in overlap):
        overlap.append(secondList[x])

print(firstList)
print(secondList)
print(overlap)