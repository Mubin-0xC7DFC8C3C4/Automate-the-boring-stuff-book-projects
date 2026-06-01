import re

def is_password_strong(password):
    if len(password) < 8:
        print("Error: Password must be at least 8 characters long")
        return False

    if not re.search(r'[A-Z]', password):
        print("Error: Password must contain at least one uppercase letter")
        return False

    if not re.search(r'[a-z]', password):
        print("Error: Password must contain at least one lowercase letter")
        return False

    if not re.search(r'\d', password):
        print("Error: Password must contain at least one digit")
        return False
    
    return True

user_input = input("Enter your password: ")

if is_password_strong(user_input):
    print("Password accepted")
else:
    print("Weak password. Please try again")