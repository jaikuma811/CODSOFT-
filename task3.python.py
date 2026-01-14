import random
import string

while True:
    print("\nPassword Complexity Levels")
    print("1. Simple (Alphabets only)")
    print("2. Medium (Alphabets + Numbers)")
    print("3. Strong (Alphabets + Numbers + Symbols)")
    print("4. Exit")

    cho = int(input("Enter complexity level: "))

    if cho == 4:
        print("Program terminated.")
        break

    if cho not in [1, 2, 3]:
        print("Invalid choice! Try again.")
        continue

    length = int(input("Enter password length (minimum 6): "))

    if length < 6:
        print("Password must contain at least 6 characters.")
        continue

    if cho == 1:
        cha = string.ascii_letters

    elif cho == 2:
        cha = string.ascii_letters + string.digits

    else:
        cha = string.ascii_letters + string.digits + string.punctuation

    # generating password
    pswd = ""
    for i in range(length):
        pswd += random.choice(cha)

    print("Generated Password:", pswd)
