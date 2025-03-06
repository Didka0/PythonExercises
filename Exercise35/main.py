import cowsay
import random

cowsay.cow("Hi, wanna play? ")
answer = input("Do you? ")

if answer == "no":
    cowsay.cow("Oh, okay, bye !")
elif answer != "yes":
    cowsay.cow("Invalid command, exiting")
    exit()

while True:
    cowsay.cow("Guess my number from 0 to 3")
    user_choice = int(input("So..? Choose a number or type exit  "))
    if user_choice == "exit":
        break
    cow_choice = random.randrange(4)
    print("My number is", cow_choice)
    if user_choice == 0 and cow_choice == 0:
        cowsay.cow("You won! 😭")
    elif user_choice == 1 and cow_choice == 1:
        cowsay.cow("You won! 😭")
    elif user_choice == 2 and cow_choice == 2:
        cowsay.cow("You won! 😭")
    elif user_choice == 3 and cow_choice == 3:
        cowsay.cow("You won! 😭")
    else:
        cowsay.cow("I won! 🤭")

    
