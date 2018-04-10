import os


def get_digits(str1):
	count = 0
	c = ""
	for i in str1:
		if i.isdigit():
			if count < 1:
				count+=1
				continue
			else:
				count+=1
				c += i
	return c

path = '//FN-SCOUT\Television\Dragon Ball\Season 06'
files = os.listdir(path)
myFileName = "Dragon Ball - S06E"
# files.sort(key=lambda x: os.stat(os.path.join(path, x)).st_mtime)
files.sort()

for file in files:
    print(file)
    # print(myFileName+get_digits(file)+'.mkv')

i = 1

for file in files:
# 	os.rename(os.path.join(path, file), os.path.join(path, myFileName+get_digits(file)+'.mkv'))
	if (i >= 10):
		os.rename(os.path.join(path, file), os.path.join(path, myFileName + str(i) + '.mkv'))
	else:    	
		os.rename(os.path.join(path, file), os.path.join(path, myFileName + "0" + str(i) + '.mkv'))
	i = i+1

