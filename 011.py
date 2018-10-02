"""
Ask the user for a number and determine whether the number is prime or not.
"""
def userNumber(info_text):
    return int(input(info_text))

number = userNumber("Give number: ")

dividors = []
