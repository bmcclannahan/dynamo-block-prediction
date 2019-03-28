from input import get_recurrent_input_array, get_recurrent_three_input_array
from keras.models import Sequential
from keras.layers import Dense, SimpleRNN, LSTM
import numpy as np

input_array, output_array = get_recurrent_three_input_array('../Features/features.txt')
#print(input_array[0])
#print(output_array)

model = Sequential()
model.add(SimpleRNN(units=10, return_sequences=True, input_shape=(3,56)))
model.add(Dense(units=1,activation='sigmoid'))
model.compile(loss='binary_crossentropy',optimizer='sgd',metrics=['accuracy'])

print(np.shape(input_array))
model.fit(np.array(input_array), np.array(output_array), epochs=10)
print(model.evaluate(np.array([input_array[0]]), np.array([output_array[0]])))
