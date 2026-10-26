password = input("Enter password: ")

has_digit = False

for ch in password:
    if ch.isdigit():
        has_digit = True

if len(password) >= 8 and has_digit:
    print("Password is valid")
else:
    print("Password is invalid")

    if len(password) < 8:
        print("Password must have at least 8 characters")

    if not has_digit:
        print("Password must contain a digit")