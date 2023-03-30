# Quelle: https://www.youtube.com/watch?v=lGLto9Xd7bU

_inputs = [1, 2, 3, 2.5]
_weights = [[0.2, 0.8, -0.5, 1.0],
             [0.5, -0.91, 0.26, -0.5],
             [-0.26, -0.27, 0.17, 0.87]]
_biases = [2, 3, 0.5]

def getOutput(input, weight, bias):
    output = 0
    for k in range(0, len(input)):
        output += input[k] * weight[k]
    output += bias
    return output

def GetOutputs():
    outputs = list()
    for i in range(0, len(_weights)):
        outputs.append(getOutput(_inputs, _weights[i], _biases[i]))
    return outputs

print(GetOutputs())