from input import get_recurrent_input_array, get_recurrent_three_input_array, get_recurrent_n_input_array
from keras.models import Sequential
from keras.layers import Dense, SimpleRNN, LSTM
import numpy as np
instr_length = 4
input_array, output_array = get_recurrent_n_input_array('../Features/features.txt', 442, instr_length)
input_array2, output_array2 = get_recurrent_n_input_array('../Features/features2.txt', 598, instr_length)
print(len(input_array2))
print(len(output_array2))

model = Sequential()
model.add(SimpleRNN(units=10, return_sequences=True, input_shape=(instr_length,67)))
model.add(Dense(units=1,activation='sigmoid'))
model.compile(loss='binary_crossentropy',optimizer='sgd',metrics=['accuracy'])

print(np.shape(input_array))
model.fit(np.array(input_array), np.array(output_array), epochs=10)
#print(model.predict_on_batch(np.array(input_array2)), output_array2[1])
#print(model.evaluate(input_array2,output_array2))
model.fit(np.array(input_array2), np.array(output_array2), epochs=10)
prediction = model.predict_on_batch(np.array(input_array2))
true_total = 0
true_correct = 0
total_yes_val = 0
total_no_val = 0
total_yes = 0
total_no = 0
for i in range(len(prediction)):
    if output_array2[i][instr_length-1][0] == 1:
        total_yes_val += prediction[i][instr_length-1][0]
        total_yes += 1
    else:
        total_no_val += prediction[i][instr_length-1][0]
        total_no += 1
print("Threshold Calc", total_yes_val/total_yes, total_no_val/total_no)
threshold = (total_yes_val/total_yes + total_no_val/total_no)/2
for i in range(len(prediction)):
    true_total += 1
    if (prediction[i][instr_length-1][0] > threshold and output_array2[i][instr_length-1][0] == 1) or (prediction[i][instr_length-1][0] < threshold and output_array2[i][instr_length-1][0] == 0):
        true_correct += 1
    # if i < 10:
    #     print(prediction[i], output_array[i])
    #     a = prediction[i][instr_length-1][0] > .3 
    #     b = output_array2[i][instr_length-1][0] == 1
    #     c = prediction[i][instr_length-1][0] < .3 
    #     d = output_array2[i][instr_length-1][0] == 0
    #     print(a,b,c,d,(a and b), (c and d), (a and b) or (c and d))
print(true_correct, true_total, true_correct/true_total)