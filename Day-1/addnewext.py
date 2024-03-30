import os

def change_file_extensions(folder_path, new_extension):
    # Check if the folder exists
    if not os.path.exists(folder_path):
        print("Folder doesn't exist:", folder_path)
        return
    
    # Iterate over files in the folder
    for filename in os.listdir(folder_path):
        # Get the full path of the file
        file_path = os.path.join(folder_path, filename)

        # Check if it's a file
        if os.path.isfile(file_path):
            # Split the filename and extension
            file_name , file_extension = os.path.splitext(filename)

            # Create a new filename with the new extension
            new_filename = file_name + "." + new_extension

            # Rename the file
            os.rename(file_path, os.path.join(folder_path, new_filename))
            print("Renamed:", filename, "to", new_filename)


# Example usage:
folder_path = "/Users/vandana/Documents/test"
new_extension = "csv"  # New extension you want to change to
change_file_extensions(folder_path, new_extension)
