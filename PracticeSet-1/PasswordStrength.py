password = input()
has_digit = any(ch.isdigit() for ch in password)
has_upper = any(ch.isupper() for ch in password)

if len(password) >= 8 and has_digit and has_upper:
    print("STRONG")
else:
    print("WEAK")