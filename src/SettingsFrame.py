import tkinter as tk
from tkinter import ttk

class SettingsPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        from LabelFrame import LablePage
        from StartFrame import StartPage
        label = ttk.Label(self, text="Settings", font=("Verdana", 35))
        label.grid(row=0, column=4, padx=10, pady=10)
        labelButton = ttk.Button(self, text="Label", command=lambda: controller.show_frame("Label"))
        labelButton.grid(row=1, column=1, padx=10, pady=10)
        homeButton = ttk.Button(self, text="Back to Home", command=lambda: controller.show_frame("Start"))
        homeButton.grid(row=2, column=1, padx=10, pady=10)