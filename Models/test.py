from keras.models import Sequential
from keras.layers import Dense, SimpleRNN, LSTM
import numpy

input_array = [[[1],[1]],[[1],[2]],[[2],[3]],[[3],[5]],[[5],[8]],[[8],[13]],[[13],[21]]]
output_array = [[[0],[1]],[[1],[1]],[[1],[0]],[[0],[1]],[[1],[1]],[[1],[0]],[[0],[1]]]

model = Sequential()
model.add(SimpleRNN(units=1, return_sequences=True, input_shape=(2,1)))
model.add(Dense(units=1,activation='sigmoid'))
model.compile(loss='binary_crossentropy',optimizer='sgd',metrics=['accuracy'])

model.fit(numpy.array(input_array), numpy.array(output_array), epochs=10)
