
def reverse_string(text):
    stack = []
    
    for char in text:
        stack.append(char)
        
    reversed_text = ""

    while len(stack) > 0:
        reversed_text += stack.pop()
        
    return reversed_text


original = "Scorpion"
result = reverse_string(original)

print(f"Original: {original}")
print(f"Reversed: {result}")