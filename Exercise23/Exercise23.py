def sum_of_evens():
    result = 0

    for x in range(0, 101):
        if x % 2 ==0:
            result = result + x
    
    print("Sum of all evens is: ")    
    print(result)

sum_of_evens()

def sum_of_odds():
    result = 0

    for x in range(0, 101):
        if x % 2 !=0:
            result = result + x
    
    print("Sum of all odds is: ") 
    print(result)
    
sum_of_odds()