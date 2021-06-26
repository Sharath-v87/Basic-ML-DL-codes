from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from keras.models import load_model

def load_image(filename):
	# load the image
	img = load_img(filename, target_size=(200, 200))
	# convert to array
	img = img_to_array(img)
	# reshape into a single sample with 3 channels
	img = img.reshape(1, 200, 200, 3)
	# center pixel data
	img = img.astype('float32')
	img = img - [123.68, 116.779, 103.939]
	return img

def run_example():
    # load the image
    img = load_image('/Users/sharath/Desktop/dog5test.png')
    # load model
    model = load_model('/Users/sharath/Desktop/kewk/initialmodel.h5')
    # predict the class
    result = model.predict(img)
    if result[0] == 1:
        print('-------- DETECTED AS DOG ----------')
    else :
        print('-------- DETECTED AS CAT ----------')
    print(result[0])

run_example() 