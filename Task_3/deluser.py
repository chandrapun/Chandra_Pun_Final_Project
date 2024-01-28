# Function to delete a user from the passwd.txt file
def delete_user():
    # Get user input for the username to be deleted
    input_username = input("Enter username: ")

    # Read the content of the password file
    with open("passwd.txt", "r") as file:
        file_content = file.readlines()

    # Flag to check if the user is found in the file
    user_found = False

    # Open the file in write mode to update the content
    with open("passwd.txt", "w") as file:
        # Iterate through each line in the file
        for line in file_content:
            # Check if the current line does not correspond to the input username
            if line.split(":")[0] != input_username:
                # Write the unchanged line to the file for other users
                file.write(line)
            else:
                # Set the flag to indicate that the user is found
                user_found = True

    # Print a message based on whether the user is found or not
    if user_found:
        print("User Deleted.")
    else:
        print("User not found. Nothing changed.")

# Execute the delete_user function if this script is run
if __name__ == "__main__":
    delete_user()
