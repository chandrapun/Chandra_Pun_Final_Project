# Import necessary modules with alias names for better readability
import codecs as code_module
import getpass as user_input

# Function to change the password for a user
def change_password():
    # Get user input for username and passwords
    input_username = input("User: ")
    current_input_password = user_input.getpass("Current Password: ")
    new_input_password = user_input.getpass("New Password: ")
    confirm_input_password = user_input.getpass("Confirm: ")

    # Hash the passwords using ROT13 encoding
    current_hash = code_module.encode(current_input_password, 'rot_13')
    new_hash = code_module.encode(new_input_password, 'rot_13')

    # Read the content of the password file
    with open("passwd.txt", "r") as file:
        lines = file.readlines()

    # Flag to check if the user is found in the file
    user_found = False

    # Open the file in write mode to update passwords
    with open("passwd.txt", "w") as file:
        # Iterate through each line in the file
        for line in lines:
            # Split the line into parts using ":" as a separator
            parts = line.split(":")
            
            # Check if the current line corresponds to the input username
            if parts[0] == input_username:
                # Check if the current password matches the stored password
                if parts[2].strip() == current_hash:
                    # Update the password if the current password is valid
                    user_found = True
                    file.write(f"{parts[0]}:{parts[1]}:{new_hash}\n")
                    print("Password changed.")
                else:
                    # Print an error message if the current password is invalid
                    print("Invalid current password. Nothing changed.")
            else:
                # Write the unchanged line to the file for other users
                file.write(line)

    # Print a message if the user is not found in the file
    if not user_found:
        print("User not found. Nothing changed.")

# Execute the change_password function if this script is run
if __name__ == "__main__":
    change_password()
