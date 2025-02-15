menu = {
    "Coke", 
    "Pizza",
    "Chicken nuggets",
    "Tea",
    "Coffee",
    "Latte",
    "Exit"
}

print("Hello,you have 20$ to spend")

def main():
    print("Menu: \n Coke - 2$ \nPizza - 10$ \nChicken nuggets - $8 \nTea - 3$ \nCoffee - 3$ \nLatte - 5$")
    print("\nTo finish your order type: Exit")
    money_left = 20

    while(money_left > 0):
        user_choice = (input("\nWhat would you like to order:"))
        if user_choice == "Exit":
            print("Goodbye!")
            break
        if user_choice == "Coke":
            money_left -= 2
            if money_left < 0:
                break
            else:
                print("Current receipt: ", 2, "$")
                continue
        elif user_choice == "Pizza":
            money_left -= 10
            if money_left <= 0:
                break
            else:
                print("Current receipt: ", 10, "$")
                continue
        elif user_choice == "Chicken nuggets":
            money_left -= 8
            if money_left <= 0:
                break
            else:
                print("Current receipt: ", 8, "$")
                continue
        elif user_choice == "Tea":
            money_left -= 3
            if money_left <= 0:
                break
            else:
                print("Current receipt: ", 3, "$")
                continue
        elif user_choice == "Coffee":
            money_left -= 3
            if money_left <= 0:
                break
            else:
                print("Current receipt: ", 3, "$")
                continue
        elif user_choice == "Latte":
            money_left -= 5
            if money_left <= 0:
                break
            else:
                print("Current receipt: ", 5, "$")
                continue
    
    while(money_left <= 0):
        print("Not enough money to continue")
        break
main()