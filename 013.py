"""
Write a program that asks the user how many Fibonnaci numbers to generate and then generates them.
Take this opportunity to think about how you can use functions.
Make sure to ask the user to enter the number of numbers in the sequence to generate.
1, 1, 2, 3, 5, 8...
"""
numbers = int(input("How many numbers: "))
lim = [1, 1]

def fibNumbers(numbers):
    a = 0
    b = a+1
    c = a+1
    for i in range (0, numbers, 1):
        new = lim[a] + lim[b]
        lim.append(new)
        numbers-=1
        a+=1
        b+=1
    print(lim)

fibNumbers(numbers)