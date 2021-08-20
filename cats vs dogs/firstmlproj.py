import numpy as np
import pandas as pd
from keras.preprocessing.image import ImageDataGenerator,load_img
from keras.utils.np_utils import to_categorical
from sklearn.model_selection import train_test_split
#import matplotlib.pyplot as plt
import random
import os

Image_Width=128
Image_Height=128
Image_Size=(Image_Width,Image_Height)
Image_Channels=3

filenames=os.listdir("enter your dataset path here")
print(filenames)
categories=[]
for f_name in filenames:
    category=f_name.split('.')[0]
    if category=='Dog':
        categories.append(1)
    else:
        categories.append(0)

df=pd.DataFrame({
    'filename':filenames,
    'category':categories
})
print(categories)
from keras.models import Sequential
from keras.layers import Conv2D,MaxPooling2D,\
     Dropout,Flatten,Dense,Activation,\
     BatchNormalization

model=Sequential()

model.add(Conv2D(32,(3,3),activation='relu',input_shape=(Image_Width,Image_Height,Image_Channels)))
model.add(BatchNormalization())
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Dropout(0.25))

model.add(Conv2D(64,(3,3),activation='relu'))
model.add(BatchNormalization())
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Dropout(0.25))

model.add(Conv2D(128,(3,3),activation='relu'))
model.add(BatchNormalization())
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Dropout(0.25))

model.add(Flatten())
model.add(Dense(512,activation='relu'))
model.add(BatchNormalization())
model.add(Dropout(0.5))
model.add(Dense(2,activation='softmax'))

model.compile(loss='categorical_crossentropy',
  optimizer='rmsprop',metrics=['accuracy'])

model.summary()

from keras.callbacks import EarlyStopping, ReduceLROnPlateau
earlystop = EarlyStopping(patience = 10)
learning_rate_reduction = ReduceLROnPlateau(monitor = 'val_acc',patience = 2,verbose = 1,factor = 0.5,min_lr = 0.00001)
callbacks = [earlystop,learning_rate_reduction]

# df["category"] = df["category"].replace({0:'cat',1:'dog'})
# train_df,validate_df = train_test_split(df,test_size=0.20,
#   random_state=42)
# print(df)












#--------------------F-----------------------

















# train_df = train_df.reset_index(drop=True)
# validate_df = validate_df.reset_index(drop=True)

# total_train=train_df.shape[0]
# total_validate=validate_df.shape[0]
# batch_size=15

# train_datagen = ImageDataGenerator(rotation_range=15,
#                                 rescale=1./255,
#                                 shear_range=0.1,
#                                 zoom_range=0.2,
#                                 horizontal_flip=True,
#                                 width_shift_range=0.1,
#                                 height_shift_range=0.1
#                                 )

# train_generator = train_datagen.flow_from_dataframe(train_df,
#                                                  "./dogs-vs-cats/train/",x_col='filename',y_col='category',
#                                                  target_size=Image_Size,
#                                                  class_mode='categorical',
#                                                  batch_size=batch_size)

# validation_datagen = ImageDataGenerator(rescale=1./255)
# validation_generator = validation_datagen.flow_from_dataframe(
#     validate_df, 
#     "./dogs-vs-cats/train/", 
#     x_col='filename',
#     y_col='category',
#     target_size=Image_Size,
#     class_mode='categorical',
#     batch_size=batch_size
# )

# test_datagen = ImageDataGenerator(rotation_range=15,
#                                 rescale=1./255,
#                                 shear_range=0.1,
#                                 zoom_range=0.2,
#                                 horizontal_flip=True,
#                                 width_shift_range=0.1,
#                                 height_shift_range=0.1)

# test_generator = train_datagen.flow_from_dataframe(train_df,
#                                                  "./dogs-vs-cats/test/",x_col='filename',y_col='category',
#                                                  target_size=Image_Size,
#                                                  class_mode='categorical',
#                                                  batch_size=batch_size)

# epochs=10
# history = model.fit_generator(
#     train_generator, 
#     epochs=epochs,
#     validation_data=validation_generator,
#     validation_steps=total_validate//batch_size,
#     steps_per_epoch=total_train//batch_size,
#     callbacks=callbacks
# )