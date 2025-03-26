import colorama
from colorama import Fore

def is_palindrome_1(user_i):
    reversed_input = user_i[::-1]
    if reversed_input == user_i:
        return True
    
    return False

def is_palindrome_2(user_i):
    for index in range(len(user_i)):
        right_index = len(user_i) - index - 1

        if user_i[index] != user_i[right_index]:
            return False
        
        diff = right_index - index

        if diff == 2:
            return True
        
    return True


def main():
    while True:
        answer = input("\nDo you want to check if your sentence or word is palindrome? ").lower()

        if answer == "yes":
            pass
        elif answer == "no":
            print("See you later!")
            exit()
        else:
            print(Fore.RED + "Invalid input" + Fore.RESET)
            exit()

        user_i = input("\nCheck your input: ")
        result = is_palindrome_2(user_i)

        if is_palindrome_1(user_i):
            print(Fore.GREEN + "\nIt's a palindrome!" + Fore.RESET)
        else:
            print(Fore.LIGHTRED_EX + "\nIt's not a palindrome!" + Fore.RESET)

        if is_palindrome_2(user_i):
            print(Fore.LIGHTCYAN_EX + "\nIt's a palindrome!" + Fore.RESET)
        else:
            print(Fore.MAGENTA + "\nIt's not a palindrome!" + Fore.RESET)
        
        again = input("\nWant to check again? ").lower()
        if again == "yes":
            pass
        elif again == "no":
            print("\nSee you later!")
            exit()
        else:
            print(Fore.LIGHTRED_EX + "\nInvalid input" + Fore.RESET)
            exit()
main()
