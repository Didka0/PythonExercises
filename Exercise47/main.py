# Find Longest Word - Write a function that finds the longest word in a given sentence.
import colorama
from colorama import Fore

def find_longest_word(word_list):
    longest_word = max(word_list, key=len)
    return longest_word


def main():
    while True:
        print("Let's find the longest word in your sentence!")
        user_i = input(Fore.LIGHTYELLOW_EX + "\nWrite your sentence here: " + Fore.RESET).lower()
        
        word_list = user_i.split()

    
        longer_word = find_longest_word(word_list)
        print("\nLonger word is: ",longer_word)
        
        letters_count = len(longer_word)
        print("\nLetters count: ",letters_count)
        answer = input("\nAgain? ").lower()
        if answer == "yes":
            pass
        elif answer == "no":
            exit()
        else:
            print(Fore.LIGHTRED_EX + "\nInvalid input" + Fore.RESET)
            exit()

main()