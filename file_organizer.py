import os, shutil

path= input("Enter path: ")
files=os.listdir(path)
"""print (files)"""

for file in files:
    filename,extension=os.path.splitext(file)
