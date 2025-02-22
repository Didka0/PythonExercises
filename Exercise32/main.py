import random

def get_user_choice():
    choice = input("Choose: head or tails? ").lower()
    if choice == "head":
        print("You chose - head")
    elif choice == "tails":
        print("You chose - tails")
    
    return choice

def get_computer_choice():
    choice = random.choice(["head", "tails"])
    print("Computer chose - ", choice)
    return choice
  
    
def main():
    answer = input("Would you like to play? ").lower()
    if answer == "no":
        print("Goodbye")
        exit()
    elif answer != "yes":
        print("Invalid command")
        exit()

    player_choice = get_user_choice()
    computer_choice = get_computer_choice()

    flip_coin = random.choice(["head", "tails"])
    print("Flipped coin is - ", flip_coin)

    if player_choice == computer_choice:
        print("Draw")
    elif player_choice == "tails" and computer_choice == "head" and flip_coin == "tails":
        print("You won")
    elif player_choice == "head" and computer_choice == "tails" and flip_coin == "head":
        print("You won")
    elif player_choice == "tails" and computer_choice == "head" and flip_coin == "head":
        print("Computer won")
    elif player_choice == "head" and computer_choice == "tails" and flip_coin == "tails":
        print("Computer won")

main()