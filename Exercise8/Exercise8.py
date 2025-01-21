def fizz_buzz(number):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 5 == 0:
        print("Buzz")
    elif number % 3 == 0:
        print("Fizz")
    else:
        print(number)

    # if number % 3 == 0:
    #     print("Fizz", end="")
    
    # if number % 5 == 0:
    #     print("Buzz", end="")
    # else:
    #     print(number)

user_input = int(input("Write a number: "))
fizz_buzz(user_input)