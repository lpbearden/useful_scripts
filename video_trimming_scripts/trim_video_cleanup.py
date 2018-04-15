""" 
This script is used to trim up the extra characters added by the shell scripts
that do the video trimming. 
    i.e. Vikings - S01E01f.mp4 ---> Vikings - S01e01.mp4
"""
import os

path = 'C://Users/FN-2187/Desktop/Dragon Ball/Season 01'
file_extension = '.mp4'
files = os.listdir(path)

for file in files:
        filename = file[:-5]
        os.rename(os.path.join(path, file), os.path.join(path, filename + file_extension))