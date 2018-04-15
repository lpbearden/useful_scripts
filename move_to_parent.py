"""
Script to move all files below the rootPath to the destPath, does not move directories.
"""

import os
import shutil

rootPath = 'C://Users/FN-2187/Desktop/Dragon Ball'
destPath = 'C://Users/FN-2187/Desktop/Dragon Ball'

for folderName, subfolders, filenames in os.walk(rootPath):
    print('The current folder is ' + folderName)

    for filename in filenames:
        print('Moving: ' + os.path.join(folderName, filename) + ' ----> ' + os.path.join(destPath, filename))
        shutil.move(os.path.join(folderName, filename), os.path.join(destPath, filename))