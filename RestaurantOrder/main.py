menu = {
    "Coke", 
    "Pizza",
    "Chicken nuggets",
    "Tea",
    "Coffee",
    "Latte"
}

print("Hello,you have 20$ to spend")

def main():
    print("Menu: \n Coke - 2$ \nPizza - 10$ \nChicken nuggets - $8 \nTea - 3$ \nCoffee - 3$ \nLatte - 5$")
    money_left = 20

    while(money_left > 0):
        user_choice = (input("What would you like to order:"))
        if user_choice == "Coke":
            money_left -= 2
            print("Current receipt: ", 2, "$")
        elif user_choice == "Pizza":
            money_left -= 10
            print("Current receipt: ", 10, "$")
        elif user_choice == "Chicken nuggets":
            money_left -= 8
            print("Current receipt: ", 8, "$")
        elif user_choice == "Tea":
            money_left -= 3
            print("Current receipt: ", 3, "$")
        elif user_choice == "Coffee":
            money_left -= 3
            print("Current receipt: ", 3, "$")
        elif user_choice == "Latte":
            money_left -= 5
            print("Current receipt: ", 5, "$")
    
    print("Not enough money to continue")
        
main()
