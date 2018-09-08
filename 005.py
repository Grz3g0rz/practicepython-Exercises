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