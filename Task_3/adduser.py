# Import necessary modules
import getpass
import codecs

# Function to add a new user
def add_user():
    # Get user input for new username, real name, and password
    new_username = input("Enter new username: ")
    user_real_name = input("Enter real name: ")
    user_password = getpass.getpass("Enter password: ")

    # Check if the new_username already exists in the passwd.txt file
    with open("passwd.txt", "r") as file:
        for read in file.readlines():
            existing_usernames = read.split(":")[0] 

            # If username already exists, print an error and return
            if new_username in existing_usernames:
                print("Cannot add. Most likely username already exists.")
                return

    # Encode the password using ROT13
    encoded_password = codecs.encode(user_password, 'rot_13')

    # Append the new user information to the end of passwd.txt file
    with open("passwd.txt", "a") as file:
        file.write(f"{new_username}:{user_real_name}:{encoded_password}\n")

    # Print a success message
    print("User Created.")

# Execute the add_user function if this script is run
if __name__ == "__main__":
    add_user()
