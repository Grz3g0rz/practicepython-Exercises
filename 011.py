"""
Ask the user for a number and determine whether the number is prime or not.
"""
def userNumber(info_text):
    return int(input(info_text))

def printInfo(x):
    if x==2:
        return(print("Primality"))
    else:
        return(print("Complex"))

number = userNumber("Give number: ")
dividors = [a for a in range(1, number+1) if number%a==0 or number/a==1]
print("Dividors of", number, dividors)
x = len(dividors)

printInfo(x)