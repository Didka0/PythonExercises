def reverse_text(text):
    rev_text = ""
    for char in text:
        rev_text = char + rev_text

    return rev_text
    
reversed_text = reverse_text("123")
print(reversed_text)