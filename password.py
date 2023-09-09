import random
import string

def generate_password(length):
    # Define the character sets for the password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate a random password by selecting characters randomly from the set
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

# Get user input for the desired password length
try:
    password_length = int(input("Enter the desired password length: "))
except ValueError:
    print("Invalid input. Please enter a valid integer for password length.")
    exit(1)

# Check if the password length is valid (greater than 0)
if password_length <= 0:
    print("Password length should be greater than 0.")
else:
    # Generate and print the random password
    random_password = generate_password(password_length)
    print("Random Password: ", random_password)
