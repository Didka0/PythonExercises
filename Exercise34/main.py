import random


while True:
    number = random.randint (1,10)
    print("Your randon number is: ", number)


    user_choice = input("Again? ")
    if user_choice == "yes":
        pass
    elif user_choice == "no":
        print("Goodbye")
        break
    else:
        print("Invalid input")
        
    