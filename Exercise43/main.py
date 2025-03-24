name = input("What's your name? ")
print("Hello,", name)

answer = input("Do you want to calculate your BMI? ").lower()
if answer =="yes":
    pass
    print("Please enter your height like this: 1.60","\nOr your results will be invalid.")
elif answer == "no":
    print("See you later!")
    exit
else:
    print("Invalid input")

def BMI_calculator():
    weight = int(input("\nWhat's your weight? "))
    height = float(input("What's your height? "))

    BMI = weight / (height * height)
    BMI = round(BMI, 2)
    print("Your BMI is: ",BMI)

BMI_calculator()