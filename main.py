import random
import string

def generate_random_password(length=12):
    # Define characters to use for generating the password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Ensure that the password contains at least one of each character type
    password = [random.choice(string.ascii_lowercase),
                random.choice(string.ascii_uppercase),
                random.choice(string.digits),
                random.choice(string.punctuation)]

    # Generate the remaining characters for the password
    remaining_length = length - len(password)
    for _ in range(remaining_length):
        password.append(random.choice(characters))

    # Shuffle the password characters to make it random
    random.shuffle(password)

    # Convert the list of characters to a string
    password = ''.join(password)

    return password

# Generate a random password with a default length of 12 characters
random_password = generate_random_password()
print("Generated Password:", random_password)
