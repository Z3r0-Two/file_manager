import sys
import os
import shutil
from send2trash import send2trash

# Store every drive connected on PC in a list
drives = [chr(x) + ':' for x in range(65, 90) if os.path.exists(chr(x) + ':')]


def choice_driver():
    # Select driver that files or folder you need
    print('\nChoose drive:')

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


def open_component(comp):
    # Open file/folders
    if comp in os.listdir(os.getcwd()):
        if os.path.isfile(comp):
            os.system('"' + comp + '"')
        else:
            os.chdir(comp)
    else:
        print('\nNo file/folder with this name')


def rename(comp):
    # Rename files
    if comp in os.listdir(os.getcwd()):
        if os.path.isfile(comp):
            comp_name, comp_ext = os.path.splitext(comp)
            new_title = input('Enter new file name:')
            new_file_name = '{}{}'.format(new_title, comp_ext)
            os.rename(comp, new_file_name)
        if os.path.isdir(comp):
            new_folder_name = input('Enter new folder name:')
            os.rename(comp, new_folder_name)


def move_component(comp):
    # Move files/folders
    """
    We check does is the selected component file or folder
    Next we select in what drive or folder we want to move file/folder
    """
    if comp in os.listdir(os.getcwd()):
        if os.path.isfile(comp):
            file_path = os.getcwd() + '\\' + comp
            print('\nChosen file path:', file_path)

            while True:
                print('\nDrives:')
                for x in range(len(drives)):
                    print(drives[x])

                sel2 = input('\nChoose drive: ')
                if sel2 in drives:
                    os.chdir(sel2 + '\\')
                    drive_path = sel2 + '\\'
                    print(drive_path)
                    break
                else:
                    print('\nEnter correct drive name')

            while True:
                print('\nMove component into drive?')
                ans = input('\nY/N: ')
                if ans == 'Y':
                    shutil.move(file_path, drive_path)
                    break
                elif ans == 'N':
                    for files in os.listdir(os.getcwd()):
                        print('|-' + files)

                    folder = input('\nChoose folder: ')
                    if folder in os.listdir(os.getcwd()):
                        if os.path.isdir(folder):
                            folder_path = os.getcwd() + '\\' + folder
                        else:
                            print('\nPlease, select a folder')

                    print('\nMove file into this directory', folder_path, '?')
                    move = input('\nY/N: ')
                    if move == 'Y':
                        shutil.move(file_path, folder_path)
                        break
                    elif move == 'N':
                        os.chdir(sel2)
                    else:
                        print('\nPlease enter Y/N')

        elif os.path.isdir(comp):
            move_folder_path = os.getcwd() + '\\' + comp
            print('Moving folder path:', move_folder_path)

            while True:
                print('\nDrives:')
                for x in range(len(drives)):
                    print(drives[x])

                sel2 = input('\nChoose drive: ')
                if sel2 in drives:
                    os.chdir(sel2 + '\\')
                    drive_path = sel2 + '\\'
                    print(drive_path)
                    break
                else:
                    print('\nEnter correct drive name')

            while True:
                print('\nMove component into drive?')
                ans = input('\nY/N: ')
                if ans == 'Y':
                    shutil.move(move_folder_path, drive_path)
                    break
                elif ans == 'N':
                    for files in os.listdir(os.getcwd()):
                        print('|-' + files)
                    folder = input('\nChoose folder: ')

                    if folder in os.listdir(os.getcwd()):
                        if os.path.isdir(folder):
                            folder_path = os.getcwd() + '\\' + folder
                        else:
                            print('\nPlease, select a folder!')

                    print('\nMove file into this directory', folder_path, '?')
                    move = input('\nY/N:')
                    if move == 'Y':
                        shutil.move(move_folder_path, folder_path)
                        break
                    elif move == 'N':
                        os.chdir(sel2)
                    else:
                        print('\nPlease enter Y/N')


def copy_component(comp):
    if comp in os.listdir(os.getcwd()):
        if os.path.isfile(comp):
            file_path = os.getcwd() + '\\' + comp
            print('\nChosen file path:', file_path)

            while True:
                print('\nDrives:')
                for x in range(len(drives)):
                    print(drives[x])

                sel2 = input('\nChoose drive: ')
                if sel2 in drives:
                    os.chdir(sel2 + '\\')
                    drive_path = sel2 + '\\'
                    print(drive_path)
                    break
                else:
                    print('\nEnter correct drive name')

            while True:
                print('\nCopy component into drive?')
                ans = input('\nY/N: ')
                if ans == 'Y':
                    shutil.copy(file_path, drive_path)
                    break
                elif ans == 'N':
                    for files in os.listdir(os.getcwd()):
                        print('|-' + files)

                    folder = input('\nChoose folder: ')
                    if folder in os.listdir(os.getcwd()):
                        if os.path.isdir(folder):
                            folder_path = os.getcwd() + '\\' + folder
                        else:
                            print('\nPlease, select a folder')

                    print('\nCopy file into this directory', folder_path, '?')
                    move = input('\nY/N: ')
                    if move == 'Y':
                        shutil.copy(file_path, folder_path)
                        break
                    elif move == 'N':
                        os.chdir(sel2)
                    else:
                        print('\nPlease enter Y/N')

        elif os.path.isdir(comp):
            move_folder_path = os.getcwd() + comp
            print('Copy folder path:', move_folder_path)

            while True:
                print('\nDrives:')
                for x in range(len(drives)):
                    print(drives[x])

                sel2 = input('\nChoose drive: ')
                if sel2 in drives:
                    os.chdir(sel2 + '\\')
                    drive_path = sel2 + '\\'
                    print(drive_path)
                    break
                else:
                    print('\nEnter correct drive name')

            while True:
                print('\nCopy component into drive?')
                ans = input('\nY/N: ')
                if ans == 'Y':
                    shutil.copytree(move_folder_path, drive_path)
                    break
                elif ans == 'N':
                    for files in os.listdir(os.getcwd()):
                        print('|-' + files)
                    folder = input('\nChoose folder: ')

                    if folder in os.listdir(os.getcwd()):
                        if os.path.isdir(folder):
                            folder_path = os.getcwd() + folder
                        else:
                            print('\nPlease, select a folder!')

                    print('\nCopy file into this directory', folder_path, '?')
                    move = input('\nY/N:')
                    if move == 'Y':
                        shutil.copytree(move_folder_path, folder_path)
                        break
                    elif move == 'N':
                        os.chdir(sel2)
                    else:
                        print('\nPlease enter Y/N')


def send_to_trash(comp):
    if comp in os.listdir(os.getcwd()):
        if os.path.isfile(comp):
            ans = input('Send this file to trash?')
            if ans == 'Y':
                send2trash(comp)
            if ans == 'N':
                os.chdir('..')
        if os.path.isdir(comp):
            ans = input('Send this directory to trash?')
            if ans == 'Y':
                send2trash(comp)
            if ans == 'N':
                os.chdir('..')


def delete_component(comp):
    if comp in os.listdir(os.getcwd()):
        if os.path.isfile(comp):
            ans = input('Delete this file?')
            if ans == 'Y':
                os.remove(comp)
            if ans == 'N':
                os.chdir('..')
        if os.path.isdir(comp):
            ans = input('Delete this folder?')
            if ans == 'Y':
                shutil.rmtree(comp)
            if ans == 'N':
                os.chdir('..')


if __name__ == '__main__':
    choice_driver()

    while True:
        for file_list in os.listdir(os.getcwd()):
            print('|-' + file_list)

        file = input('Choose file: ')
        delete_component(file)

