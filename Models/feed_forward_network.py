from input import get_feed_forward_input_array
from keras.models import Sequential

input_array, output_array = get_feed_forward_input_array('../Features/features.txt')
print(input_array[0])

