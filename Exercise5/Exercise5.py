def check_number(number):
    if number == 0:
        print("Your number is: Zero")
    if number > 0:
        print("Your number is: Positive")
    if number < 0:
        print("Your number is: Negative")

user_input = int(input("Write your number: "))
check_number(user_input)