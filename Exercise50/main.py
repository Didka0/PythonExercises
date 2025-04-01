# odd or even

user_i = int(input("What's your number? "))

def odd_or_even():
    if user_i % 2 == 0:
        print("Your number is - even!")
    elif user_i % 2 != 0:
        print("Your number is - odd!")
    elif user_i == 0:
        print("You can't divide zero")

odd_or_even()