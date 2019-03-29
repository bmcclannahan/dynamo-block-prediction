from input import get_feed_forward_input_array
from keras.models import Sequential
from keras.layers import Dense
import numpy

input_array, output_array = get_feed_forward_input_array('../Features/features.txt')
#print(output_array)

model = Sequential()
model.add(Dense(units=32,activation='relu',input_dim=56))
model.add(Dense(units=1,activation='sigmoid'))
model.compile(loss='binary_crossentropy',optimizer='sgd',metrics=['accuracy'])
model.fit(input_array, output_array, epochs=100, batch_size=32)