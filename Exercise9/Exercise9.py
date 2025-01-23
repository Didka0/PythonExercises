def celsius_to_fahrenheit(number):
    return number * 9/5 + 32

c = int(input("Write a celsius number: "))
f = celsius_to_fahrenheit(c)
print(f)