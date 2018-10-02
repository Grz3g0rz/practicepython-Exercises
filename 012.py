import random
elementList = random.sample(range(1, 20), 5)
def select(elementList):
    firstLast = [elementList[0], elementList[-1]]
    print(elementList)
    print(firstLast)

select(elementList)