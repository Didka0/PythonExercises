import colorama
from colorama import Fore


name = input("What's your name? ").capitalize()
print("Hello,", name)

answer = input("Do you want to calculate your BMI? ").lower()
if answer =="yes":
    pass
    print( Fore.YELLOW + "\nPlease enter your height like this: 1.60","\nOr your results will be invalid." + Fore.RESET )
elif answer == "no":
    print("See you later!")
    exit
else:
    print(Fore.RED + "Invalid input" + Fore.RESET )

def BMI_calculator():
    weight = int(input("\nWhat's your weight? "))
    height = float(input("What's your height? "))

    BMI = weight / (height * height)
    BMI = round(BMI, 2)
    print(Fore.LIGHTMAGENTA_EX + "Your BMI is: ",BMI)

BMI_calculator()