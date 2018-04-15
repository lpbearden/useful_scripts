"""
Script used to rename files based on their last modified time.
Best used one season at a time.
"""
import os

path = 'C://Users/FN-2187/Desktop/Dragon Ball/Season 01'
show_name = 'Dragon Ball - S01'
file_extension = '.mkv'
files = os.listdir(path)

# sort files by last modified time
files.sort(key=lambda x: os.stat(os.path.join(path, x)).st_mtime)

i = 1
for filename in files:
	print(filename)
    if i < 10:
        os.rename(os.path.join(path, filename), os.path.join(path, show_name + "0" + str(i) + '.mkv'))
    else:        
        os.rename(os.path.join(path, filename), os.path.join(path, show_name + str(i) + '.mkv'))
    i = i+1

