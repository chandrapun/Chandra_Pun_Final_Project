# Import necessary modules with alias names for better readability
import codecs as code_module
import getpass as user_input

# Function to perform user login
def login():
    # Get user input for username and password
    input_username = input("User: ")
    input_password = user_input.getpass("Password: ")

    # Hash the password using ROT13 encoding
    encoded_password = code_module.encode(input_password, 'rot_13')

    # Check if the user exists and the password is correct
    with open("passwd.txt", "r") as file:
        # Iterate through each line in the file
        for line in file:
            # Split the line into parts using ":" as a separator
            parts = line.split(":")
            
            # Check if the current line corresponds to the input username and password
            if parts[0] == input_username and parts[2].strip() == encoded_password:
                # Grant access and return from the function
                print("Access granted.")
                return

    # Print an error message if the user is not found or the password is incorrect
    print("Access denied.")

# Execute the login function if this script is run
if __name__ == "__main__":
    login()
