from keras.datasets import mnist
from keras.layers.convolutional import Conv
from keras.layers import Dense, Dropout, Flatten
from keras.layers.pooling import MaxPooling2D
from tensorflow.keras.utils import to_categorical
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D

(xtrain,ytrain),(xtest,ytest)=mnist.load_data()

xtrain = (xtrain.reshape(xtrain.shape[0],28,28,1))/255
xtest = (xtest.reshape(xtest.shape[0],28,28,1))/255
classes = 10
ytrain= to_categorical(ytrain,classes)
ytest= to_categorical(ytest,classes)

model = Sequential() 
model.add(Conv2D(32,kernel_size=(3,3),activation='relu',input_shape=(28,28,1)))
model.add(Conv2D(64,kernel_size=(3,3),activation='relu'))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Dropout(0.25))
model.add(Flatten())
model.add(Dense(128,activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(classes,activation='softmax'))

model.compile(loss='categorical_crossentropy',optimizer = 'adam', metrics = ['accuracy'])

model.fit(xtrain, ytrain, batch_size=128, epochs=10, verbose=1, validation_data=(xtest, ytest))
eval=model.evaluate(xtest,ytest,verbose=0)
print('test loss ',eval[0])
print('accuracy ',eval[1])
model.save("ocr.h5")
