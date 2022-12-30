# a layer with 3 neurons , previous layer has 4 neurons
import numpy as np

# the layer has 3 neurons, previous layer has 4 neurons, so each neuron in the layer has 4 inputs
inputs = np.array([1, 1, 1, 2])  # all neurons in the layer has the same inputs

# but 3 different weights vectors
weights1 = np.array([0.5, 0.6, 0.8, 0.9])
weights2 = np.array([0.5, 0.3, 0.3, 0.9])
weights3 = np.array([0.5, 0.6, 0.8, 0.3])

weights = np.array([weights1, weights2, weights3])

bias1 = 2
bias2 = 1
bias3 = 2.5

bias = [bias1, bias2, bias3]

# number of output = number of neurons in the layer,
print("len weights = ", len(weights))  # the output is a vector of 3 elements (3 outputs)
outputs = np.zeros(len(weights))

for i in range(len(weights)):
    outputs[i] += np.sum(inputs*weights[i])
    print("out after", i, " = ", outputs)

print("bias = ", bias)
for i in range(len(weights)):
    outputs[i] += bias[i]

print("output =\n", outputs)
