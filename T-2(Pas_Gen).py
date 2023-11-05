import random
import string

def generateme_password(length, need_uppercase, need_lowercase, need_digits, need_spl_chars):
    characters = ""
    
    if need_uppercase:
        characters += string.ascii_uppercase
    if need_lowercase:
        characters += string.ascii_lowercase
    if need_digits:
        characters += string.digits
    if need_spl_chars:
        characters += string.punctuation
    
    if length <= 0:
        return "Entering password must be above 0."
    
    if not characters:
        return "Select atleast one choice to Generete."
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Generate Me Password")
    try:
        length = int(input("Enter the Better password length: "))
        
        need_uppercase = input("Do You Need uppercase ? (yes/no): ").lower() == "yes"
        need_lowercase = input(" Do You Need lowercase ? (yes/no): ").lower() == "yes"
        need_digits = input("Do You Need digits? (yes/no): ").lower() == "yes"
        need_spl_chars = input("Do You Need special characters? (yes/no): ").lower() == "yes"
        
        password = generateme_password(length, need_uppercase, need_lowercase, need_digits, need_spl_chars)
        
        if password:
            print("Here is your Password:", password)
            print("It keeps You Safe")
        else:
            print("Sorry I Unable To Generete.")
    except ValueError:
        print("Invalid input. Give Me a valid number for password length.")

if __name__ == "__main__":
    main()
