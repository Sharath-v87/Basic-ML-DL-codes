from os import makedirs
dataset_home = 'enter you dataset path here'
subdirs = ['train/', 'test/']
for subdir in subdirs:
	# create label subdirectories
	
	labeldirs = ['dogs/', 'cats/']
	for labldir in labeldirs:
		newdir = dataset_home + subdir + labldir
		makedirs(newdir, exist_ok=True)
		print (newdir)