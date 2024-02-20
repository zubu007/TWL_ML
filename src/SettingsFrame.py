import tkinter as tk
from tkinter import ttk
import json

class SettingsPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        # self.config = {
        #     "input nodes": "0",
        #     "batch size": 32,
        #     "output nodes": 2
        # }

        with open('models\ANN.json', 'r') as f:
            self.config = json.load(f)



        label = ttk.Label(self, text="Settings", font=("Verdana", 35))
        label.grid(row=0, column=4, padx=10, pady=10)

        outputNodesLabel = ttk.Label(self, text="Output Nodes:")
        outputNodesLabel.grid(row=1, column=4, padx=10, pady=10)
        self.outputNodesCombo = ttk.Combobox(self, values=[1, 2, 3, 4, 5])
        self.outputNodesCombo.current(0)
        self.outputNodesCombo.grid(row=1, column=5, padx=10, pady=10)

        hiddenNodesLabel = ttk.Label(self, text="Hidden Nodes:")
        hiddenNodesLabel.grid(row=1, column=2, padx=10, pady=10)
        self.hiddenNodesLabel = ttk.Entry(self)
        self.hiddenNodesLabel.insert(0, "100")
        self.hiddenNodesLabel.grid(row=1, column=3, padx=10, pady=10)

        heightLabel = ttk.Label(self, text="Height:")
        heightLabel.grid(row=2, column=2, padx=10, pady=10)
        self.heightEntry = ttk.Entry(self)
        self.heightEntry.insert(0, "224")
        self.heightEntry.grid(row=2, column=3, padx=10, pady=10)

        widthLabel = ttk.Label(self, text="Width:")
        widthLabel.grid(row=3, column=2, padx=10, pady=10)
        self.widthEntry = ttk.Entry(self)
        self.widthEntry.insert(0, "224")
        self.widthEntry.grid(row=3, column=3, padx=10, pady=10)

        channelLabel = ttk.Label(self, text="Channel:")
        channelLabel.grid(row=4, column=2, padx=10, pady=10)
        self.channelEntry = ttk.Entry(self)
        self.channelEntry.insert(0, "1")
        self.channelEntry.grid(row=4, column=3, padx=10, pady=10)


        labelButton = ttk.Button(self, text="Label", command=lambda: self.label_page(controller))
        labelButton.grid(row=1, column=1, padx=10, pady=10)

        homeButton = ttk.Button(self, text="Back to Home", command=lambda: controller.show_frame("Start"))
        homeButton.grid(row=2, column=1, padx=10, pady=10)

    def label_page(self, controller):
        self.config['output_layer']["units"] = int(self.outputNodesCombo.get())
        self.config['input_layer']["units"] = int(self.heightEntry.get()) * int(self.widthEntry.get()) * int(self.channelEntry.get())
        self.config['hidden_layers'][0]["units"] = int(self.hiddenNodesLabel.get())
        with open('models\ANN.json', 'w') as f:
            json.dump(self.config, f, indent=4)
        # controller.shared_data['output nodes'] = self.config['output nodes']
        controller.show_label_frame()
