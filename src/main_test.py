import tkinter as tk
from tkinter import ttk
from utils.config import START_PAGE_TEXT
from LabelFrame import LablePage
from SettingsFrame import SettingsPage
from StartFrame import StartPage

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

# class StartPage(tk.Frame):
#     def __init__(self, parent, controller):
#         tk.Frame.__init__(self, parent)
#         label = ttk.Label(self, text=START_PAGE_TEXT, font=("Verdana", 15))
#         label.grid(row=0, column=1, padx=10, pady=10)
#         nextButton = ttk.Button(self, text="Lets Start", command=lambda: controller.show_frame("Setting"))
#         nextButton.grid(row=1, column=1, padx=10, pady=10)

# class SettingsPage(tk.Frame):
#     def __init__(self, parent, controller):
#         tk.Frame.__init__(self, parent)
#         label = ttk.Label(self, text="Settings", font=("Verdana", 35))
#         label.grid(row=0, column=4, padx=10, pady=10)
#         labelButton = ttk.Button(self, text="Label", command=lambda: controller.show_frame(LablePage))
#         labelButton.grid(row=1, column=1, padx=10, pady=10)
#         homeButton = ttk.Button(self, text="Back to Home", command=lambda: controller.show_frame(StartPage))
#         homeButton.grid(row=2, column=1, padx=10, pady=10)

# class LablePage(tk.Frame):
#     def __init__(self, parent, controller):
#         tk.Frame.__init__(self, parent)
#         label = ttk.Label(self, text="Lable", font=("Verdana", 35))
#         label.grid(row=0, column=4, padx=10, pady=10)
#         button = ttk.Button(self, text="Back to Home", command=lambda: controller.show_frame(StartPage))
#         button.grid(row=1, column=1, padx=10, pady=10)

if __name__ == "__main__":
    app = tkinterApp()
    app.mainloop()
