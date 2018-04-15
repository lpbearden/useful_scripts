"""
Rename tv episode files by digits in filename, i.e. 2.1 would become: Show Name - S02E01.ext
path should be: /path/to/folder/TV Show
Where directory structure is this (seasons must be 2 digits):
TV Show
  | Season 01
  | Season 02
  | Season 03

Tested fixing following formats:
    s.e
    s.ee
    ss.ee
    se
    see
    ssee
    some text ss some text ee (season and episode must be first 4 digits)

To do one folder at a time change path directly to folder, and use the below loop instead
of the nested loop.
    for filename in os.listdir(path):
        # do work

ALWAYS TEST WITH THE PRINT METHODS BEFORE RENAMING
"""
import os
import re


def get_formatted_number(filename):
    episode_numbers = re.findall('\d', filename)

    if len(episode_numbers) > 4:
        episode_numbers = [episode_numbers[0], episode_numbers[1], episode_numbers[2], episode_numbers[3]]
    if len(episode_numbers) == 4:
        return 'S' + episode_numbers[0] + episode_numbers[1] + 'E' + episode_numbers[2] + episode_numbers[3] 
    elif len(episode_numbers) == 3:
        return 'S0' + episode_numbers[0] + 'E' + episode_numbers[1] + episode_numbers[2]
    elif len(episode_numbers) == 2:
        return 'S0' + episode_numbers[0] + 'E0' + episode_numbers[1]
    else:
        return "Error: The entered format is not supported, filename: " + filename


path = 'C://Users/FN-2187/Desktop/Dragon Ball/'
show_name = 'Dragon Ball'
file_extension = '.mkv'


for root, dirs, files in os.walk(path):
    for filename in files:
        if filename.endswith(".mkv"):
            formatted_number = get_formatted_number(filename)
            if 'Error' in formatted_number:
                print(filename + ' is not in an acceptable format, skipping.')
            else:
                new_name = show_name + ' - ' + formatted_number + file_extension
                print('Renaming ' + filename + ' ---> ' + new_name)
                full_path = path + 'Season ' + formatted_number[1] + formatted_number[2] + '/'
                os.rename(os.path.join(full_path, filename), os.path.join(full_path, new_name))