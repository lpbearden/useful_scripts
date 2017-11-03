import os
import re

path = 'F://Video/MKVs/Done/Season 03'
files = os.listdir(path)
myFileName = "Boardwalk Empire - S03E"

print(files)
regex = '\d*'
p = re.compile(regex)

for file in files:
	m = p.search(file)
	print(m.group())
	if int(m.group()) < 10:
		print(myFileName + '0'+ str(m.group()) +' Episode ' + file)
		os.rename(os.path.join(path, file), os.path.join(path, myFileName + '0'+ str(m.group()) +' Episode ' + file))
	else:
		print(myFileName + str(m.group()) +' Episode ' + file)
		os.rename(os.path.join(path, file), os.path.join(path, myFileName + str(m.group()) +' Episode ' + file))

