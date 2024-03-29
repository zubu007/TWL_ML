# TWL_ML
TWL lets you "Train While Labeling" a machine learning or deep learning model.

Public datasets are available which are mostly clean and labeled. However, if you want to create a dataset by labeling on your own, it can be tidious task. Here in this repo, I explain how to collect and label datasets. The repo provides a tool to label the dataset with a GUI. It begins with you selected a model architecture (also with a GUI) for your project and then start labeling your data. The training of the model will be done on the fly as you label your data in real time. This is a great tool to understand how neural networks and other machine learning model works. 

### Project plan
Lets start with labeling an image dataset which is to be trained on a simple neural network.
The app will have 3 frames. 
1. Starting frame: which will have welcome information for the user and the button to guide to the next frame.
2. Setting frames: Here there will be various setting for the user to select. liek model architecture, dataset file lcoation, lose function, optimizer etc.
3. Labeling frame: Here there the images will be loaded and there will be buttons to label the images. On the side of this frame, there will be information about the image like image name, shape, etc. Another side of this frame, will be a figure of the neural network and its weights.
Use matplotlib to show the neural network and other machine learning algorithms in action.
Use Neuralplot to show 3d plot of the neural network.

##### main todo
- [x] create model architecture from the model config
- [x] create pytorch training funtion for 1 batch.
- [ ] Option to select batch size.
- [x] training funtion invoked when labeled.
- [x] Activation function choose.
- [ ] Show the loss and other model info in the GUI

##### small features
- [x] Create a GUI to load and show the images
- [x] Display image information in the side. Like image name, shape, etc.
- [ ] Create a design for the UI
- [ ] Add comments to the code
- [ ] Create a GUI to select the model architecture
- [ ] Create a GUI to select the loss function
- [ ] Create a GUI to select the optimizer
- [x] Create an entry file on the main directory
- [ ] Warn the user to select appropriate input shape (length, width, channel) for the model
- [x] Create a GUI to select the dataset file location
- [x] Use keyboard arrow keys to navigate through the images
- [ ] Add image resizing option
- [ ] Add image augmentation option
- [ ] Add Black and white image option

### Installation

### Contributions
