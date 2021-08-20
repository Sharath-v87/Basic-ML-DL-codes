
from os import listdir
import shutil
# seed random number generator
from random import seed
from random import random
seed(1)
# define ratio of pictures to use for validation
val_ratio = 0.25
# copy training dataset images into subdirectories
src_directory = 'enter your data set path here'
for file in listdir(src_directory):
	src = src_directory + file 
	dst_dir = 'train/'
	if random() < val_ratio:
		dst_dir = 'test/'
	if file.startswith('Cat'):
		dst = 'dataset_dogs_vs_cats/' + dst_dir + 'cats/'  + file
		shutil.copyfile(src, dst)
	elif file.startswith('Dog'):
		dst = 'dataset_dogs_vs_cats/' + dst_dir + 'dogs/'  + file
		shutil.copyfile(src, dst)