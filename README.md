# Wilderness Image Classification using Neural Networks

- by <B>Mayank Patel</B>, IIT Kharagpur (under supervision of <B>Professor Tomas Maul</B>, University of Nottingham, Malaysia)

<br>
<br>

## Abstract:
<p>Satellite image classification is a challenging problem that lies at the crossroads of remote sensing, computer vision, and machine learning. Due to the high similarity in 
the satellite data, deep learning models have found it difficult to classify images with similar characteristics. In this project we have reviewed the currently available 
image classification architectures (LeNet, ResNet, VGG, Google-Inception, DenseNet and MobileNet) based on their accuracies while training them on dataset of monoculture and 
forest. The data used for training and validation has been collected by us for this specific purpose, since this attempt has been done for the first time, there is no
available dataset.</p>
<br><br>


## Data:
The data has been downloaded from Google Earth Pro (GE). We collected 24 (4800 x 2822) images belonging to category of forest and 24 images that belong to non-forest category. These raw images were sliced into          256 x 256-pixel size images. As a result, we have ---- images and ---- images of forest and non-forest category. We have separated 2000 images taken randomly out of ---- images in the validation set. 

<br>
<br>


## Training:
We have trained the following models:
-	LeNet
-	VGGNet11, VGGNet13, VGGNet16, VGGNet19
-	ResNet9
-	Google-Inceptionv1
-	DenseNet
-	MobileNetv2

The models have been trained for 50 epochs with learning rate of 1e-5 while using Adam optimizer. Models were trained on a Nvidia Tesla K80 Graphic Processing Unit.<br><br>

## Results
For visualizations of the training and validation accuracies and losses go to [Train_validation_loss_accuracies](https://github.com/mayankpatel14/Wilderness-Image-Classification/tree/master/Train_validation_loss_accuracies).








