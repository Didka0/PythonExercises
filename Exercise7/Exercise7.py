def is_triangle(a,b,c):
    if a + b > c and a + c > b and b + c > a:
        return True
    else:
        return False

x = int(input("What's x? "))
y = int(input("What's y? "))
z = int(input("What's z? "))

answer = is_triangle(x,y,z)

print(answer)