import os
import datetime

def rename_file_with_datetime(folder_path):
    # Check if the folder exists
    if not os.path.exists(folder_path):
        print("Folder doesn't exist:", folder_path)
        return
    
    # Get the current datetime             string_format year,month,day || hour,month,second
    current_datetime = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

    # Iterate over files in the folder
    for index, filename in enumerate(os.listdir(folder_path)):

        #-1 < len(abc.txt)   - out of range
        if index < len(new_filenames):
            new_file = new_filenames[index]
        else:
            #1 > len(abc.txt)    12:01:00_1
            new_file = f"{current_datetime}_{index}"

        old_filename = os.path.join(folder_path, filename)
        new_filename = os.path.join(folder_path, new_file)

        os.rename(old_filename, new_filename)
        print("Renamed:", filename, "to", new_file)

# Example usage:
folder_path = "/Users/vandana/Documents/test"
new_filenames=[]
rename_file_with_datetime(folder_path)
