
inputs = [1.0, 2.0, 3.0, 2.5]

weights = [[0.2, 0.8, -0.5, 1.0], [0.5, -0.91, 0.26, -0.5], [-0.26, -0.27, 0.17, 0.87]]

biases = [2, 3, 0.5]



# Multiplies Each Input By Corresponding Weight then adds Bias.

inputs = [1.0, 2.0, 3.0, 2.5]

weights = [[0.2, 0.8, -0.5, 1.0], [0.5, -0.91, 0.26, -0.5], [-0.26, -0.27, 0.17, 0.87]]

biases = [2, 3, 0.5]


layer_outputs = [] # Output of Current Layer

for neuron_weights, neuron_bias in zip(weights, biases):

    print(f"\nNeuron Weights: {neuron_weights}, Neuron Bias: {neuron_bias}")

    neuron_output = 0 # Output of Current Neuron

    print(f"Neuron Output: {neuron_output}")

    for n_input, weight in zip(inputs, neuron_weights):

        neuron_output += n_input * weight
        print(f"INNER LOOP - Neuron Output: {neuron_output}")

        
    zipped = (zip(inputs, neuron_weights))
    z_list = list(zipped)    
    print(f"Zipped List: {z_list}")
        

    neuron_output += neuron_bias
    print(f"Final Neuron: {neuron_output}")

    layer_outputs.append(neuron_output)


print(layer_outputs)






