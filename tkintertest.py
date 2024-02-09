import os
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

class ImageViewer:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Viewer")
        self.root.geometry("800x600")

        self.image_folder = None
        self.image_list = []
        self.current_image_index = 0

        self.canvas = tk.Canvas(self.root, width=600, height=400)
        self.canvas.pack()

        self.btn_load = tk.Button(self.root, text="Load Images", command=self.load_images)
        self.btn_load.pack()

        self.btn_prev = tk.Button(self.root, text="Previous", command=self.show_previous_image)
        self.btn_prev.pack()

        self.btn_next = tk.Button(self.root, text="Next", command=self.show_next_image)
        self.btn_next.pack()

    def load_images(self):
        self.image_folder = filedialog.askdirectory()
        if self.image_folder:
            self.image_list = [os.path.join(self.image_folder, filename) for filename in os.listdir(self.image_folder)]
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

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageViewer(root)
    root.mainloop()
