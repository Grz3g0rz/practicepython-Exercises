#Create a program that asks the user for a number and then prints out a list of all the divisors of that number.

userNumber = int(input("Input number: "))
x = range(1, userNumber+1)
divisor = []
for element in x:
    if userNumber%element == 0:
        divisor.append(element)

print(divisor)