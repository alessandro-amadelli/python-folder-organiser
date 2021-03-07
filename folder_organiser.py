"""
python-folder-organiser

This script automatically organise all the files of a folder named 'Misc' by moving them in various folders depending
on their extensions.

Author: Ama
"""
import os

#python dictionary containing all folder names and relative file extensions
FOLDER_TYPES = {
    "Music": [
    '.mp3', '.m4a', '.flac', '.wav', '.wma', '.aac'
    ],
    "Videos": [
    '.avi', '.mpg', '.mp2', '.mp4', '.mpeg', '.mpe', '.mpv', '.mkv', '.m4p', '.m4v', '.wmv', '.mov', '.qt', '.swf', '.flv'
    ],
    "Documents": [
    '.doc', '.docx', '.xls', '.xlsx', '.txt', '.odt', '.ods', '.ppt', '.pptx', '.html', '.htm'
    ],
    "PDFs": [
    '.pdf'
    ],
    "Photos": [
    '.tif', '.tiff', '.bmp', '.jpg', '.jpeg', '.gif', '.png', '.eps', '.raw', '.cr2', '.nef', '.orf', '.sr2'
    ]
}


def get_file_names():
    """
    This function returns a list containing full pathname of each file present in the 'Misc' folder
    """
    current_dir = os.getcwd() #current directory
    misc_dir = os.path.join(os.getcwd(), 'Misc')

    #Check if the folder 'Misc' already exists and if not, it proceeds to create it
    if not os.path.isdir(misc_dir):
        os.mkdir(misc_dir)

    #List of all files in the 'Misc' folder
    #Each element in the list is a set containing full file path and filename
    file_list = [(os.path.join(misc_dir,file), file) for file in os.listdir(misc_dir) if os.path.isfile(os.path.join(misc_dir, file))]

    return file_list


def organise_file(filepath, filename):
    """
    Given a file path and name, this function checks the file extension and moves the file to the corresponding folder
    """
    file, extension = os.path.splitext(filename)

    destination_folder = ""

    for fn in FOLDER_TYPES:
        if extension.lower() in FOLDER_TYPES[fn]:
            destination_folder = os.path.join(os.getcwd(), fn)
            break

    #If extension is not in my extensions list, just return an empty string and leave the file in the 'Misc' directory
    if destination_folder == "":
        return "passed"

    #Creates the folder if doesn't exist
    if not os.path.isdir(destination_folder):
        os.mkdir(destination_folder)

    #Move the file from the original folder to the destination folder mantaining the same file name
    #checks if file already exists to avoid unwanted overwriting
    new_filepath = os.path.join(os.getcwd(), destination_folder, filename)
    if not os.path.isfile(new_filepath):
        os.rename(filepath, new_filepath)

    return destination_folder


if __name__ == "__main__":
    """
    Main execution
    """
    print("Perusing your files...")
    file_list = get_file_names()

    file_tot = len(file_list) #Total number of files in 'Misc'

    print("Moving files around...")

    folders = {}

    #for loop to move each file and save the counter for final stats
    for f in file_list:
        folder = organise_file(f[0], f[1])
        if folder in folders.keys():
            folders[folder] += 1
        else:
            folders[folder] = 1

    print("Finished!")

    #Final Stats
    print(f"Processed a total of {file_tot} files")
    for f in folders:
        if f != "passed":
            print(f" # {folders[f]} file(s) moved in folder {f}")

    if "passed" in folders.keys():
        print(f" # {folders['passed']} file(s) left unmoved...")
