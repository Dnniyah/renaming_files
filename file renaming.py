import os  # Import the OS module to interact with the operating system

# Get folder path and renaming pattern from the user
folder_path = input("Enter the path to the folder containing files to rename: ")  # Prompt the user for folder path
renaming_pattern = input("Enter the new naming pattern (e.g., 'file_'): ")  # Prompt the user for the renaming pattern
start_index = int(input("Enter the starting index number (e.g., 1): "))  # Ask the user for a starting number

# Check if the provided folder exists
if not os.path.exists(folder_path):
    print(f"Error: The folder '{folder_path}' does not exist.")  # Print error if the folder doesn't exist
else:
    # Loop through each file in the folder
    for index, filename in enumerate(os.listdir(folder_path), start=start_index):
        # Get the file extension (e.g., .txt, .jpg)
        file_extension = os.path.splitext(filename)[1]  # Split the file name and extension

        # Construct the new file name with the provided pattern and index number
        new_filename = f"{renaming_pattern}{index}{file_extension}"

        # Get the full file paths for renaming
        source = os.path.join(folder_path, filename)  # Original file path
        destination = os.path.join(folder_path, new_filename)  # New file path with renamed file

        # Rename the file
        os.rename(source, destination)

        # Print the renaming action
        print(f"Renamed '{filename}' to '{new_filename}'")

print("All files renamed successfully!")
