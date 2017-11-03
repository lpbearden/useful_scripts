import os


path = 'F://Video/MKVs/Boardwalk Empire/Season 1'
files = os.listdir(path)
myFileName = "Boardwalk Empire - S01E"
files.sort(key=lambda x: os.stat(os.path.join(path, x)).st_mtime)

print(files)

i = 1

for file in files:
	if (i >= 10):
		os.rename(os.path.join(path, file), os.path.join(path, myFileName + str(i) +' Episode ' + str(i) + '.mkv'))
	else:    	
		os.rename(os.path.join(path, file), os.path.join(path, myFileName + "0" + str(i) +' Episode ' + str(i) + '.mkv'))
	i = i+1

