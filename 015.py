userWords = ""
def userPhrase():
    userWords = input("Your phrase: ")
    print(userWords)
    print(userWords[::-1])

userPhrase()