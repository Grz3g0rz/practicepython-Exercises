userNumber = int(input("Your number:"))
if userNumber%4 == 0:
    print("Even, div by 4 mod 0")
elif userNumber%2 == 0:
    print("Even, div by 2 mod 0")
else:
    print("Odd")

check = int(input("Give another number: "))
if userNumber%check == 0:
    print("Divides evenly")
else:
    print("Divides NOT evenly!")