import sys
import os
import shutil
import send2trash

# Store every drive connected on PC in a list
drives = [chr(x) + ':' for x in range(65, 90) if os.path.exists(chr(x) + ':')]


# List each files/folders in the correct working directory
def list_directories():
    listdir = os.listdir(os.getcwd())
    for components in listdir:
        print('|-' + components)


# Select driver that files or folder you need
def choice_driver():
    print('\n Chose drive:')

    print('Drives: ')
    for x in range(len(drives)):
        print(drives[x])

    while True:
        inp = input("\nEnter your Choice: ")

        if inp in drives:
            os.chdir(inp + '\\')
            break

        else:
            print('Error\nEnter a correct drive name.\n')


# Open file/folders
def open_component():
    choice_driver()

    while True:
        list_directories()

        res = input('\nChoose a file/folder: ')
        print('\n')

        if res in os.listdir(os.getcwd()):
            if os.path.isfile(res):
                os.system('"' + res + '"')
            else:
                os.chdir(res)
        else:
            print('\nNo file/folder with this name')


# Rename files
def rename():
    choice_driver()

    while True:
        list_directories()
        res = input('\nChoose a file/folder: ')
        print('\n')

        if res in os.listdir(os.getcwd()):
            if os.path.isfile(res):
                print('Chosen file:', res)
                res_name, res_ext = os.path.splitext(res)
                new_title = input('Enter new file name:')
                new_file_name = '{}{}'.format(new_title, res_ext)
                os.rename(res, new_file_name)
            if os.path.isdir(res):
                print('Chosen folder:', res)
                new_folder_name = input('Enter new folder name:')
                os.rename(res, new_folder_name)


if __name__ == '__main__':
    print(drives)
    rename()
