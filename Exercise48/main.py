# Write a function that removes duplicate characters from a given string.

user_i = input("What's your inpput? ")

new_user_i = ''.join(sorted(set(user_i), key=user_i.index))
print(new_user_i)

characters_encountered = ""

for char in user_i:
    if char not in characters_encountered:
        characters_encountered += char

print(characters_encountered)

