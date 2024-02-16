import tkinter as tk
from tkinter import ttk

class SettingsPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.config = {
            "input shape": "tor maire",
            "batch size": 32,
            "output nodes": 2
        }
        label = ttk.Label(self, text="Settings", font=("Verdana", 35))
        label.grid(row=0, column=4, padx=10, pady=10)

        outputNodesLabel = ttk.Label(self, text="Output Nodes:")
        outputNodesLabel.grid(row=1, column=4, padx=10, pady=10)
        self.outputNodesCombo = ttk.Combobox(self, values=[1, 2, 3, 4, 5])
        self.outputNodesCombo.current(0)
        self.outputNodesCombo.grid(row=1, column=5, padx=10, pady=10)
        


        labelButton = ttk.Button(self, text="Label", command=lambda: self.label_page(controller))
        labelButton.grid(row=1, column=1, padx=10, pady=10)
        homeButton = ttk.Button(self, text="Back to Home", command=lambda: controller.show_frame("Start"))
        homeButton.grid(row=2, column=1, padx=10, pady=10)

    def label_page(self, controller):
        self.config['output nodes'] = self.outputNodesCombo.get()
        controller.shared_data['output nodes'] = self.config['output nodes']
        controller.show_label_frame()
