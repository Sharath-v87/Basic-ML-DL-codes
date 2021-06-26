from os import listdir
from numpy import asarray
from numpy import save

from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
# define location of dataset
folder = 'enter your data set path here'
photos, labels = list(), list()
# enumerate files in the directory
i = 0
for fil in listdir(folder):
    # determine class
    output = 0.0
    
    if fil.startswith('Cat'):
    	output = 1.0
	# load image
    photo = load_img(folder + fil, target_size=(200, 200))
    
	# convert to numpy array
    photo = img_to_array(photo)
	# store
    photos.append(photo)
    labels.append(output)
# convert to a numpy arrays
photos = asarray(photos)
labels = asarray(labels)
print(photos.shape, labels.shape)
# save the reshaped photos
save('dogs_vs_cats_photos.npy', photos)
save('dogs_vs_cats_labels.npy', labels)

from numpy import load
photos = load('dogs_vs_cats_photos.npy')
labels = load('dogs_vs_cats_labels.npy')
print(photos.shape, labels.shape)

# dataset_home = 'dataset_dogs_vs_cats/'
# subdirs = ['train/', 'test/']
# for subdir in subdirs:
# 	# create label subdirectories
# 	labeldirs = ['dogs/', 'cats/']
# 	for labldir in labeldirs:
# 		newdir = dataset_home + subdir + labldir
# 		makedirs(newdir, exist_ok=True)