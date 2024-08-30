# From AI - 7 (The Smoothies)
# Edited to keep all neuron outputs in memory
# Also added outputs to be added

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
                total += memory[weight]*self.weights[weight]
                memory[self.ID] = self.af(total)
  
  
  
    def __init__(self, network):
        # Exp for Sigmoid
        from math import exp
        self.exp = exp
        # Network and Data
        self.network = []
        self.network.append(network[0]['inputs'])
        self.AFs = {'step':self.step, 'linear':self.linear, 'relu':self.relu, 'sigmoid':self.sigmoid, 'mirroredStep':self.mirroredStep}
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
        self.outputs = []
  
    def run(self, inputs):
        # Compute Neurons
        memory = {'B': 1} 
        for inputVar in self.network[0]:
            memory[inputVar] = inputs[inputVar]
        for layer in self.network[1:-1]:
            for neuron in layer:
                neuron.run(memory)
        # Run Through Outputs
        outputs = {}
        for neuron in self.network[-1]:
            outputs[neuron] = memory[neuron]
        return outputs
    
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
    def mirroredStep(brain, total):
        if total > 0:
            return 1
        elif total < 0:
            return -1
        else:
            return 0
    def sigmoid(brain, total):
        return 1/(1+brain.exp(-total))
    
    # Add Outputs
    def addOutput(self, output):
        self.outputs.append(output)



#-------------------------------------------------
