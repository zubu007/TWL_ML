# import torch
import torch.nn as nn
import json


class ANNModel(nn.Module):
    def __init__(self, json_file):
        super(ANNModel, self).__init__()

        with open(json_file, 'r') as f:
            config = json.load(f)

        self.layers = nn.ModuleList()
        self.layers.append(nn.Linear(config['input_layer']['units'], config['hidden_layers'][0]['units']))
        if config['hidden_layers'][0]['activation'] == 'sigmoid':  # change this to a suitable activation function
            self.layers.append(nn.Sigmoid())
        elif config['hidden_layers'][0]['activation'] == 'tanh':
            self.layers.append(nn.Tanh())
        else:
            self.layers.append(nn.ReLU())
        if len(config['hidden_layers']) > 1:
            for i in range(1, len(config['hidden_layers'])):
                self.layers.append(nn.Linear(config['hidden_layers'][i-1]['units'], config['hidden_layers'][i]['units']))
                if config['hidden_layers'][0]['activation'] == 'sigmoid':
                    self.layers.append(nn.Sigmoid())
                elif config['hidden_layers'][0]['activation'] == 'tanh':
                    self.layers.append(nn.Tanh())
                else:
                    self.layers.append(nn.ReLU())
        self.layers.append(nn.Linear(config['hidden_layers'][-1]['units'], config['output_layer']['units']))
        if config['output_layer']['activation'] == '':
            self.layers.append(nn.Sigmoid())

    def forward(self, x):
        for layer in self.layers:
            x = layer(x)
        return x