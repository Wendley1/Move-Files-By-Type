import os
import shutil

main_folder = input('Enter main folder: ')
destine_folder = input('Enter destine folder: ')
file = input('Enter File Type: ')
copy_or_move = input('Copy Files (y/n): ')

fileType = '.' + file

if copy_or_move.lower() in ('s', 'y'):
    copyFiles = True
elif copy_or_move.lower() in ('n'):
    copyFiles = False
else:
    print('Invalid input, defaulting to move files')
    copyFiles = False

count = 0

print('Started')

try:
    for foldername, subfolders, filenames in os.walk(main_folder):
        for filename in filenames:
            if filename.endswith(fileType):
                filepath = os.path.join(foldername, filename)
                if copyFiles:
                    shutil.copy(filepath, destine_folder)
                else:
                    shutil.move(filepath, destine_folder)
                count += 1
    if copyFiles:
        print('File type:', fileType, 'copied:', count)
    else:
        print('File type:', fileType, 'moved:', count)
    print('Done')
except FileNotFoundError:
    print('Invalid folder path!')
