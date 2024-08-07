input = [1.2, 3.3, 5,4] # Outputs from 3 Neurons in previous layer
weight = [1, 8.7, 5.5] # How much OOMPF each input has relative to other inputs
bias = 3 # Each Neuron has a Unique Bias

output = input[0] * weight[0] + input[1] * weight[1] + input[2] * weight[2] + bias
print(output)
