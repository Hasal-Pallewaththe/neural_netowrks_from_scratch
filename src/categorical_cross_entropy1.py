# Calculating the loss with Categorical Cross Entropy

import math

softmax_output = [0.85, 0.1, 0.05]
target_output = [1, 0, 0]

loss = -(math.log(softmax_output[0]) * target_output[0] +
         math.log(softmax_output[1]) * target_output[1] +
         math.log(softmax_output[2]) * target_output[2])

print("the categorial cross entropy loss = ", loss)
