vowels = [
    "a",
    "e",
    "i",
    "o",
    "u"
]

def get_number_of_vowels(user_input: str):
    counter = 0
    for character in user_input:
        for vowel in vowels:
            if vowel.lower() == character.lower():
                counter += 1
    
    return counter

def get_number_of_vowels1(user_input: str):
    counter = 0
    for character in user_input:
        if character in vowels:
            counter += 1
    
    return counter

   
def main():
    answer = input("Do you want to count vowels in your word or sentence? ")
    if answer == "yes":
        pass
    elif answer == "no":
        print("see you later!")
    else:
        print("Invalid input")

    user_input = input("Write your input: ")
    number_of_vowels1 = get_number_of_vowels(user_input)
    number_of_vowels2 = get_number_of_vowels1(user_input)
    print(number_of_vowels1)
    print(number_of_vowels2)


main()

