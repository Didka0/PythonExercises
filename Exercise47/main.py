# Find Longest Word - Write a function that finds the longest word in a given sentence.

print("Let's find the longest word in your sentence!")

def find_longest_word(word_list):
    longest_word = max(word_list, key=len)
    return longest_word

def main():
    user_i = input("Write your sentence here: ").lower()
    word_list = user_i.split()

  
    longer_word = find_longest_word(word_list)
    print("Longer word is: ",longer_word)

main()




