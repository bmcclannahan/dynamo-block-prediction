from input import get_simple_feed_forward_input_array, build_input_from_multiple_files
from keras.models import Sequential
from keras.layers import Dense, Dropout
import numpy
import os

input_files = ['Feature_Files/'+ f for f in os.listdir('Feature_Files')]
input_array, output_array = build_input_from_multiple_files(input_files,get_simple_feed_forward_input_array)
print(len(output_array))

model = Sequential()
model.add(Dense(units=12,activation='relu',input_dim=12))
model.add(Dropout(rate=.3))
model.add(Dense(units=8,activation='relu'))
model.add(Dropout(rate=.2))
model.add(Dense(units=1,activation='sigmoid'))
model.compile(loss='binary_crossentropy',optimizer='sgd',metrics=['accuracy'])
model.fit(input_array, output_array, epochs=100, validation_split=.3, batch_size=32)
