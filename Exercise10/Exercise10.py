def calculator(num1, operator, num2):
    if operator == "-":
        return num1 - num2
    elif operator == "+":
        return num1 + num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        return num1 / num2
    else:
        print("Wrong operator")

def main():
    first_number = int(input("First number: "))
    operator = input("Choose operator")
    second_nubmer = int(input("Second number"))
    
    result = calculator(first_number, operator, second_nubmer)
    print(result)

main()