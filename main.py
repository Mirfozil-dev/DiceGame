import random

print("This is a Dice simulator!")

y = "y"

while y == "y":
    x = random.randint(1, 6)
    if x == 1:
        print("_________")
        print("|       |")
        print("|   O   |")
        print("|       |")
        print("_________")
    elif x == 2:
        print("_________")
        print("|       |")
        print("|  O O  |")
        print("|       |")
        print("_________")
    elif x == 3:
        print("_________")
        print("|       |")
        print("| O O O |")
        print("|       |")
        print("_________")
    elif x == 4:
        print("_________")
        print("|  O O  |")
        print("|       |")
        print("|  O O  |")
        print("_________")
    elif x == 5:
        print("_________")
        print("|  O O  |")
        print("|   O   |")
        print("|  O O  |")
        print("_________")
    elif x == 6:
        print("_________")
        print("|  O O  |")
        print("|  O O  |")
        print("|  O O  |")
        print("_________")
    y = input("Enter y to roll again, or n to exit: ").lower()
if y == "n":
    print("Goodbye!")
