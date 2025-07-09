#Task 3: Email Validator
'''Develop a Python function that validates whether a given string is a valid email address. 
Implement checks for the format, including the presence of an "@" symbol and a domain name'''

def email_validation(email_id):
    username, domain = email_id.split("@")
    if ("@" not in email_id) or (email_id.count("@") != 1): #input: XXXXgmail.com
        return False
        
    if (not username) or (not domain): #input: @gmail.com or XXXX@
        return False
        
    if ("." not in domain) or (domain.startswith(".")) or (domain.endswith(".")):
        return False #input: XXXX@gmailcom or XXXX@.gmailcom or XXXX@gmailcom.
    
    return True

def main():
    email_id = input("enter the input:").strip()
    result = email_validation(email_id)
    if result :
        print("Valid") 
    else:
        print("Invalid")

main()