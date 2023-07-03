import random
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits # "+ string.punctuation" can be used if you want punctuations in the password.
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

if __name__ == "__main__":
    password_length = int(input("Enter the desired password length: "))
    password = generate_password(password_length)
    print("Generated Password:", password)

"""string.ascii_letters (containing both uppercase and lowercase letters), string.digits (containing digits 0-9), and string.punctuation (containing special characters) to create a password of the specified length."""
