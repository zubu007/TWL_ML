import PySimpleGUI as sg
from PIL import Image
import os
import numpy as np

def load_images_from_folder(folder_path):
    image_list = []
    for filename in os.listdir(folder_path):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
            img = Image.open(os.path.join(folder_path, filename))
            img = np.array(img)
            img = np.stack((img,)*3, axis=-1)
            img = Image.fromarray(img)
            image_list.append(img)
    return image_list

def main():
    folder_path = "MNIST-JPG\\MNIST Dataset JPG format\\MNIST - JPG - testing\\0"  # Replace with your actual folder path
    images = load_images_from_folder(folder_path)

    layout = [
        [sg.Image(key="-IMAGE-")],
        [sg.Button("Previous"), sg.Button("Next")]
    ]

    window = sg.Window("Image Viewer", layout)

    index = 0
    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED:
            break
        elif event == "Previous":
            index = (index - 1) % len(images)
        elif event == "Next":
            index = (index + 1) % len(images)
        print(images[index])
        window["-IMAGE-"].update(data=images[index].tobytes())

    window.close()

if __name__ == "__main__":
    main()
