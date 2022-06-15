# -*- coding: utf-8 -*-
"""Image_classificaton_Simple_MNIST_convnet.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1KvG3mIMMUl0u85-ZTfrDabMyGgvzPCmi

# Simple MNISt convnet
"""

import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

"""# Prepare the data"""

num_classes = 10
input_shape = (28,28,1)

# the data, split between train and test sets
(x_train, y_train),(x_test, y_test) = keras.datasets.mnist.load_data()

# scaling images to [0-] range
x_train = x_train.astype("float32") / 255
x_test = x_test.astype("float32") / 255

# make sure images have shape (28,28,1)
x_train = np.expand_dims(x_train, -1)
x_test = np.expand_dims(x_test, -1)
print("x_train shape:", x_train.shape)
print(x_train.shape[0],"train samples")
print(x_test.shape[0],"test samples")

# convert class vectors to binary class matrics
y_train = keras.utils.to_categorical(y_train,num_classes)
y_test = keras.utils.to_categorical(y_test, num_classes)

"""# Building the Model"""

model = keras.Sequential(
    [
     keras.Input(shape= input_shape),
     layers.Conv2D(32,kernel_size=(3,3), activation="relu"),
     layers.MaxPool2D(pool_size=(2,2)),
     layers.Conv2D(64,(3,3),activation="relu"),
     layers.MaxPool2D((2,2)),
     layers.Flatten(),
     layers.Dropout(0.5),
     layers.Dense(num_clases, activation="softmax"),
    ]
)
model.summary()

"""# Train the model"""

batch_size = 128
epochs = 50
model.compile(loss = "categorical_crossentropy", optimizer = 'adam', metrics = ["accuracy"])

from tensorflow.python.ops.gen_batch_ops import batch
model.fit(x_train, y_train, batch_size = batch_size, epochs = epochs, validation_split=0.1)

"""# Evaluate the trained Model"""

score = model.evaluate(x_test,y_test, verbose = 0)
print("Test loss: ", score[0])
print("Test accuracy: ", score[1])