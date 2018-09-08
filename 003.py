a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [] #extras no. 1
userNumber = int(input("Give me a number 1 - 89: "))
for element in range(0, len(a), 1):
    if a[element] < userNumber:
        b.append(a[element])
for element in range(0, len(b), 1):
    print(b[element])