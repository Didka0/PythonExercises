import colorama
from colorama import Fore

def string_reverse_slicing(string):
    reversed_str = string[::-1]
    return reversed_str


def reversed_string_loop(string):
    reversed_str = ""
    for char in reversed(string):
        reversed_str += char
    
    return reversed_str


def main():
    string_to_reverse = "So many books, so little time."
    print(string_to_reverse)

    print(Fore.LIGHTGREEN_EX + string_reverse_slicing(string_to_reverse) + Fore.RESET)

    print(Fore.LIGHTYELLOW_EX + reversed_string_loop(string_to_reverse) + Fore.RESET)
    


main()