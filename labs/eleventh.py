lines = []
print("Enter a sequence of lines (Enter to end):")
while True:
    line = input()
    if not line:
        break
    lines.append(line.lower())
print()
print("Output:")
for line in lines:
    print(line)