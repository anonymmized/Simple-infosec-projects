import random
import string

def password_generate(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for n in range(length))
    return password

per = int(input("Enter password length: "))
print(f"Generated password: {password_generate(per)}")