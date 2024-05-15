def check_password_strength(password):
    if len(password) >= 8 and any(char.isupper() for char in password) and any(char.isdigit() for char in password) and any(char in '!@#$%^&*(),.?":{}|<>' for char in password):
        return "seems good"
    else:
        return "tf is this bruh?"
user_password = input("Enter ur passowrd nigga: ")
result = check_password_strength(user_password)
print(result)
