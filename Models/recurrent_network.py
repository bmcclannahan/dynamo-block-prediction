from input import get_recurrent_input_array, get_recurrent_three_input_array, get_recurrent_n_input_array, build_recurrent_input_from_multiple_files
from keras.models import Sequential, load_model
from keras.layers import Dense, SimpleRNN, LSTM
import numpy as np
import os

instr_length = 3

input_files = ['Feature_Files/'+ f for f in os.listdir('Feature_Files')]
input_array, output_array = build_recurrent_input_from_multiple_files(input_files, get_recurrent_three_input_array)
print(len(output_array))

# model = Sequential()
# model.add(SimpleRNN(units=10, return_sequences=True, input_shape=(instr_length,67)))
# model.add(Dense(units=1,activation='sigmoid'))
# model.compile(loss='binary_crossentropy',optimizer='sgd',metrics=['accuracy'])

# print(np.shape(input_array))
# model.fit(np.array(input_array), np.array(output_array), epochs=30, validation_split=.3)
# model.save('Trained_Models/recurrent_network.h5')

model = load_model('Trained_Models/recurrent_network.h5')

prediction = model.predict_on_batch(np.array(input_array))

true_array = []
false_array = []
for i in range(len(prediction)):
    if output_array[i][instr_length-1][0] == 1:
        true_array.append(prediction[i][instr_length-1][0])
    else:
        false_array.append(prediction[i][instr_length-1][0])
true_array.sort()
false_array.sort()
true_median = true_array[(len(true_array))//2]
false_median = false_array[(len(false_array))//2]
true_average = sum(true_array)/len(true_array)
false_average = sum(false_array)/len(false_array)
print(true_average,false_average)
print('true_array', true_array[(len(true_array))//4], true_array[(len(true_array))//2], true_array[(3*len(true_array))//4])
print('false_array', false_array[(len(false_array))//4], false_array[(len(false_array))//2], false_array[(3*len(false_array))//4])

print("Threshold Calc", true_median, false_median)
threshold = (true_average + false_average)/2

total = 0
true_correct = 0
false_correct = 0
true_incorrect = 0
false_incorrect = 0
for i in range(len(prediction)):
    total += 1
    if prediction[i][instr_length-1][0] > threshold and output_array[i][instr_length-1][0] == 1:
        true_correct += 1
    elif prediction[i][instr_length-1][0] < threshold and output_array[i][instr_length-1][0] == 0:
        false_correct += 1
    elif prediction[i][instr_length-1][0] > threshold and output_array[i][instr_length-1][0] == 0:
        true_incorrect += 1
    else:
        false_incorrect += 1
    # if i < 10:
    #     print(prediction[i], output_array[i])
    #     a = prediction[i][instr_length-1][0] > .3 
    #     b = output_array[i][instr_length-1][0] == 1
    #     c = prediction[i][instr_length-1][0] < .3 
    #     d = output_array[i][instr_length-1][0] == 0
    #     print(a,b,c,d,(a and b), (c and d), (a and b) or (c and d))
accuracy = (true_correct + false_correct)/total
precision = (true_correct)/(true_correct+true_incorrect)
recall = (true_correct)/(true_correct+false_incorrect)
print(true_correct,true_incorrect,false_correct,false_incorrect)
print('Accuracy:', accuracy, 'Precision:', precision, 'Recall', recall)