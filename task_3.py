import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    for i in range(length):
        print(''.join(random.choice(characters)),end="")
        
length = int(input("Enter the length of password you want : "))
generate_password(length)

