import os

#rename file in the folders

def rename_file(folder_path,new_filenames):
    #files exists in the current folder
    if not os.path.exists(folder_path):
        print("File doesn't exist {folder_path}")
        return
    
    #if file is present then, 
    for index, filename in enumerate(os.listdir(folder_path)):
            print("index : "+ str(index))
            print("current File = " + filename)
            new_file = new_filenames[index]

            old_filename = os.path.join(folder_path,filename)
            new_filename = os.path.join(folder_path,new_file)
            os.rename(old_filename,new_file)
            print("---------------------------")
            print("Old-file " + old_filename)
            print("New-file " + new_filename)
            print("---------------------------")


folder_path="/Users/vandana/Documents/test"
new_filenames=["pop.txt","me.txt"]
rename_file(folder_path,new_filenames)

