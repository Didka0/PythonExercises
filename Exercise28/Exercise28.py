def fibonacci_series():
    a = 0
    b = 1
    for _ in range (0, 15):
        print(a)
        temp = a
        a = b
        b += temp
    
fibonacci_series()