print("Hello,you have 20$ to spend")

def main():
    print("Menu: \n Coke - 2$ \nPizza - 10$ \nChicken nuggets - $8 \nTea - 3$ \nCoffee - 3$ \nLatte - 5$")
    print("\nTo finish your order type: Exit")
    money_left = 20

    while(money_left > 0):
        user_choice = input("\nWhat would you like to order:").lower()

        if user_choice == "exit":
            print("Goodbye!")
            break
        if user_choice == "coke":
            price_of_item = 2
        elif user_choice == "pizza":
            price_of_item = 10
        elif user_choice == "chicken nuggets":
           price_of_item = 8
        elif user_choice == "tea":
            price_of_item = 3
        elif user_choice == "coffee":
            price_of_item = 3
        elif user_choice == "latte":
            price_of_item = 5

        money_left -= price_of_item
        if money_left < 0:
            print("Not enough money to continue")
        else:
            print("Current receipt: ", price_of_item, "$")

main()