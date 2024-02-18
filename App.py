import tkinter as tk
from tkinter import ttk
from utils.config import START_PAGE_TEXT
from src.LabelFrame import LablePage
from src.SettingsFrame import SettingsPage
from src.StartFrame import StartPage

class tkinterApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F, s in ((StartPage, "Start"), (SettingsPage, "Setting"), (LablePage, "Label")):
            frame = F(container, self)   # make objects of the classes
            self.frames[s] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        
        self.show_frame("Start")

    def show_frame(self, cont_str):
        frame = self.frames[cont_str]
        frame.tkraise()

if __name__ == "__main__":
    app = tkinterApp()
    app.mainloop()