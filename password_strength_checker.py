#Task 3: Password Strength Checker
'''Create a Python function that evaluates the strength of a password entered by the 
user. Implement checks for factors such as length, presence of uppercase and lowercase 
letters, digits, and special characters'''

import string

def check_password_strength(password):
    strength = 0
    feedback = []

    # check the lenght
    if len(password) >= 8:
        strength += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    # check the lowercase letters
    if any(l.islower() for l in password):
        strength += 1
    else:
        feedback.append("Add at least one lowercase letter.")

    # check the uppercase letters
    if any(u.isupper() for u in password):
        strength += 1
    else:
        feedback.append("Add at least one uppercase letter.")

    # check the number
    if any(n.isdigit() for n in password):
        strength += 1
    else:
        feedback.append("Include at least one number.")

    # check the punctuation
    if any(c in string.punctuation for c in password):
        strength += 1
    else:
        feedback.append("Include at least one special character (!@#$ etc.).")

    if strength == 5:
        return "Strong password!"
    elif 3 <= strength < 5:
        return "Medium password:\n" + "\n".join(feedback)
    else:
        return "Weak password:\n" + "\n".join(feedback)


user_pass = input("Enter a password to check: ")
result = check_password_strength(user_pass)
print(result)
