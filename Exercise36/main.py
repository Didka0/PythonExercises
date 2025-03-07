import random

houses = [
    "Gryffindor",
    "Hufflepuff",
    "Ravenclow",
    "Slytherin"
]

answer = input("Want to use Sorting Hat? ").lower()
if answer == "yes":
    name = input("What is your name? ").capitalize()
    pass
elif answer == "no":
    print("See you later!")
    exit()
else:
    print("Invalid input")
    exit()
house = random.choice(houses)
print("Congratulations,",name,".", sep='', end='')
print("Your house is: ", house)