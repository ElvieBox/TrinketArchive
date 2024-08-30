# https://trinket.io/python/48a2e6f5b3

# "Bologna"

class Brain():
  
    class Neuron():
        def __init__(self, data, af):
            # Sets up Neuron Data
            from math import exp
            self.exp = exp
            self.ID = data['id']
            self.af = af
            self.weights = data['weights']
        def run(self, memory):
            # Adds up inputs and squashing
            total = 0
            for weight in self.weights:
                total += memory[0][weight]*self.weights[weight]
                memory[1][self.ID] = self.af(total)
  
  
  
    def __init__(self, network):
        # Exp for Sigmoid
        from math import exp
        self.exp = exp
        # Network and Data
        self.network = []
        self.network.append(network[0]['inputs'])
        self.AFs = {'step':self.step, 'linear':self.linear, 'relu':self.relu, 'sigmoid':self.sigmoid}
        # Creating Neurons
        for layer in network[1:-2]:
            self.network.append([])
            for nData in layer:
                self.network[-1].append(self.Neuron(nData, self.AFs[network[0]['hiddenAF']])) 
        # Output Neurons
        self.network.append([])
        for nData in network[-2]:
            self.network[-1].append(self.Neuron(nData, self.AFs[network[0]['outputAF']]))
        # Set up Outputs
        self.network.append(network[-1])
  
    def run(self, inputs):
        # Compute Neurons
        memory = [{'B': 1}, {}]
        for inputVar in self.network[0]:
            memory[0][inputVar] = inputs[inputVar]
        for layer in self.network[1:-1]:
            for neuron in layer:
                neuron.run(memory)
            memory = [memory[1], {}]
            memory[0]['B'] = 1
        # Run Through Outputs
        print(memory)
        for neuron in self.network[-1]:
            if memory[0][neuron] > 0:
                self.network[-1][neuron]()
    
    # Activation Functions   
    def step(brain, total):
        if total > 0:
            return 1
        elif total <= 0:
            return 0
    def linear(brain, total):
        return total
    def relu(brain, total):
        if total > 1:
            return 1
        elif total < 0:
            return 0
        else:
            return total
    def sigmoid(brain, total):
        return 1/(1+brain.exp(-total))


#-------------------------------------------------

def exampleOutput1():
    print('exampleOutput1')
def exampleOutput2():
    print('exampleOutput2')


smoothie = Brain(
[
    {
        "inputs": ["a", "b"],
        "hiddenAF": "sigmoid",
        "outputAF": "step",
        "topid": "N5"
    },
    [
        {"id": "N1", "weights": {"a": .5}},
        {"id": "N2", "weights": {"b": -.5}}
    ],
    [
        {"id": "N3", "weights": {"N1": .5}},
        {"id": "N4", "weights": {"N2": 2}}
    ],
    {
        "N3": exampleOutput1,
        "N4": exampleOutput2
    }
])

inputs = {
    'a': 5,
    'b': 5
}

smoothie.run(inputs)
