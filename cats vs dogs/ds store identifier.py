#This code is for mac users inorder to find if there are ds store files so that they could remove it
from os import listdir
folder = 'enter your dataset path'
fils=listdir(folder)
for i in range(len(fils)):
    name=fils[i]
    print(name)
    ext=name.split('.')[1]
    if ext != 'jpg' :
        print(name) 