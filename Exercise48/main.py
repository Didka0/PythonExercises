# Write a function that removes duplicate characters from a given string.
import colorama
from colorama import Fore

user_i = input("What's your inpput? ")
print()

new_user_i = ''.join(sorted(set(user_i), key=user_i.index))
print(Fore.YELLOW + new_user_i + Fore.RESET)

print()

characters_encountered = ""

for char in user_i:
    if char not in characters_encountered:
        characters_encountered += char

print(Fore.GREEN + characters_encountered + Fore.RESET)

