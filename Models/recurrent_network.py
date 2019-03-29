from input import get_recurrent_input_array, get_recurrent_three_input_array
#from keras.models import Sequential
#from keras.layers import Dense, SimpleRNN, LSTM
import numpy as np

input_array, output_array = get_recurrent_three_input_array('../Features/features.txt', 442)
input_array2, output_array2 = get_recurrent_three_input_array('../Features/features2.txt', 598)
print(len(input_array2))
print(len(output_array2))

model = Sequential()
model.add(SimpleRNN(units=10, return_sequences=True, input_shape=(3,67)))
model.add(Dense(units=1,activation='sigmoid'))
model.compile(loss='binary_crossentropy',optimizer='sgd',metrics=['accuracy'])

print(np.shape(input_array))
model.fit(np.array(input_array), np.array(output_array), epochs=10)
#print(model.predict_on_batch(np.array(input_array2)), output_array2[1])
#print(model.evaluate(input_array2,output_array2))
prediction = model.predict_on_batch(np.array(input_array2))
true_total = 0
true_correct = 0
for i in range(len(prediction)):
    true_total += 1
    if i < 10:
        print(prediction[i], output_array[i])
    if round(prediction[i][2][0]) == output_array2[i][2]:
        true_correct += 1
print(true_correct, true_total, true_correct/true_total)