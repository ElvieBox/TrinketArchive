def deepCopy(IN):
    if str(type(IN)) == "<class 'dict'>":
        OUT = {}
        for key in IN.keys():
            value = IN[key]
            copied_value = deepCopy(value)
            OUT[key] = copied_value
        
    elif str(type(IN)) == "<class 'list'>":
        OUT = []
        for item in IN:
            copied_item = deepCopy(item)
            OUT.append(copied_item)
        
    else: 
        OUT = IN
    
    return OUT


def clear(List):
    while len(List) > 0:
        List.pop(0)

def printNetwork(net):
    for layer in net[1:]:
        print("[")
        for neuron in layer:
            print("    " + str(neuron))
        print("],")
    print("\n--------------------------------------------\n")

def getScore(blob):
    return blob.score




# Mutations ---v
from random import randint, random, randrange, choice



def getNeuronIDs(network, layers):
    neuronIDs = []
    for nInput in network[0]['inputs']:
        neuronIDs.append(nInput)
    if layers == "all":
        layers = len(network)-1
    elif layers == 1:
        return neuronIDs
    for layer in network[1:layers]:
        for neuron in layer:
            neuronIDs.append(neuron['id'])
    return neuronIDs


def mutate(network):
    message = "!NULL"
    while message[0] == "!":
        message = "!NULL"
        mutationNum = randint(0,10)
        
        # ADD NEURON
        if mutationNum == 0:
            if randint(0,2) == 0:
                # Add New Layer
                layer = randint(1,len(network)-2)
                network.insert(layer, [])
                message = " NEW LAYER[" + str(layer) + "]"
            else:
                layer = randint(1,len(network)-3)
                message = " LAYER[" + str(layer) + "]"
            # Pick Nueron ID
            neuronID = str(randint(0,99999))
            while neuronID in getNeuronIDs(network, "all"):
                neuronID = str(random.randint(0,99999))
            # Pick Weights
            weights = {}
            weights[choice(getNeuronIDs(network, layer))] = round(random()*randrange(-1,2,2), 2)
            while True:
                if randint(0,1) == 0:
                    weights[choice(getNeuronIDs(network, layer))] = round(random()*randrange(-1,2,2), 2)
                else:
                    break
            # Add Neuron
            network[layer].append({'id': str(neuronID), 'weights': deepCopy(weights)})
            message = "++ADDED NEURON[" + neuronID + "] IN" + message
        
        
        # DELETE NEURON
        elif mutationNum == 1:
            layer = randint(1,len(network)-3)
            attempts = 0
            if network[layer] != []:
                neuron = randint(0,len(network[layer])-1)
                neuronID = network[layer][neuron]["id"]
                message = "--DELETED NUERON[" + neuronID + "] IN LAYER[" + str(layer) + "]" 
                network[layer].pop(neuron)
                for layer in network[1:-1]:
                    for neuron in layer:
                        if neuronID in neuron["weights"].keys():
                            del neuron["weights"][neuronID]
                        if neuron["weights"] == {}:
                            neuron = layer.index(neuron)
                            layer = network.index(layer)
                            weight = choice(getNeuronIDs(network, layer))
                            while (weight in network[layer][neuron]["weights"]):
                                weight = choice(getNeuronIDs(network, layer))
                            network[layer][neuron]["weights"][weight] = round(random()*randrange(-1,2,2), 2)
            elif len(network) == 4:
                message = "!--DELETED NEURON FAIL[too few layers] IN LAYER[" + str(layer) + "]"
            else:
                network.pop(layer)
                message = "--DELETED LAYER[" + str(layer) + "]"
          
          
        # CHANGE WEIGHT
        elif mutationNum == 2 or mutationNum == 3:
            layer = randint(1,len(network)-2)
            if network[layer] == []:
                message = "!*CHANGE WEIGHT FAIL[empty layer] IN L[" + str(layer) + "]"
            else:
                neuron = randint(0,len(network[layer])-1)
                weight = choice(list(network[layer][neuron]["weights"].keys()))
                network[layer][neuron]["weights"][weight] = round(random()*randrange(-1,2,2), 2)
                message = "*CHANGED WEIGHT[" + weight + "] IN NEURON[" + network[layer][neuron]["id"] + "] IN LAYER[" + str(layer) + "]"
          
        
        # ADD WEIGHT
        elif mutationNum == 4 or mutationNum == 5: 
            layer = randint(1,len(network)-2)
            if network[layer] == []:
                message = "!+ADDED WEIGHT FAIL[empty layer] IN LAYER[" + str(layer) + "]"
            else:
                attempt = 0
                neuron = randint(0,len(network[layer])-1)
                weight = choice(getNeuronIDs(network, layer))
                while (weight in network[layer][neuron]["weights"]) and (attempt < 5):
                    weight = choice(getNeuronIDs(network, layer))
                    attempt += 1
                if attempt >= 5:
                    message = "!+ADDED WEIGHT FAIL[too many attempts with duplicate weights] IN NEURON[" + network[layer][neuron]["id"] + "] IN LAYER[" + str(layer) + "]"
                else:
                    network[layer][neuron]["weights"][weight] = round(random()*randrange(-1,2,2), 2)
                    message = "+ADDED WEIGHT[" + weight + "] IN NEURON[" + network[layer][neuron]["id"] + "] IN LAYER[" + str(layer) + "]"
            
        # DELETE WEIGHT
        elif mutationNum == 6 or mutationNum == 7:
            layer = randint(1,len(network)-2)
            if network[layer] == []:
                message = "!-DELETED WEIGHT FAIL[empty layer] IN LAYER[" + str(layer) + "]"
            else:
                neuron = randint(0,len(network[layer])-1)
                if len(network[layer][neuron]["weights"]) == 1:
                    message = "!-DELETED WEIGHT FAIL[too few weights] IN NEURON[" + network[layer][neuron]["id"] +"]IN LAYER[" + str(layer) + "]"
                else:
                    weight = choice(list(network[layer][neuron]["weights"].keys()))
                    del network[layer][neuron]["weights"][weight]
                    message = "-DELETED WEIGHT[" + weight + "] IN NEURON[" + network[layer][neuron]["id"] + "] IN LAYER[" + str(layer) + "]"
            
        
        # QUIT
        elif mutationNum == 8 or mutationNum == 9 or mutationNum == 10:    # Quit
            message = "QUIT"
    
    return message




