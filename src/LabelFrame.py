import os
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import csv

class LablePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.parent = parent

        self.shared_data = controller.shared_data

        self.image_folder = None
        self.image_list = []
        self.current_image_index = 0

        self.canvas = tk.Canvas(self, width=600, height=400)
        self.canvas.pack()

        self.label_buttons = []
        for output_node in range(self.shared_data['output nodes']):
            button = tk.Button(self, text=output_node, command=lambda node=output_node: self.label_image(node))
            button.pack()
            self.label_buttons.append(button)

        self.btn_load = tk.Button(self, text="Load Images", command=self.load_images)
        self.btn_load.pack()

        self.btn_prev = tk.Button(self, text="Previous", command=self.show_previous_image)
        self.btn_prev.pack()

        self.btn_next = tk.Button(self, text="Next", command=self.show_next_image)
        self.btn_next.pack()

        self.btn_back = tk.Button(self, text="Settings", command=lambda: controller.show_frame("Setting"))
        self.btn_back.pack()

    def load_images(self):
        self.image_list.clear()
        self.image_folder = filedialog.askdirectory()
        for filename in os.listdir(self.image_folder):
            if filename.endswith(".jpg") or filename.endswith(".png"):
                self.image_list.append(os.path.join(self.image_folder, filename))
        self.show_current_image()

    def show_current_image(self):
        if self.image_list:
            image_path = self.image_list[self.current_image_index]
            img = Image.open(image_path)
            img = img.resize((600, 400), Image.LANCZOS)
            self.photo = ImageTk.PhotoImage(img)
            self.canvas.create_image(0, 0, anchor=tk.NW, image=self.photo)

    def show_previous_image(self):
        if self.image_list:
            self.current_image_index = (self.current_image_index - 1) % len(self.image_list)
            self.show_current_image()

    def show_next_image(self):
        if self.image_list:
            self.current_image_index = (self.current_image_index + 1) % len(self.image_list)
            self.show_current_image()

    def label_image(self, node):
        if self.image_list:
            with open('image_labels.csv', 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([self.image_list[self.current_image_index], node])
            self.show_next_image()

