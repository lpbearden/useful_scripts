import os, sys
from pathlib import Path

location = input("Show location: ")
working_dir = Path(location)
if not working_dir.is_dir():
    print("The location entered is not a directory.")
    sys.exit(0)

show_name = input("Show name: ")
season_num = int(input("Season #: "))

if season_num > 9:
    season_str = str(season_num)
else:
    season_str = f"0{season_num}"

print(f"Converting episodes found in {location}, for season {season_str} of {show_name}.")
confirm = input("Would you like to proceed? [Y/N] ").upper()

if not confirm == 'Y':
    print("Confirm input was not Y, exiting.")
    sys.exit(0)


count = 1
for file in os.listdir(working_dir):
    if count < 10:
        print(f"Renaming {file} --> {show_name} - S{season_str}E0{count}.mkv")
        os.rename(working_dir.joinpath(file), working_dir.joinpath(f"{show_name} - S{season_str}E0{count}.mkv"))
    else:
        print(f"Renaming {file} --> {show_name} - S{season_str}E{count}.mkv")
        os.rename(working_dir.joinpath(file), working_dir.joinpath(f"{show_name} - S{season_str}E{count}.mkv"))
    count = count + 1
