# Print contents of a directory using os module 

import os

# path of directory (you can change it)
path = 'your/path/directory'

# list all files and folders
files = os.listdir(path)

# print each file/folder
for file in files:
    print(file) 