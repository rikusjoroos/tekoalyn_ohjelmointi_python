# -*- coding: utf-8 -*-

from keras.datasets import mnist
from keras.utils import np_utils
from keras.models import Sequential
from keras.layers import Dense

batch_size = 128

num_classes = 10
epochs = 8
(x_train, y_train), (x_test, y_test) = mnist.load_data()

x_train = x_train.reshape(60000, 784)
x_test = x_test.reshape(10000, 784)
x_train = x_train.astype('float32')
x_test = x_test.astype('float32')
x_train /= 255
x_test /= 255

print(x_train.shape[0], 'train samples')
print(x_test.shape[0], 'test samples')

y_train = np_utils.to_categorical(y_train, num_classes)
y_test = np_utils.to_categorical(y_test, num_classes)

model = Sequential()

model.add(Dense(512, activation = 'relu', input_shape = (784,)))

model.add(Dense(512, activation = 'relu'))
model.add(Dense(num_classes, activation = 'softmax'))

model.summary()

model.compile(loss = 'categorical_crossentropy', metrics = ['accuracy'], optimizer = 'adam')

history = model.fit(
    x_train, y_train,
    batch_size = batch_size,
    epochs = epochs,
    verbose = 1,
    validation_data = (x_test, y_test)
    )

score = model.evaluate(x_test, y_test, verbose = 0)

print('Test loss:', score[0])
print('Test accuracy:', score[1])





