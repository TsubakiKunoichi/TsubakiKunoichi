# Quelle: https://www.youtube.com/watch?v=lGLto9Xd7bU

_inputs = [1,2,3,2.5]

_weights1 = [0.2,0.8,-0.5,1.0]
_weights2 = [0.5,-0.91,0.26,-0.5]
_weights3 = [-0.26,-0.27,0.17,0.87]

_bias1 = 2
_bias2 = 3
_bias3 = 0.5

def getOutput(input, weight, bias):
    output = 0
    for k in range(0,len(input)):
        output += input[k] * weight[k]
    output += bias
    return output

print(getOutput(_inputs,_weights1,_bias1))
print(getOutput(_inputs,_weights2,_bias2))
print(getOutput(_inputs,_weights3,_bias3))

print(pow(4,2.3), 4**2.3, pow(4,2)*pow(4,0.3))
