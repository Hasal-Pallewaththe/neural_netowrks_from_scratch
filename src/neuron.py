# consider one neuron , in a dense neural net

# the neuron has 4 inputs (previous layer has 4 neurons), so it has 4 weights
inputs = [1, 1, 1, 2, 3, 4]
weights = [0.5, 0.6, 0.8, 0.9, 0.7, 0.2]
bias = 2
output = 0
for i in range(len(inputs)):
    output += inputs[i]*weights[i]


output = output + bias
print("output =\n", output)

# after this the activation function, this entire output is goes to activation func and the actual output is, output = activation_func(output)
