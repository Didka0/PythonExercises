
from colorama import Fore, Back, Style
balance = 0

while True:
    user_choice = input(Fore.YELLOW + "Choose a command: deposit, withdraw, exit. \n" + Style.RESET_ALL).lower()

    if user_choice == "deposit":
        deposit = int(input(Fore.YELLOW + "How much would you like to deposit?\n" + Style.RESET_ALL))
        balance = balance + deposit
        print(Fore.BLUE + "Your new balance is ", balance)
    elif user_choice == "withdraw":
        withdraw = int(input(Fore.YELLOW + "How much would you like to withdraw?\n" + Style.RESET_ALL))
        balance = balance - withdraw
        print(Fore.BLUE + "Your new balance is: ", balance)
        if balance == 0:
            print("☠️")
    elif user_choice == "exit":
        print(Fore.LIGHTMAGENTA_EX + "Goodbye!","👋")
        exit()
    else:
        print(Fore.RED + "Invalid input" + Style.RESET_ALL)
        pass