from input import get_feed_forward_input_array, build_input_from_multiple_files
from keras.models import Sequential
from keras.layers import Dense
import numpy as np
import os

input_files = ['Feature_Files/'+ f for f in os.listdir('Feature_Files')]
input_array, output_array = build_input_from_multiple_files(input_files,get_feed_forward_input_array)
print(len(output_array))

model = Sequential()
model.add(Dense(units=32,activation='relu',input_dim=67))
model.add(Dense(units=1,activation='sigmoid'))
model.compile(loss='binary_crossentropy',optimizer='sgd',metrics=['accuracy'])
model.fit(input_array, output_array, epochs=100, validation_split=.3, batch_size=32)

prediction = model.predict_on_batch(np.array(input_array))
print(len(prediction))

# true_array = []
# false_array = []
# for i in range(len(prediction)):
#     if output_array[i][instr_length-1][0] == 1:
#         true_array.append(prediction[i][instr_length-1][0])
#     else:
#         false_array.append(prediction[i][instr_length-1][0])
# true_array.sort()
# false_array.sort()
# true_median = true_array[(len(true_array))//2]
# false_median = false_array[(len(false_array))//2]
# true_average = sum(true_array)/len(true_array)
# false_average = sum(false_array)/len(false_array)
# print(true_average,false_average)
# print('true_array', true_array[(len(true_array))//4], true_array[(len(true_array))//2], true_array[(3*len(true_array))//4])
# print('false_array', false_array[(len(false_array))//4], false_array[(len(false_array))//2], false_array[(3*len(false_array))//4])

# print("Threshold Calc", true_median, false_median)
threshold = .5#(true_median + false_median)/2

total = 0
true_correct = 0
false_correct = 0
true_incorrect = 0
false_incorrect = 0
for i in range(len(prediction)):
    total += 1
    if prediction[i] > threshold and output_array[i] == 1:
        true_correct += 1
    elif prediction[i] < threshold and output_array[i] == 0:
        false_correct += 1
    elif prediction[i] > threshold and output_array[i] == 0:
        true_incorrect += 1
    else:
        false_incorrect += 1
accuracy = (true_correct + false_correct)/total
precision = (true_correct)/(true_correct+true_incorrect)
recall = (true_correct)/(true_correct+false_incorrect)
print(true_correct,true_incorrect,false_correct,false_incorrect)
print('Accuracy:', accuracy, 'Precision:', precision, 'Recall', recall)