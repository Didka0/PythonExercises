import colorama
from colorama import Fore

print("Please enter your grades like this: 5.50 ")

user_i = float(input("\nWhat is your grade? "))

if user_i >= 5.50:
    print(Fore.LIGHTYELLOW_EX + "\nExellent!" + Fore.RESET)
elif user_i >= 4 and user_i < 5.50:
    print(Fore.LIGHTYELLOW_EX + "\nGood result!" + Fore.RESET)
elif user_i < 1:
    print(Fore.LIGHTRED_EX + "\nInvalid input" + Fore.RESET)