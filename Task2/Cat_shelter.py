import sys

def analyze_pet_shelter_log(log_filename):
    try:
        # Read the contents of the log file into a list of lines
        with open(log_filename, 'r') as file:
            lines = file.readlines()

        # Initialize variables to store statistics
        pet_visits = 0
        other_pets = 0
        total_time_in_shelter = 0
        longest_stay = 0
        shortest_stay = float('inf')

        # Iterate through each line in the log file
        for line in lines:
            # Check for the end of the log
            if line.strip() == "END":
                break
            
            # Split the line into parts using comma as the delimiter
            parts = line.strip().split(',')
            pet_name, entry_time, exit_time = parts
            
            # Convert entry and exit times to integers
            entry_time = int(entry_time)
            exit_time = int(exit_time)

            # Calculate the duration of the pet's stay
            duration = exit_time - entry_time

            # Check if the pet is "OURS" or another pet
            if pet_name == "OURS":
                pet_visits += 1
                total_time_in_shelter += duration

                # Update the longest and shortest stay if necessary
                if duration > longest_stay:
                    longest_stay = duration

                if duration < shortest_stay:
                    shortest_stay = duration
            else:
                other_pets += 1

        # Calculate the average stay length
        average_stay_length = total_time_in_shelter / pet_visits if pet_visits > 0 else 0

        # Convert total time to hours and minutes
        total_hours = total_time_in_shelter // 60
        total_minutes = total_time_in_shelter % 60

        # Print the analysis results
        print("\nLog File Analysis")
        print("==================\n")
        print(f"Pet Visits: {pet_visits}")
        print(f"Other Pets: {other_pets}\n")
        print(f"Total Time in Shelter: {total_hours} Hours, {total_minutes} Minutes\n")
        print(f"Average Stay Length: {int(average_stay_length)} Minutes")
        print(f"Longest Stay:        {longest_stay} Minutes")
        print(f"Shortest Stay:       {shortest_stay} Minutes")

    except FileNotFoundError:
        # Handle the case where the specified log file is not found
        print(f'Cannot open "{log_filename}"!')

# Check if the correct number of command line arguments is provided
if len(sys.argv) != 2:
    print("Missing command line argument!")
else:
    # Call the function to analyze the pet shelter log file
    analyze_pet_shelter_log(sys.argv[1])
