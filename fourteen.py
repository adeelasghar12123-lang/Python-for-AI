import re
password = input("Enter a password to test: ")
valid = True
if len(password) < 6 or len(password) > 16:
    valid = False
elif not re.search(r"[a-z]", password):
    valid = False
elif not re.search(r"[A-Z]", password):
    valid = False
elif not re.search(r"[0-9]", password):
    valid = False
elif not re.search(r"[$#@]", password):
    valid = False

if valid:
    print("Valid password!")
else:
    print("Invalid password. It does not meet the requirements.")