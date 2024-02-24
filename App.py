import tkinter as tk
from tkinter import ttk
from src.LabelFrame import LablePage
from src.SettingsFrame import SettingsPage
from src.StartFrame import StartPage
import json
from src.models.models import ANNModel

class tkinterApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.container = container

        self.model = None

        self.shared_data = {}

        self.frames = {}
        for F, s in ((StartPage, "Start"), (SettingsPage, "Setting")):
            frame = F(container, self)   # make objects of the classes
            self.frames[s] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        
        self.show_frame("Start")

    def show_frame(self, cont_str):
        # method to raise the frame
        print(self.shared_data)
        frame = self.frames[cont_str]
        frame.tkraise()

    def show_label_frame(self):
        # this creates the label frame using the shared data after the data is loaded from the json file
        self.model = ANNModel('src\models\ANN.json')
        print(self.model)
        with open('src\models\ANN.json', 'r') as f:
            self.shared_data = json.load(f)
        label_frame = LablePage(self.container, self)
        label_frame.grid(row=0, column=0, sticky="nsew")
        label_frame.tkraise()

if __name__ == "__main__":
    app = tkinterApp()
    app.mainloop()