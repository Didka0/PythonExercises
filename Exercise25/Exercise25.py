list = [10, 5, 4, 7, 12, 30, 150, 600, 20, 75, 160, 230, 700]

def display_numbers():
    for x in list:
        if x > 500:
            break

        if x > 150:
            continue

        if x % 5 == 0:
            print(x)

display_numbers()
