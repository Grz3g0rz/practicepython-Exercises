#Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a string that reads the same forwards and backwards.)

userWord = input("Podaj słowo: ")
string = userWord[0: len(userWord)]
oposite = userWord[::-1]
if string == oposite:
    print("Palindrom")
else:
    print("nie")