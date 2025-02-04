def factorial(n):
    y = 1
    for x in range(2, n + 1):
        y = y * x
    print(y)

factorial(4)