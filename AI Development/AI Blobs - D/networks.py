testNetwork = [
    {
        "inputs": ["food_x", "food_y", "blob_x", "blob_y"],
        "hiddenAF": "step",
        "outputAF": "mirroredStep",
    },
    [
        {"id": "aaa", "weights": {'food_x': 1}},
        {"id": "bbb", "weights": {'food_y': 1}},
        {"id": "ccc", "weights": {'food_x': -1}},
        {"id": "ddd", "weights": {'food_y': -1}},
    ],
    [
        {"id": "move_right", "weights": {'aaa': 1}},
        {"id": "move_left", "weights": {'ccc': 1}},
        {"id": "move_up", "weights": {'bbb': 1}},
        {"id": "move_down", "weights": {'ddd': 1}},
    ],
    [
        {"id": "move_horizontally", "weights": {'move_right': 1, "move_left": -1}},
        {"id": "move_vertically", "weights": {'move_up': 1, "move_down": -1}},
    ],
    [
        "move_vertically",
        "move_horizontally"
    ]
]



predatorNetwork = [
    {
        "inputs": ["food_x", "food_y", "blob_x", "blob_y"],
        "hiddenAF": "step",
        "outputAF": "mirroredStep",
    },
    [
        {"id": "aaa", "weights": {'blob_x': 1}},
        {"id": "bbb", "weights": {'blob_y': 1}},
        {"id": "ccc", "weights": {'blob_x': -1}},
        {"id": "ddd", "weights": {'blob_y': -1}},
    ],
    [
        {"id": "move_right", "weights": {'aaa': 1}},
        {"id": "move_left", "weights": {'ccc': 1}},
        {"id": "move_up", "weights": {'bbb': 1}},
        {"id": "move_down", "weights": {'ddd': 1}},
    ],
    [
        {"id": "move_horizontally", "weights": {'move_right': 1, "move_left": -1}},
        {"id": "move_vertically", "weights": {'move_up': 1, "move_down": -1}},
    ],
    [
        "move_vertically",
        "move_horizontally"
    ]
]


blankNetwork = [
    {
        "inputs": ["food_x", "food_y", "blob_x", "blob_y"],
        "hiddenAF": "step",
        "outputAF": "mirroredStep",
    },
    [],
        # Inner Layers
    [
        {"id": "move_horizontally", "weights": {"B": 0}},   # Weights added by program
        {"id": "move_vertically", "weights": {"B": 0}},     # Weights added by program
    ],
    [
        "move_vertically",
        "move_horizontally"
    ]
]


# Work in Progress Deep Copy
def deepCopy(data):
    if str(type(data)) == "<class 'dict'>":
        copy = {}
        for key in data.keys():
            copy[key] = deepCopy(data[key])
    if str(type(data)) == "<class 'list'>":
        copy = []
        for item in data:
            copy.append(deepCopy(item))
    else:
        return data
    return copy
    
    
