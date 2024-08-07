
input = [1.0, 2.0, 3.0, 2.5]

weight0 = [0.2, 0.8, -0.5, 1.0]
weight1 = [0.5, -0.91, 0.26, -0.5] 
weight2 = [-0.26, -0.27, 0.17, 0.87]

bias0 = 2
bias1 = 3
bias2 = 0.5


output = [input[0] * weight0[0] + input[1] * weight0[1] + input[2] * weight0[2] + input[3] * weight0[3] + bias0,
          input[0] * weight1[0] + input[1] * weight1[1] + input[2] * weight1[2] + input[3] * weight1[3] + bias1,
          input[0] * weight2[0] + input[1] * weight2[1] + input[2] * weight2[2] + input[3] * weight2[3] + bias2]

print(output)







