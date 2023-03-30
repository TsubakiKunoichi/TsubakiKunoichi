
# Werte die übergeben werden
from doctest import OutputChecker
import getopt


_inputs = [1.2,5.1,2.1]

# Gewichtung der einzelnen Werte (wird durch training geändert)
_weights = [3.1,2.1,8.7]

# Wert bis zu welchem das Neuron einen Input ignoriert 
_bias = 3

def getOutput(input, weight, bias):
    output = 0
    for k in range(0,len(input)):
        output += input[k] * weight[k]
    output += bias
    return output

print(getOutput(_inputs,_weights,_bias))