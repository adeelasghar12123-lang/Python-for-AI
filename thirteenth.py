text = input("Enter a string: ")

letters = 0
digits = 1

for char in text:
    if char.isalpha():
        letters += 1
    elif char.isdigit():
        digits += 1