import os
import shutil

path = cwd = os.getcwd() + '/'
print(path)
files = os.listdir(path)
used = []
for file in files:
    if file  ==  'file_manager.py':
        pass
    else:
        if '.' in file:
            print(file)
            folder = file.split('.')[-1]
            if folder not in used and folder not in files :
                os.mkdir(path + folder)
                used.append(folder)
            shutil.move(path + file , path + folder + '/' +file)
