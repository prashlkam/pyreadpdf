import os

path = 'c:\\projects\\hc2\\'
def lsdir (path):
	files = []
	# r=root, d=directories, f = files
	for r, d, f in os.walk(path):
		for file in f:
			if '.pdf' in file:
				files.append(os.path.join(r, file))
	for f in files:
		print(f)
	return files
