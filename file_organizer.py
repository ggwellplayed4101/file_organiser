import os, shutil

path= input("Enter path: ")
files=os.listdir(path)   #listing files in the given path

for file in files:
    filename,extension=os.path.splitext(file)    #seperating path and extension in 
    extension=extension[1:]

    if os.path.exists(path+"/"+extension):     #checks if there is a folder for a type of extension
        shutil.move(path+"/"+file, path+"/"+extension+"/"+file)    #changes directory of the file
    
    else:
        os.makedirs(path+"/"+extension)        #makes an folder for the type of extension
        shutil.move(path+"/"+file, path+"/"+extension+"/"+file)     #changes directory of the file
