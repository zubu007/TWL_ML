import os
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import csv
from torchvision import transforms
import torch
import torch.nn as nn

class LablePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.parent = parent

        self.shared_data = controller.shared_data

        self.model = controller.model
        # self.model.eval()
        # define loss function and optimizer
        self.criterion = nn.CrossEntropyLoss()
        self.optimizer = torch.optim.Adam(self.model.parameters(), lr=0.001)
        # get the shape of the last layer
        self.output_layer_shape = self.model.layers[-2].out_features
        # print(self.output_layer_shape)

        self.image_folder = None
        self.image_list = []
        self.current_image_index = 0

        # canvas to display the image
        self.canvas = tk.Canvas(self, width=600, height=600)
        self.canvas.pack()

        # label to display the image info
        self.image_info = tk.Label(self, text="", anchor=tk.W, justify=tk.LEFT)
        self.image_info.pack(side=tk.LEFT, padx=10)

        # buttons to label the image. This is dynamic based on the number of output nodes
        self.label_buttons = []
        # print(self.shared_data['output nodes'])
        for output_node in range(int(self.shared_data['output_layer']["units"])):
            button = tk.Button(self, text=output_node, command=lambda node=output_node: self.label_image(node))
            button.pack()
            self.label_buttons.append(button)

            # bind the number keys to the label buttons
            self.bind(str(output_node + 1), lambda event, node=output_node: self.label_image(node))
            

        self.btn_load = tk.Button(self, text="Load Images", command=self.load_images)
        self.btn_load.pack()
  
        self.btn_prev = tk.Button(self, text="Previous", command=self.show_previous_image)
        self.btn_prev.pack()

        self.btn_next = tk.Button(self, text="Next", command=self.show_next_image)
        self.btn_next.pack()

        self.btn_back = tk.Button(self, text="Settings", command=lambda: controller.show_frame("Setting"))
        self.btn_back.pack()

        # bind the left and right arrow keys
        self.bind("<Left>", self.show_previous_image)
        self.bind("<Right>", self.show_next_image)
        self.focus_set()

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
            img = img.resize((600, 600), Image.LANCZOS)
            self.photo = ImageTk.PhotoImage(img)
            self.canvas.create_image(0, 0, anchor=tk.NW, image=self.photo)
            self.show_image_info()

    def show_previous_image(self, event=None):
        if self.image_list:
            self.current_image_index = (self.current_image_index - 1) % len(self.image_list)
            self.show_current_image()

    def show_next_image(self, event=None):
        if self.image_list:
            self.current_image_index = (self.current_image_index + 1) % len(self.image_list)
            self.show_current_image()

    def label_image(self, node, event=None):
        if self.image_list:
            with open('image_labels.csv', 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([self.image_list[self.current_image_index], node])

            x = Image.open(self.image_list[self.current_image_index])
            # x = x.resize((224, 224), Image.LANCZOS)    <--- This is for the resizing feature
            x = transforms.ToTensor()(x)
            # x = x.unsqueeze(0)   <--- This is for the batching feature
            x = x.view(1, 28 * 28)
            y = torch.zeros(1, self.output_layer_shape)
            y[0][node] = 1

            self.optimizer.zero_grad()

            outputs = self.model.forward(x)
            loss = self.criterion(outputs, y)
            print(loss.item())
            loss.backward()

            self.optimizer.step()

            print(outputs)
            print(y)
            
            self.show_next_image()

    def show_image_info(self):
        image_name = os.path.basename(self.image_list[self.current_image_index])
        image_shape = str(Image.open(self.image_list[self.current_image_index]).size)
        image_index = "Image Info:\n" + str(self.current_image_index) + " / " + str(len(self.image_list))
        self.image_info.config(text= image_index + "\n" + image_name + "\n" + image_shape)


