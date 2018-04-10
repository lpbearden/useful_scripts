import os

path = '//FN-SCOUT\Television\The Expanse\Season 1'
files = os.listdir(path)

for file in files:
		filename = file[:-5]
		print(filename)
		os.rename(os.path.join(path, file), os.path.join(path, filename+'.mkv'))