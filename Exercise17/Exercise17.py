def print_pattern(n):
    for x in range (0, n):    
        for y in range (0, x+1):
            print("#", end="")
    
        print()

print_pattern(8)