import numpy as np
import imageio 
from keras.models import load_model

ip = imageio.imread('/Users/sharath/Desktop/random models/OCR/five.png')
bandw = np.dot(ip[...,:3],[0.2989, 0.5870, 0.1140])
bandw = (bandw.reshape(1,28,28,1))/255

model = load_model('/Users/sharath/Desktop/random models/OCR/ocr.h5')

output = model.predict(bandw)
print(output.argmax())