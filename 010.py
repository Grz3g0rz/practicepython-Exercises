omly generate two lists to test this
"""
#nowsza wersja pliku po zmianach
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