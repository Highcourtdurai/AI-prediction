import tensorflow as tf
from tensorflow import keras
from keras.models import Sequential
from keras.layers import Dense,Flatten,Conv2D,MaxPool2D,Dropout
from tensorflow.keras import layers
from keras.utils import to_categorical
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')
from keras.datasets import cifar10

(xtrain,ytrain),(xtest,ytest)=cifar10.load_data()

#check type of the train and test
print(type(xtrain))

print(xtrain.shape)

#look a first image in array
xtrain[10]#0 to 255

img=plt.imshow(xtrain[100])

#get image label

lab1=ytrain[100]
print(lab1)

classification=['airplane','automobile','bird','cat','deer','dog','frog','horse','ship','truck']

print('image class is:',classification[ytrain[100][0]])

#Change the label into set of numbers [10]
ytrain_one_hot=to_categorical(ytrain)
ytest_one_hot=to_categorical(ytest)

ytest_one_hot[100] #000100000 #000100000

#Normalize the pixels values
xtrain=xtrain/255
xtest=xtest/255

#create the architecture
model=Sequential()
#first conv layer
model.add(Conv2D(32,(5,5),activation='relu',input_shape=(32,32,3)))
#pooling layer
model.add(Maxpool2D(pool_size=(2,2))
#second conv layer
model.add(Conv2D(32,(5,5),activation='relu'))
#pooling layer two
model.add(MaxPool2D(pool_size=(2,2)))

#flattening layer
model.add(Flatten())

#add a layer
model.add(Dense(1000,activation='relu'))
#add Dropout layer
model.add(Dropout(0.5))

#add a layer
model.add(Dense(500,activation='relu'))

#add Dropout layer
model.add(Dropout(0.5))

#add a layer
model.add(Dense(250,activation='relu'))

#add a layer
model.add(Dense(10,activation='softmax'))

model.summary()

#Back propagation

model.compile(loss='categorical_crossentropy',optimizer='adam',metrics=['accuracy'])

tr=model.fit(xtrain,ytrain_one_hot,batch_size=256,epochs=1,validation_split=0.2)

model.evaluate(xtest,ytest_one_hot)

dog=plt.imread('dog.jpg')
img=plt.imshow(dog)

#resize the image
#pip install scikit-image
from skimage import transform

resize=transform.resize(dog,(32,32,3))

img=plt.imshow(resize)

prediction=model.predict(np.array([resize]))
print(prediction)

list_index=[0,1,2,3,4,5,6,7,8,9]
x=prediction
for i in range(10):
    for j in range(10):
        if x[0][list_index[i]]>x[0][list_index[j]]:
            temp=list_index[i]
            list_index[i]=list_index[j]
            list_index[j]=temp
print(list_index)

for i in range(5):
    print(classification[list_index[i]])
    