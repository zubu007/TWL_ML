import tkinter as tk
from tkinter import ttk
from src.utils.config import START_PAGE_TEXT

class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text=START_PAGE_TEXT, font=("Verdana", 15))
        label.grid(row=0, column=1, padx=10, pady=10)
        nextButton = ttk.Button(self, text="Lets Start", command=lambda: controller.show_frame("Setting"))
        nextButton.grid(row=1, column=1, padx=10, pady=10)