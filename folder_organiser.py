"""
python-folder-organiser

This script automatically organise all the files of a folder named 'Misc' by moving them in various folders depending
on their extensions.

Author: Ama
"""
import os
import sys
import time

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


def logo_print():
    print("\n\n")
    print("=" * 40)
    print(" ****  *   *  *****  *  *   ***   *   *")
    time.sleep(0.2)
    print(" *  *   * *     *    *  *  *   *  **  *")
    time.sleep(0.2)
    print(" ****    *      *    ****  *   *  * * *")
    time.sleep(0.2)
    print(" *       *      *    *  *  *   *  *  **")
    time.sleep(0.2)
    print(" *       *      *    *  *   ***   *   *")
    time.sleep(0.2)
    print(" " + "-" * 38)
    time.sleep(0.3)
    print(" F O L D E R          O R G A N I S E R")
    print("=" * 40)
    print("\n\n")
    time.sleep(0.3)

def show_instructions():
    print("INSTRUCTIONS")
    print("1. Create a folder named 'Misc' in the same directory as the script \n" \
    "(or just run the program the first time and the folder will be created for you)")
    print("2. Put all the files you want to organise inside the 'Misc' folder")
    print("3. Execute the script")
    print("4. Enjoy the tidy result\n")

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
    #Logo print
    logo_print()

    #Asking user input
    print("Choose an option")
    while True:
        print("\n")
        print("i - See Instructions")
        print("o - Organise files in folder 'Misc'")
        print("q - Quit program")
        usr_option = input("option: ").lower()
        if usr_option == "q":
            sys.exit()
        elif usr_option == "i":
            show_instructions()
            time.sleep(0.3)
            print("Choose an option")
        elif usr_option == "o":
            break
        else:
            print("Wrong choice...please select one of the following options:")

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
    print("=" * 11)
    print(" S T A T S")
    print("=" * 11)
    time.sleep(0.2)
    print(f"Processed a total of {file_tot} files")
    for f in folders:
        if f != "passed":
            time.sleep(0.2)
            print(f" # {folders[f]} file(s) moved in folder {f}")

    if "passed" in folders.keys():
        time.sleep(0.2)
        print(f"WARNING! # {folders['passed']} file(s) left unmoved...")

    time.sleep(0.2)
    print("\nBye! :)\n")
