import random
import string


def generate_password(length=12):
    # Define characters to use in the password
    chars = string.ascii_letters + string.digits + string.punctuation

    # Generate a random password
    password = "".join(random.choice(chars) for _ in range(length))

    return password


if __name__ == "__main__":
    print("======================")
    print("= PASSWORD GENERATOR =")
    print("======================")

    length = int(input("Choose the password length (e.g. 12): "))
    password = generate_password(length)
    print("\nSecure Password:")
    print(f"\033[1;32m{password}\033[0m")
