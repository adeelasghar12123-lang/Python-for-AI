
binary_input = input("Enter comma-separated 4-digit binary numbers: ")
binary_list = binary_input.split(',')
valid_numbers = []

for binary_str in binary_list:
    clean_str = binary_str.strip()
    decimal_num = int(clean_str, 2)
    if decimal_num % 5 == 0:
        valid_numbers.append(clean_str)
print(",".join(valid_numbers))