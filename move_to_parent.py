
import fnmatch
import os
import shutil

rootPath = 'F://Video//MKVs'
destDir = 'F://Video/MKVs'


matches = []
for root, dirnames, filenames in os.walk(rootPath):
	for filename in filenames:
		matches.append(os.path.join(root, filename))
		print(os.path.join(root, filename))
		shutil.move(os.path.join(root, filename), os.path.join(destDir, filename))