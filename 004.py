userNumber = int(input("Input number: "))
x = range(1, userNumber+1)
divisor = []
for element in x:
    if userNumber%element == 0:
        divisor.append(element)

print(divisor)